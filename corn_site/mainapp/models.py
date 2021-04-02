from typing import AbstractSet
from django.db import models
from django.urls import reverse


class RefEventTypes(models.Model):
    event_type_description = models.TextField('Описание', max_length=200)

    class Meta:
        verbose_name = 'Описание событий'
        verbose_name_plural = 'Описание событий'

    def __str__(self) -> str:
        return self.event_type_description



class Customers(models.Model):
    customer_phone = models.IntegerField('Номер Тел. Покупателя')
    customer_email = models.CharField('Почта', max_length=100)
    customer_addres = models.CharField('Адрес покупателя', max_length=100)
    customer_payment_method_details = models.CharField('Способ оплаты покупателя', null=True, max_length=100)

    class Meta:
        verbose_name = 'Покупатели'
        verbose_name_plural = 'Покупатели'

    def __str__(self) -> str:
        return self.customer_email



class Events(models.Model):
    event_type_code = models.ForeignKey(RefEventTypes, on_delete=models.CASCADE)
    event_name = models.CharField('Название события', max_length=100)
    event_start_date = models.DateField('Время начало события', null=True)
    event_end_date = models.DateField('Время конец события', null=True)

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'
    
    def __str__(self) -> str:
        return self.event_name



class EventRegistrations(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    event_datetime = models.DateField('Дата события', null=True)
    booking_made_date = models.DateField('Дата бронирования', null=True)
    booking_seat_count = models.IntegerField('Количество мест', null=True)

    class Meta:
        verbose_name = 'Регистрации на мероприятия'
        verbose_name_plural = 'Регистрации на мероприятия'

    def __str__(self) -> str:
        return f"{self.customer_id} {self.event_id}"


class EventReservartions(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    event_datetime = models.DateField('Дата события', null=True)
    booking_made_date = models.DateField('Дата бронирования', null=True)
    booking_seat_count = models.IntegerField('Количество мест', null=True)

    class Meta:
        verbose_name = 'Резервирование событий'
        verbose_name_plural = 'Резервирование событий'
    
    def __str__(self) -> str:
        return f"{self.customer_id} {self.event_id}"
