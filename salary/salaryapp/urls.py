# urls.py

from django.urls import path
from .views import home,registration,login

urlpatterns = [
    path('', home, name='home'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    # Add other URL patterns for your application if needed
]
