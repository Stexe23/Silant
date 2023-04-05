from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CLIENT = 'Клиент'
    SERVICE = 'Сервис'
    MANAGER = 'Менеджер'
    ADMIN = 'Админ'

    CHOICES = [
        (CLIENT, 'Клиент'),
        (SERVICE, 'Сервисная организация'),
        (MANAGER, 'Менеджер'),
        (ADMIN, 'Админ'),
    ]

    role = models.CharField('Роль пользователя', max_length=10, choices=CHOICES, default='Клиент')


    def __str__(self):
        return f'{self.first_name}'
    