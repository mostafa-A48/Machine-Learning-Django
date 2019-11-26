from django.urls import path
from . import views

app_name = 'mlnhp'

urlpatterns = [
    # mlnhp/
    path('',views.index,name='index'),
    path('predict',views.predict,name='predict'),
    path('scrape',views.scrape, name='scrape')
]

