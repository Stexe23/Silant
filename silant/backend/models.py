import datetime
from django.db import models
from users.models import CustomUser


# Справочник компаний
class Sersvice(models.Model):
    name = models.ForeignKey(CustomUser, related_name='service_company', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Справочник сервисных компаний'

    def __str__(self):
        return self.name


# Справочник по модели трансмиссии
class ModTransmissionG(models.Model):
    name = models.CharField('Модель трансмиссии', max_length=32, unique=True)
    description = models.TextField('Описание', max_length=256, null=False)

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Справочник моделей трансмиссии'

    def __str__(self):
        return self.name


# Справочник по модели машины
class ModMashinsG(models.Model):
    name = models.CharField('Модель машины', max_length=32, unique=True)
    description = models.TextField('Описание', max_length=256, null=False)

    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Справочник моделей машины'

    def __str__(self):
        return self.name


# Справочник по модели мотора
class ModMotorG(models.Model):
    name = models.CharField('Модель мотора', max_length=32, unique=True)
    description = models.TextField('Описание', max_length=256, null=False)

    class Meta:
        verbose_name = 'Модель мотора'
        verbose_name_plural = 'Справочник моделей мотора'

    def __str__(self):
        return self.name


# Справочник по модели ведущего моста
class ModDriveBridgeG(models.Model):
    name = models.CharField('Ведущий мост', max_length=32, unique=True)
    description = models.TextField('Описание', max_length=256, null=False)

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Справочник моделей ведущего моста'

    def __str__(self):
        return self.name


# Справочник по модели управляемого моста
class ModControllBridgeG(models.Model):
    name = models.CharField('Управляемый мост', max_length=32, unique=True)
    description = models.TextField('Описание', max_length=256, null=False)

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Справочник моделей управляемого моста'

    def __str__(self):
        return self.name


# Справочник по видам тех. обслуживания
class VidTOG(models.Model):
    name = models.CharField('Вид ТО', max_length=32, unique=True)
    description = models.TextField('Описание', max_length=256, null=False)

    class Meta:
        verbose_name = 'Вид технического обслуживания '
        verbose_name_plural = 'Справочник видов ТО'

    def __str__(self):
        return self.name


# Справочник по характерам отказа
class NatureRefusalG(models.Model):
    name = models.CharField('Характер отказа', max_length=50, unique=True)
    description = models.TextField('Описание', max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Справочник характеров отказа'

    def __str__(self):
        return self.reason_refusal


# Справочник по способам восстановления
class RecoveryMethodG(models.Model):
    recovery_method = models.CharField(max_length=64)
    text_rec = models.TextField(max_length=256)

    def __str__(self):
        return self.recovery_method


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
    vid_TO = models.ForeignKey(VidTOG, on_delete=models.CASCADE)  # Вид ТО
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
    reason_refusal = models.ForeignKey(NatureRefusalG, on_delete=models.CASCADE)  # Описание отказа
    recovery_method = models.ForeignKey(RecoveryMethodG, on_delete=models.CASCADE)  # Способ восстановления
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
