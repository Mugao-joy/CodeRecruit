from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'crjob_board'

urlpatterns = [
    path ('', views.landing, name = 'landing'),
    path ('home/', views.home, name = 'home'),
    path ('landing/', views.landing, name = 'landing'),
    path ('create/', views.create, name = 'create'),
    path('submitted/', views.submitted, name='submitted'),
    path('search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)