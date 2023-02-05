from django.urls import path, include
from .views import (ModMotorGList, ModTransmissionGList, MashinsList, ModMashinsGList, ModDriveBridgeGList,
                    ModControllBridgeGList, RecoveryMethodGList, ComplaintList, UsersSilantList, NatureRefusalGList,
                    ClientGList, SersviceList, VidTOGList, TOList)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', ModMotorGList.as_view()),
    path('', ModTransmissionGList.as_view()),
    path('', MashinsList.as_view()),
    path('', ModMashinsGList.as_view()),
    path('', ModDriveBridgeGList.as_view()),
    path('', ModControllBridgeGList.as_view()),
    path('', RecoveryMethodGList.as_view()),
    path('', ComplaintList.as_view()),
    path('', UsersSilantList.as_view()),
    path('', NatureRefusalGList.as_view()),
    path('', ClientGList.as_view()),
    path('', SersviceList.as_view()),
    path('', VidTOGList.as_view()),
    path('', TOList.as_view()),
]
