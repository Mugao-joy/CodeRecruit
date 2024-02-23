from django.urls import path
from .views import user_login, user_register

app_name = 'Authentication'
urlpatterns = [
    path ('register/', user_register, name = 'register'),
    path ('login/', user_login, name = 'login')
    
]