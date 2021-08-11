from django.contrib import admin
from django.urls import path,include
from django.conf import SettingsReference, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
] 
