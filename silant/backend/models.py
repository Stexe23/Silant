import datetime
from django.db import models

from users.models import CustomUser


# Справочник компаний
class Sersvice(models.Model):
    name = models.ForeignKey(CustomUser, verbose_name='Сервисная компания',
                             on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Справочник сервисных компаний'

    def __str__(self):
        return f'{self.name}'


# Справочник по модели трансмиссии
class ModTransmissionG(models.Model):
    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Справочник моделей трансмиссии'

    name = models.CharField('Модель трансмиссии', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'


# Справочник по модели машины
class ModMashinsG(models.Model):
    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Справочник моделей машины'

    name = models.CharField('Модель машины', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'


# Справочник по модели мотора
class ModMotorG(models.Model):
    class Meta:
        verbose_name = 'Модель мотора'
        verbose_name_plural = 'Справочник моделей мотора'

    name = models.CharField('Модель мотора', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'


# Справочник по модели ведущего моста
class ModDriveBridgeG(models.Model):
    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Справочник моделей ведущего моста'

    name = models.CharField('Ведущий мост', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# Справочник по модели управляемого моста
class ModControllBridgeG(models.Model):
    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Справочник моделей управляемого моста'

    name = models.CharField('Управляемый мост', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# Справочник по видам тех. обслуживания
class VidTOG(models.Model):
    class Meta:
        verbose_name = 'Вид технического обслуживания '
        verbose_name_plural = 'Справочник видов ТО'

    name = models.CharField('Вид ТО', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# Справочник по характерам отказа
class NatureRefusalG(models.Model):
    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Справочник характеров отказа'

    name = models.CharField('Характер отказа', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# Справочник по способам восстановления
class RecoveryMethodG(models.Model):
    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Справочник способов восстановления'
    
    name = models.CharField('Способ восстановления', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# Справочник клиентов
class ClientG(models.Model):

    name = models.ForeignKey(CustomUser, verbose_name='Клиент', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиент'

    def __str__(self):
        return f'{self.name}'


# Справочник узлов отказа 
class FailureNodeReference(models.Model):
    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Справочник узлов отказа'

    name = models.CharField('Наименование узла', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# Таблица по машине
class Mashins(models.Model):
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    zav_nom_mashins = models.CharField('Зав. № машины', primary_key=True, null=False, max_length=32, unique=True)
    model_mashins = models.ForeignKey(ModMashinsG, verbose_name='Модель машины', on_delete=models.CASCADE,
                                      related_name='model_mashins')

    model_motor = models.ForeignKey(ModMotorG, verbose_name='Модель двигателя', on_delete=models.CASCADE,
                                    related_name='model_motor')

    zav_nom_motor = models.CharField('Зав. № двигателя', max_length=32, blank=True, null=True)
    model_transmission = models.ForeignKey(ModTransmissionG, verbose_name='Модель трансмиссии',
                                           on_delete=models.CASCADE, related_name='model_transmission',
                                           blank=True, null=True)

    zav_nom_transmission = models.CharField('Зав. № трансмиссии', max_length=32, unique=True, blank=True, null=True)
    model_drive_bridge = models.ForeignKey(ModDriveBridgeG, verbose_name='Модель ведущего моста',
                                           on_delete=models.CASCADE, related_name='model_drive_bridgeclear',
                                           blank=True, null=True)

    zav_nom_drive_bridge = models.CharField('Зав. № ведущего моста', max_length=32, blank=True, null=True)
    model_controll_bridge = models.ForeignKey(ModControllBridgeG, verbose_name='Модель управляемого моста',
                                              on_delete=models.CASCADE, related_name='model_controll_bridge',
                                              blank=True, null=True)

    zav_nom_controll_bridge = models.CharField('Зав. № управляемого моста', max_length=100, blank=True, null=True)
    dogovor = models.CharField('Договор поставки №, дата', max_length=250, blank=True, null=True)  
    date_shipment = models.DateField('Дата отгрузки с завода', blank=True, null=True)  
    consignee = models.CharField('Грузополучатель (конечный потребитель)', max_length=250, blank=True, null=True)
    delivery_address = models.TextField('Адрес поставки (эксплуатации)', max_length=250, blank=True, null=True) 
    equipment = models.TextField('Комплектация (доп. опции)', max_length=250, blank=True, null=True)  
    client = models.ForeignKey(ClientG, verbose_name='Клиент', on_delete=models.CASCADE,
                               related_name='client', blank=True, null=True)
    service_company = models.ForeignKey(Sersvice, verbose_name='Сервисная компания', on_delete=models.CASCADE,
                                        related_name='service_company', blank=True, null=True)
      
    def __str__(self) -> str:
        return f'{self.zav_nom_mashins}: {self.model_mashins}'


# Таблица по тех. обслуживанию
class TO(models.Model):
    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'

    vid_TO = models.ForeignKey(VidTOG, verbose_name='Вид технического обслуживания', on_delete=models.CASCADE,
                               related_name='vid_TO')  # Вид ТО
    date_TO = models.DateField('Дата проведения ТО')
    mtbf = models.DecimalField('Наработка, м/час', max_digits=10, decimal_places=0)
    num_order = models.CharField('№ заказ-наряда', max_length=32, unique=True)
    date_order = models.DateField('Дата заказ-наряда')

    service_TO = models.ForeignKey(Sersvice, verbose_name='Сервисная компания', on_delete=models.CASCADE)
    mashins_TO = models.ForeignKey(Mashins, verbose_name='Машина', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.mashins_TO}: {self.vid_TO}'


# Таблица рекламаций
class Complaint(models.Model):
    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
    
    mashins_c = models.ForeignKey(Mashins, verbose_name='Машина', on_delete=models.CASCADE)
    date_refusal = models.DateField('Дата отказа', null=True, blank=True)
    mtdf_c = models.DecimalField('Наработка, м/час', max_digits=10, decimal_places=0)
    failure_node = models.ForeignKey(FailureNodeReference, verbose_name='Узел отказа',
                                     on_delete=models.CASCADE, related_name='failure_node')

    reason_refusal = models.ForeignKey(NatureRefusalG, verbose_name='Описание отказа',
                                       on_delete=models.CASCADE, related_name='reason_refusal')

    recovery_method = models.ForeignKey(RecoveryMethodG, verbose_name='Способ восстановления',
                                        on_delete=models.CASCADE, related_name='recovery_method',)
    spare = models.TextField('Используемые запасные части', max_length=1000, blank=True, null=True) 
    date_recovery = models.DateField('Дата восстановления', blank=True, null=True)
    downtime = models.IntegerField('Время простоя техники (дней)', default=0)

    def downtime(self):
        deltatime = self.date_recovery - self.date_refusal
        return deltatime.days

    def __str__(self):
        return f'{self.mashins_c} {self.reason_refusal}: {self.date_refusal}/{self.date_recovery}'
    