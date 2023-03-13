from rest_framework import viewsets
from rest_framework import permissions

from backend.models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                            ModControllBridgeG, RecoveryMethodG, Complaint, NatureRefusalG,
                            ClientG, Sersvice, VidTOG, TO, FailureNodeReference, )
from .serializers import (ModMotorGSerializer, ModTransmissionGSerializer, MashinsSerializer, ModMashinsGSerializer,
                          ModDriveBridgeGSerializer, ModControllBridgeGSerializer, RecoveryMethodGSerializer,
                          ComplaintSerializer, NatureRefusalGSerializer, SersviceSerializer,
                          VidTOGSerializer, TOSerializer, FailureNodeReferenceSerializer,
                          ClientGSerializer)


# Список моделей моторов
class ModMotorGViewSet(viewsets.ModelViewSet):
    queryset = ModMotorG.objects.all()
    serializer_class = ModMotorGSerializer


# Список моделей трансмиссий
class ModTransmissionGViewSet(viewsets.ModelViewSet):
    queryset = ModTransmissionG.objects.all()
    serializer_class = ModTransmissionGSerializer


# Список машин
class MashinsViewSet(viewsets.ModelViewSet):
    queryset = Mashins.objects.all()
    serializer_class = MashinsSerializer


# Список моделей машин
class ModMashinsGViewSet(viewsets.ModelViewSet):
    queryset = ModMashinsG.objects.all()
    serializer_class = ModMashinsGSerializer


# Список моделей ведущего моста
class ModDriveBridgeGViewSet(viewsets.ModelViewSet):
    queryset = ModDriveBridgeG.objects.all()
    serializer_class = ModDriveBridgeGSerializer


# Список моделей управляемого моста
class ModControllBridgeGViewSet(viewsets.ModelViewSet):
    queryset = ModControllBridgeG.objects.all()
    serializer_class = ModControllBridgeGSerializer


# Список способов восстановления
class RecoveryMethodGViewSet(viewsets.ModelViewSet):
    queryset = RecoveryMethodG.objects.all()
    serializer_class = RecoveryMethodGSerializer


# Список клиентов
class ClientGViewSet(viewsets.ModelViewSet):
    queryset = ClientG.objects.all()
    serializer_class = ClientGSerializer


# Список рекламаций
class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


# Список характера отказов
class NatureRefusalGViewSet(viewsets.ModelViewSet):
    queryset = NatureRefusalG.objects.all()
    serializer_class = NatureRefusalGSerializer


# Список видов ТО
class VidTOGViewSet(viewsets.ModelViewSet):
    queryset = VidTOG.objects.all()
    serializer_class = VidTOGSerializer


# Список ТО
class TOViewSet(viewsets.ModelViewSet):
    queryset = TO.objects.all()
    serializer_class = TOSerializer


# Список сервисных компаний
class SersviceViewSet(viewsets.ModelViewSet):
    queryset = Sersvice.objects.all()
    serializer_class = SersviceSerializer
    permission_classes = []


class FailureNodeReferenceViewSet(viewsets.ModelViewSet):
    queryset = FailureNodeReference.objects.all()
    serializer_class = FailureNodeReferenceSerializer
