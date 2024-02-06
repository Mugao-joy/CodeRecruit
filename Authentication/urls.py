from django.urls import path
from .views import user_login

app_name = 'Authentication'
urlpatterns = [
    path ('login/', user_login, name = 'landing')
]