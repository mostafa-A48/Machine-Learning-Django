import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import pickle
import sys
import os
import django

sys.path.extend(['D:/Projects/news'])
sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")
django.setup()

print(os.listdir())
data = pd.read_json('machine-learning/News_Dataset.json')
data = data[data.category != 'POLITICS']
data = data[data.category != 'ENTERTAINMENT']
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
features = vect.fit_transform(data.headline)
pickle.dump(vect.vocabulary_, open("machine-learning/features.pkl","wb"))
from sklearn.feature_extraction.text import CountVectorizer

#GET VECTOR COUNT
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data.headline)

from sklearn.feature_extraction.text import TfidfTransformer

#TRANSFORM WORD VECTOR TO TF IDF
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

pickle.dump(tfidf_transformer, open("machine-learning/tfidf.pkl","wb"))

from sklearn.model_selection import train_test_split
from sklearn import svm
clf_svm = svm.LinearSVC()
X_train, X_test, y_train, y_test = train_test_split(X_train_tfidf, data.category, test_size=0.25, random_state=42)
clf_svm.fit(X_train_tfidf, data.category)

pickle.dump(clf_svm, open("machine-learning/model.pkl", "wb"))