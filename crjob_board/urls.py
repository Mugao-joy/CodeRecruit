from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import landing,home

app_name = 'crjob_board'
urlpatterns = [
    path ('', landing, name = 'landing'),
    path ('home/', home, name = 'home')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)