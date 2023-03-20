from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportMixin

from users.models import CustomUser

from .models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                     ModControllBridgeG, RecoveryMethodG, Complaint, NatureRefusalG,
                     ClientG, Sersvice, VidTOG, TO, FailureNodeReference)


# Мотор
class MotorResource(resources.ModelResource):
    class Meta:
        model = ModMotorG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(ModMotorG)
class MotorAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MotorResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Ведущий мост
class DriveBridgeResource(resources.ModelResource):
    class Meta:
        model = ModDriveBridgeG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(ModDriveBridgeG)
class DriveBridgeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DriveBridgeResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Трансмиссия
class TransmissionResource(resources.ModelResource):
    class Meta:
        model = ModTransmissionG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(ModTransmissionG)
class MotorAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TransmissionResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Модель машины
class ModelMashinsResource(resources.ModelResource):
    class Meta:
        model = ModMashinsG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(ModMashinsG)
class ModelMashinsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ModelMashinsResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Модель управляемого мост
class ControllBridgeResource(resources.ModelResource):
    class Meta:
        model = ModControllBridgeG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(ModControllBridgeG)
class ControllBridgeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ControllBridgeResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Узел восстановления
class FailureNodeReferenceResource(resources.ModelResource):
    class Meta:
        model = FailureNodeReference
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(FailureNodeReference)
class FailureNodeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FailureNodeReferenceResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Метод восстановления
class RecoveryMethodResource(resources.ModelResource):
    class Meta:
        model = RecoveryMethodG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(RecoveryMethodG)
class RecoveryMethodAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RecoveryMethodResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Вид ТО
class VidTOResource(resources.ModelResource):
    class Meta:
        model = VidTOG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(VidTOG)
class VidTOAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = VidTOResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Характер отказа
class NatureRefusalResource(resources.ModelResource):
    class Meta:
        model = NatureRefusalG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(NatureRefusalG)
class NatureRefusalAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = NatureRefusalResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Машины
class MashinsResource(resources.ModelResource):
    class Meta:
        model = Mashins
        report_skipped = True
        fields = ('zav_nom_mashins',
                  'model_mashins',
                  'model_motor',
                  'zav_nom_motor',
                  'model_transmission',
                  'zav_nom_transmission',
                  'model_drive_bridge',
                  'zav_nom_drive_bridge',
                  'model_controll_bridge',
                  'zav_nom_controll_bridge',
                  'dogovor',
                  'date_shipment',
                  'consignee',
                  'delivery_address',
                  'equipment',
                  'client',
                  'service_company',
                  )


@admin.register(Mashins)
class MashinsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MashinsResource
    list_display = ('zav_nom_mashins',
                    'model_mashins',
                    'model_motor',
                    'model_transmission',
                    'model_drive_bridge',
                    'model_controll_bridge',
                    'date_shipment',
                    'equipment',
                    'client',
                    'service_company',
                    )
    filter = ('zav_nom_mashins',)


# ТО
class TOResource(resources.ModelResource):
    class Meta:
        model = TO
        report_skipped = True
        fields = ('id',
                  'vid_TO',
                  'date_TO',
                  'mtbf',
                  'num_order',
                  'date_order',
                  'service_TO',
                  'mashins_TO',
                  )


@admin.register(TO)
class TOAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TOResource
    list_display = ('mashins_TO',
                    'vid_TO',
                    'date_TO',
                    'mtbf',
                    'num_order',
                    'date_order',
                    'service_TO',
                    )
    filter = ('mashins_TO',)


# Рекламации
class ComplaintResource(resources.ModelResource):
    class Meta:
        model = Complaint
        report_skipped = True
        fields = ('id',
                  'mashins_c',
                  'date_refusal',
                  'mtdf_c',
                  'failure_node',
                  'reason_refusal',
                  'recovery_method',
                  'spare',
                  'date_recovery',
                  'downtime',
                  )


@admin.register(Complaint)
class ComplaintAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ComplaintResource
    list_display = ('id',
                    'mashins_c',
                    'date_refusal',
                    'mtdf_c',
                    'failure_node',
                    'reason_refusal',
                    'recovery_method',
                    'spare',
                    'date_recovery',
                    'downtime',
                    )
    filter = ('mashins_c',)


# Клиенты
class ClientResource(resources.ModelResource):
    class Meta:
        model = ClientG
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(ClientG)
class ClientAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ClientResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


# Сервисная организация
class SersviceResource(resources.ModelResource):
    class Meta:
        model = Sersvice
        report_skipped = True
        fields = ('id', 'name', 'description',)


@admin.register(Sersvice)
class SersviceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SersviceResource
    list_display = ('id', 'name', 'description',)
    filter = ('name',)
