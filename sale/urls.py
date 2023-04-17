from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sale-home'),
    path('about/', views.about, name='sale-about'),
    ]



