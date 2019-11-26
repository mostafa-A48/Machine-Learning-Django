from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from .models import News

def index(request):
    
    return render(request,'index.html',context={})

def predict(request):
    headline = request.GET['headline']
    headline = [headline]
    loaded_vec = CountVectorizer(vocabulary=pickle.load(open("features.pkl", "rb")))
    loaded_tfidf = pickle.load(open("tfidf.pkl","rb"))
    loaded_model = pickle.load(open("model.pkl","rb"))
    X_new_counts = loaded_vec.transform(headline)
    X_new_tfidf = loaded_tfidf.transform(X_new_counts)
    predicted = loaded_model.predict(X_new_tfidf)

    return render(request,'index.html',context={'name': predicted[0]}) 

def scrape(request):
    # driver = Chrome("D:/chromedriver_win32/chromedriver.exe")
    link = "https://www.pajhwok.com/en/health"
    chrome_options = ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = Chrome("D:/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(link)
    headlines = [headline.text for headline in driver.find_elements_by_xpath("//h2[@class='node-title']/a")]
    for headline in headlines:
        new_headline = [headline]
        loaded_vec = CountVectorizer(vocabulary=pickle.load(open("features.pkl", "rb")))
        loaded_tfidf = pickle.load(open("tfidf.pkl","rb"))
        loaded_model = pickle.load(open("model.pkl","rb"))
        X_new_counts = loaded_vec.transform(new_headline)
        X_new_tfidf = loaded_tfidf.transform(X_new_counts)
        predicted = loaded_model.predict(X_new_tfidf)
        news = News()
        news.headline = headline
        news.predicted_category = predicted
        news.save()
    return render(request,'index.html',context={'message': 'The Site Has Been Successfully Scraped'})   