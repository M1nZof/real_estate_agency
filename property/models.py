from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField(
        'Новое здание?',
        null=True,
        blank=True,
        db_index=True)

    likes = models.ManyToManyField(User, related_name='liked_flats', null=True, blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Grievance(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='grievances',
        related_query_name='grievance'
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        related_name='grievances',
        related_query_name='grievance',
    )
    text = models.TextField('Текст жалобы', null=True)

    def __str__(self):
        return f'Жалоба от {self.user} на квартиру {self.flat}'


class Owner(models.Model):
    fullname = models.CharField('ФИО владельца', db_index=True, max_length=200)
    phonenumber = models.CharField('Номер владельца', max_length=20, db_index=True)
    pure_phone = PhoneNumberField('Нормализованный номер владельца', null=True, blank=True, db_index=True)
    flat = models.ManyToManyField(
        Flat,
        related_name='owners',
        related_query_name='owner',
        verbose_name='Квартиры в собственности',
        db_index=True,
    )

    def __str__(self):
        return f'{self.fullname} | {self.pure_phone}'
