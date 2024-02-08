from django.urls import path
from .views import user_login, user_register

app_name = 'Authentication'
urlpatterns = [
    path ('login/', user_login, name = 'landing'),
    path ('register/', user_register, name = 'register')
]