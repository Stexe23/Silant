from rest_framework import serializers
from ..backend.models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                              ModControllBridgeG, RecoveryMethodG, Complaint, UsersSilant, NatureRefusalG,
                              ClientG, Sersvice, VidTOG, TO)


class ModMotorGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModMotorG
        fields = ('model_motor', 'text_mo',)


class ModTransmissionGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModTransmissionG
        fields = ('model_transmission', 'text_t',)


class MashinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mashins
        fields = ('zav_nom_mashins', 'model_mashins', 'model_motor', 'zav_nom_motor',
                  'model_transmission', 'zav_nom_transmission', 'model_drive_bridge',
                  'zav_nom_drive_bridge', 'model_controll_bridge', 'zav_nom_controll_bridge',
                  'dogovor', 'date_shipment', 'consignee', 'delivery_address',
                  'equipment', 'client', 'service_company',)


class ModMashinsGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModMashinsG
        fields = ('model_mashins', 'text_ma',)


class ModDriveBridgeGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModDriveBridgeG
        fields = ('model_drive_bridge', 'text_db',)


class ModControllBridgeGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModControllBridgeG
        fields = ('model_controll_bridge', 'text_cb',)


class RecoveryMethodGSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethodG
        fields = ('recovery_method', 'text_rec',)


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id_c', 'date_refusal', 'mtdf_c', 'reason_refusal',
                  'recovery_method', 'spare', 'date_recovery', 'mashins_c',)


class UsersSilantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersSilant
        fields = ('username', 'password', 'user_email', 'name', 'position', 'is_active',)


class NatureRefusalGSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatureRefusalG
        fields = ('reason_refusal', 'text_ref',)


class ClientGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientG
        fields = ('client', 'text_cl',)


class SersviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sersvice
        fields = ('service_company', 'text_s',)


class VidTOGSerializer(serializers.ModelSerializer):
    class Meta:
        model = VidTOG
        fields = ('vid_TO', 'text_v',)


class TOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TO
        fields = ('id_t', 'vid_TO', 'mtbf', 'num_order', 'date_order', 'service_TO', 'mashins_TO',)
