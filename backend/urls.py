from django.contrib import admin
from django.urls import path, include
from frontend import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/accounts/', include('allauth.urls')),
]
