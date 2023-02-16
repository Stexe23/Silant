from rest_framework import generics, viewsets
from rest_framework import permissions

from ..backend.models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                              ModControllBridgeG, RecoveryMethodG, Complaint, UsersSilant, NatureRefusalG,
                              ClientG, Sersvice, VidTOG, TO)
from .serializers import (ModMotorGSerializer, ModTransmissionGSerializer, MashinsSerializer, ModMashinsGSerializer,
                          ModDriveBridgeGSerializer, ModControllBridgeGSerializer, RecoveryMethodGSerializer,
                          ComplaintSerializer, UsersSilantSerializer, NatureRefusalGSerializer,
                          ClientGSerializer, SersviceSerializer, VidTOGSerializer, TOSerializer)


# Список моделей моторов
class ModMotorGListCreate(generics.ListCreateAPIView):
    model = ModMotorG
    queryset = ModMotorG.objects.all()
    serializer_class = ModMotorGSerializer


# Список моделей трансмиссий
class ModTransmissionGListCreate(generics.ListCreateAPIView):
    model = ModTransmissionG
    queryset = ModTransmissionG.objects.all()
    serializer_class = ModTransmissionGSerializer


# Список машин
class MashinsListCreate(generics.ListCreateAPIView):
    model = Mashins
    queryset = Mashins.objects.all()
    serializer_class = MashinsSerializer


# Список моделей машин
class ModMashinsGListCreate(generics.ListCreateAPIView):
    model = ModMashinsG
    queryset = ModMashinsG.objects.all()
    serializer_class = ModMashinsGSerializer


# Список моделей ведущего моста
class ModDriveBridgeGListCreate(generics.ListCreateAPIView):
    model = ModDriveBridgeG
    queryset = ModDriveBridgeG.objects.all()
    serializer_class = ModDriveBridgeGSerializer


# Список моделей управляемого моста
class ModControllBridgeGListCreate(generics.ListCreateAPIView):
    model = ModControllBridgeG
    queryset = ModControllBridgeG.objects.all()
    serializer_class = ModControllBridgeGSerializer


# Список способов восстановления
class RecoveryMethodGListCreate(generics.ListCreateAPIView):
    model = RecoveryMethodG
    queryset = RecoveryMethodG.objects.all()
    serializer_class = RecoveryMethodGSerializer


# Список клиентов
class ClientGListCreate(generics.ListCreateAPIView):
    model = ClientG
    queryset = ClientG.objects.all()
    serializer_class = ClientGSerializer


# Список рекламаций
class ComplaintListCreate(generics.ListCreateAPIView):
    model = Complaint
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


# Список характера отказов
class NatureRefusalGListCreate(generics.ListCreateAPIView):
    model = NatureRefusalG
    queryset = NatureRefusalG.objects.all()
    serializer_class = NatureRefusalGSerializer


# Список видов ТО
class VidTOGListCreate(generics.ListCreateAPIView):
    model = VidTOG
    queryset = VidTOG.objects.all()
    serializer_class = VidTOGSerializer


# Список ТО
class TOListCreate(generics.ListCreateAPIView):
    model = TO
    queryset = TO.objects.all()
    serializer_class = TOSerializer


# Список сервисных компаний
class SersviceListCreate(generics.ListCreateAPIView):
    model = Sersvice
    queryset = Sersvice.objects.all()
    serializer_class = SersviceSerializer


# Список пользователей
class UsersSilantListCreate(generics.ListCreateAPIView):
    model = UsersSilant
    queryset = UsersSilant.objects.all()
    serializer_class = UsersSilantSerializer
