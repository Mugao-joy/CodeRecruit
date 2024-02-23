from django.urls import path
from .views import user_login, user_register
from . import views

app_name = 'Authentication'
urlpatterns = [
    path('register/', views.user_register, name='register'),
    path ('login/', views.user_login, name = 'login')
    
]