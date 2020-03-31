from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'predict'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('result/',views.result, name = 'result'),
]