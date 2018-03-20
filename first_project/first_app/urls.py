from django.urls import path
from first_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('static-image/', views.img, name='img')
]