from django.urls import path, include
from .api_router import router

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),

]
