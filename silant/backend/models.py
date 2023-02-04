import datetime
from django.db import models


client = 'CL'
service = 'SR'
manager = 'MG'

POSITIONS = [
    (client, 'Клиент'),
    (service, 'Сервис'),
    (manager, 'Менеджер')
]


# Класс пользователя
class UsersSilant(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Логин
    password = models.CharField(max_length=32)  # Пароль
    user_email = models.EmailField()
    name = models.CharField(max_length=128, blank=True)  # ФИО
    position = models.CharField(max_length=2, choices=POSITIONS, default=client)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __int__(self):
        return self.name


# Справочник компаний
class Sersvice(models.Model):
    service_company = models.CharField(max_length=128)
    text_s = models.TextField(max_length=256)

    def __str__(self):
        return self.service_company


# Справочник по модели трансмиссии
class ModTransmissionG(models.Model):
    model_transmission = models.CharField(max_length=32)
    text_t = models.TextField(max_length=256)

    def __str__(self):
        return self.model_transmission


# Справочник по модели машины
class ModMashinsG(models.Model):
    model_mashins = models.CharField(max_length=32)
    text_ma = models.TextField(max_length=256)

    def __str__(self):
        return self.model_mashins


# Справочник по модели мотора
class ModMotorG(models.Model):
    model_motor = models.CharField(max_length=32)
    text_mo = models.TextField(max_length=256)

    def __str__(self):
        return self.model_motor


# Справочник по модели ведущего моста
class ModDriveBridgeG(models.Model):
    model_drive_bridge = models.CharField(max_length=32)
    text_db = models.TextField(max_length=256)

    def __str__(self):
        return self.model_drive_bridge


# Справочник по модели управляемого моста
class ModControllBridgeG(models.Model):
    model_controll_bridge = models.CharField(max_length=32)
    text_cb = models.TextField(max_length=256)

    def __str__(self):
        return self.model_controll_bridge


# Справочник по видам тех. обслуживания
class VidTOG(models.Model):
    vid_TO = models.CharField(max_length=32)
    text_v = models.TextField(max_length=256)

    def __str__(self):
        return self.vid_TO


# Справочник по характерам отказа
class NatureRefusalG(models.Model):
    reason_refusal = models.CharField(max_length=32)
    text_ref = models.TextField(max_length=256)

    def __str__(self):
        return self.reason_refusal


# Справочник по способам восстановления
class RecoveryMethodG(models.Model):
    recovery_method = models.CharField(max_length=64)
    text_rec = models.TextField(max_length=256)

    def __str__(self):
        return self.recovery_method


# Связь таблиц машины, ТО и рекламаций
# class MashinsTORef(models.Model):
#    zav_nom_mashins = models.ForeignKey(Mashins, on_delete=models.CASCADE)
#    id_t = models.ForeignKey(TO, on_delete=models.CASCADE)
#    id_c = models.ForeignKey(Complaint, on_delete=models.CASCADE)


# Справочник клиентов
class ClientG(models.Model):
    client = models.CharField(max_length=128)
    text_cl = models.TextField(max_length=256)

    def __str__(self):
        return self.client


# Таблица по машине
class Mashins(models.Model):
    zav_nom_mashins = models.CharField(primary_key=True, null=False, max_length=32)
    model_mashins = models.ForeignKey(ModMashinsG, on_delete=models.CASCADE)
    model_motor = models.ForeignKey(ModMotorG, on_delete=models.CASCADE)
    zav_nom_motor = models.CharField(max_length=32)
    model_transmission = models.ForeignKey(ModTransmissionG, on_delete=models.CASCADE)
    zav_nom_transmission = models.CharField(max_length=32)
    model_drive_bridge = models.ForeignKey(ModDriveBridgeG, on_delete=models.CASCADE)
    zav_nom_drive_bridge = models.CharField(max_length=32)
    model_controll_bridge = models.ForeignKey(ModControllBridgeG, on_delete=models.CASCADE)
    zav_nom_controll_bridge = models.CharField(max_length=32)
    dogovor = models.CharField(max_length=32)  # Договор №
    date_shipment = models.DateField()  # Дата отгрузки
    consignee = models.CharField(max_length=128)   # Грузополучатель
    delivery_address = models.TextField(max_length=128)  # Адрес доставки(эксплуатации)
    equipment = models.TextField(max_length=256)  # Комплектация (доп. опция)
    client = models.ForeignKey(ClientG, on_delete=models.CASCADE)  # Клиент
    service_company = models.ForeignKey(Sersvice, on_delete=models.CASCADE)


# Таблица по тех. обслуживанию
class TO(models.Model):
    id_t = models.IntegerField(primary_key=True)
    vid_TO = models.CharField(max_length=32)  # Вид ТО
    date_TO = models.DateField()  # Дата проведения ТО
    mtbf = models.IntegerField()  # Наработка м/час
    num_order = models.CharField(max_length=32)
    date_order = models.DateField()  # Дата ордер-заказа
    service_TO = models.ForeignKey(Sersvice, on_delete=models.CASCADE)
    mashins_TO = models.ForeignKey(Mashins, on_delete=models.CASCADE)


# Таблица рекламаций
class Complaint(models.Model):
    id_c = models.IntegerField(primary_key=True)
    date_refusal = models.DateField()  # Дата отказа
    mtdf_c = models.IntegerField()  # Наработка м/час
    reason_refusal = models.ForeignKey(NatureRefusalG, on_delete=models.CASCADE)
    recovery_method = models.ForeignKey(RecoveryMethodG, on_delete=models.CASCADE)
    spare = models.TextField(max_length=256)  # Использованные запасные части
    date_recovery = models.DateField(blank=True)  # Дата восстановления
    downtime = models.IntegerField({date_recovery} - {date_refusal}, blank=True)  # Время простоя техники
    mashins_c = models.ForeignKey(Mashins, on_delete=models.CASCADE)

    def prostoy(self, date_refusal, date_recovery, downtime):
        date_refusal = self.date_refusal
        date_recovery = self.date_recovery
        d1 = datetime.date(f'{date_refusal}')
        d2 = datetime.date(f'{date_recovery}')
        du = d2 - d1
        self.downtime = du
        return self.downtime
