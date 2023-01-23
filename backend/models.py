from django.db import models


class Mashins(models.Model):
    zav_nom_mashins = models.CharField(primary_key=True, null=False)
    mod_mashins = models.CharField()
    mod_motor = models.CharField()
    zav_nom_motor = models.CharField()
    mod_transmission = models.CharField()
    zav_nom_transmission = models.CharField()
    mod_drive_bridge = models.CharField()
    zav_nom_drive_bridge = models.CharField()
    mod_controll_bridge = models.CharField()
    zav_nom_controll_bridge = models.CharField()
    dogovor = models.CharField()
    date_shipment = models.DateField()
    consignee = models.CharField()
    equipment = models.TextField()
    client_ = models.CharField()
    service_company = models.CharField


class TO(models.Model):
    vid_TO = models.CharField()
    date_TO = models.DateField()
    mtbf = models.IntegerField()
    nom_order = models.CharField()
    date_order = models.DateField()
    service_TO = models.CharField()
    mashins_TO = models.CharField()


class Complaint(models.Model):
    date_refusal = models.DateField()
    mtdf_c = models.CharField()
    reason_refusal = models.CharField()
    recovery_method = models.CharField()
    spare = models.TextField()
    date_recovery = models.DateField()
    downtime = models.IntegerField()
    mashins_c = models.CharField()


class Guide(models.Model):
    mod_equipment_g = models.ForeignKey()
    mod_motor_g = models.ForeignKey()

