from django.contrib import admin
from django.urls import path
from blog.views import index, alimentos, ads, apicultura, informatica

urlpatterns = [
    path('', index, name = 'index'),
    path('alimentos', alimentos, name = 'alimentos'),
    path('ads', ads, name = 'ads'),
    path('apicultura', apicultura, name = 'apicultura'),
    path('informatica', informatica, name = 'informatica'),
]