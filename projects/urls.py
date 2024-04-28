from django.urls import path, include
from . import views

app_name = 'projects'  # Set the app_name attribute

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('about/', views.about, name='about'),
]
