from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('hakkında', views.about, name= 'about'),
    path('yazılar', views.yazilar, name= 'yazilar'),
    path('yazı/<slug:slug>', views.yazidetay, name= 'yazidetay'),
]