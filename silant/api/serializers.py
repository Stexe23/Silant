from rest_framework import serializers
from users.models import CustomUser
from silant.backend.models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                                   ModControllBridgeG, RecoveryMethodG, Complaint, NatureRefusalG,
                                   ClientG, Sersvice, VidTOG, TO)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ModMotorGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModMotorG
        fields = '__all__'


class ModTransmissionGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModTransmissionG
        fields = '__all__'


class MashinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mashins
        fields = '__all__'


class ModMashinsGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModMashinsG
        fields = '__all__'


class ModDriveBridgeGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModDriveBridgeG
        fields = '__all__'


class ModControllBridgeGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModControllBridgeG
        fields = '__all__'


class RecoveryMethodGSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethodG
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class NatureRefusalGSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatureRefusalG
        fields = '__all__'


class ClientGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientG
        fields = '__all__'


class SersviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sersvice
        fields = '__all__'


class VidTOGSerializer(serializers.ModelSerializer):
    class Meta:
        model = VidTOG
        fields = '__all__'


class TOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TO
        fields = '__all__'
