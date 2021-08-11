from django.contrib import admin
from django.urls import path
from app import views

app_name='ytdownloader'

urlpatterns = [
   path('',views.index,name='home'),
   path('donations/',views.donations,name='donations'),
   path('contact/',views.contact,name='contact'),
   path('download/',views.download,name='download'),
   path('download/<resolution>/',views.ytud_download,name='finish'),
]
