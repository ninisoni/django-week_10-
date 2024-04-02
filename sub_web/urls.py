from .views import home, about, contact, web
from django.urls import path

urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('', web),
]