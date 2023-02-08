from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('api/modmotorg/', views.ModMotorGListCreate.as_view()),
    path('api/modtransmission/', views.ModTransmissionGListCreate.as_view()),
    path('api/mashins/', views.MashinsListCreate.as_view()),
    path('api/modmashinsg/', views.ModMashinsGListCreate.as_view()),
    path('api/moddrivebridgeg/', views.ModDriveBridgeGListCreate.as_view()),
    path('api/modcontrollbridgeg/', views.ModControllBridgeGListCreate.as_view()),
    path('api/recoverymethodg/', views.RecoveryMethodGListCreate.as_view()),
    path('api/complaint/', views.ComplaintListCreate.as_view()),
    path('api/usersailant/', views.UsersSilantListCreate.as_view()),
    path('api/naturerefusalg/', views.NatureRefusalGListCreate.as_view()),
    path('api/clientg/', views.ClientGListCreate.as_view()),
    path('api/sersvice/', views.SersviceListCreate.as_view()),
    path('api/vidtog/', views.VidTOGListCreate.as_view()),
    path('api/to/', views.TOListCreate.as_view()),
]
