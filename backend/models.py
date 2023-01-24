from django.db import models


# Справочник компаний
class Sersvice(models.Model):
    service_company = models.CharField()
    text_s = models.TextField()


# Таблица по машине
class Mashins(models.Model):
    zav_nom_mashins = models.CharField(primary_key=True, null=False)
    model_mashins = models.CharField()
    model_motor = models.CharField()
    zav_nom_motor = models.CharField()
    model_transmission = models.CharField()
    zav_nom_transmission = models.CharField()
    model_drive_bridge = models.CharField()
    zav_nom_drive_bridge = models.CharField()
    model_controll_bridge = models.CharField()
    zav_nom_controll_bridge = models.CharField()
    dogovor = models.CharField()
    date_shipment = models.DateField()
    consignee = models.CharField()
    equipment = models.TextField()
    client_ = models.CharField()
    service_company = models.ForeignKey(Sersvice, on_delete=models.CASCADE)


# Таблица по тех. обслуживанию
class TO(models.Model):
    id_t = models.IntegerField(primary_key=True)
    vid_TO = models.CharField()
    date_TO = models.DateField()
    mtbf = models.IntegerField()
    num_order = models.CharField()
    date_order = models.DateField()
    service_TO = models.CharField()
    mashins_TO = models.CharField()


# Таблица рекламаций
class Complaint(models.Model):
    id_c = models.IntegerField(primary_key=True)
    date_refusal = models.DateField()
    mtdf_c = models.CharField()
    reason_refusal = models.CharField()
    recovery_method = models.CharField()
    spare = models.TextField()
    date_recovery = models.DateField()
    downtime = models.IntegerField()
    mashins_c = models.CharField()


# Справочники:
# Справочник по модели трансмиссии
class ModTransmissionG(models.Model):
    model_transmission = models.ForeignKey(Mashins, on_delete=models.CASCADE)
    text_t = models.TextField()


# Справочник по модели машины
class ModMashinsG(models.Model):
    model_mashins = models.ForeignKey(Mashins, on_delete=models.CASCADE)
    text_ma = models.TextField()


# Справочник по модели мотора
class ModMotorG(models.Model):
    model_motor = models.ForeignKey(Mashins, on_delete=models.CASCADE)
    text_mo = models.TextField()


# Справочник по модели ведущего моста
class ModDriveBridgeG(models.Model):
    model_drive_bridge = models.ForeignKey(Mashins, on_delete=models.CASCADE)
    text_db = models.TextField()


# Справочник по модели управляемого моста
class ModControllBridgeG(models.Model):
    model_controll_bridge = models.ForeignKey(Mashins, on_delete=models.CASCADE)
    text_cb = models.TextField()


# Справочник по видам тех. обслуживания
class VideTOG(models.Model):
    vid_TO = models.ForeignKey(TO, on_delete=models.CASCADE)
    text_v = models.TextField()


# Справочник по характерам отказа
class NatureRefusalG(models.Model):
    reason_refusal = models.ForeignKey(Complaint, on_delete=models.CASCADE)


# Справочник по способам восстановления
class RecoveryMethodG(models.Model):
    recovery_method = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    text_r = models.TextField()


# Связь таблиц машины, ТО и рекламаций
class MashinsTORef(models.Model):
    zav_nom_mashins = models.ForeignKey(Mashins, on_delete=models.CASCADE)
    id_t = models.ForeignKey(TO, on_delete=models.CASCADE)
    id_c = models.ForeignKey(Complaint, on_delete=models.CASCADE)
