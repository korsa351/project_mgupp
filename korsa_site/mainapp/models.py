from django.db import models
from django.db.models.fields import related
from django.urls import reverse

#Start DB University Gymnastics


class Meets(models.Model):
    Meet_Date = models.DateField('Дата встречи')
    Meet_Location = models.TextField('Место встречи')
    Meet_Score = models.DecimalField('Итоговые баллы', max_digits=10, decimal_places=2)
    Other_Details = models.TextField('Прочие детали встречи', blank=True)

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"

    def __str__(self) -> str:
        return self.Meet_Date


class University(models.Model):
    University_Name = models.CharField('Название Университета', max_length=100)
    Other_Details = models.TextField('Прочие детали', blank=True)

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"

    def __str__(self) -> str:
        return self.University_Name


class University_Meet_Participation(models.Model):
    University_ID = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name='Университет')
    Meet_ID = models.ForeignKey(Meets, on_delete=models.CASCADE, verbose_name='Встреча')
    Overall_University_Scores = models.DecimalField('Общие баллы Университета', max_digits=10, decimal_places=2)

    class Meta: 
        verbose_name = "Университетская встреча"
        verbose_name_plural = "Университетские встречи" 

    def __str__(self) -> str:
        return self.Meet_ID


class Addresses(models.Model):
    Address = models.CharField('Детальный адрес', max_length=100)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self) -> str:
        return self.Address


class Gymnasts(models.Model):
    Gymnast_Name = models.CharField('Имя гимнаста', max_length=50)
    Gymnast_Hometown = models.CharField('Родной город', max_length=50)
    Gymnast_Address = models.ManyToManyField(Addresses, through='Addresses_Gymnasts')
    Gymnast_Photo = models.ImageField('Фото', upload_to='photos')
    Other_Gymnast_Details = models.TextField('Детали', blank=True)
    University_ID = models.ForeignKey(University, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Гимнаст"
        verbose_name_plural = "Гимнасты"

    def __str__(self) -> str:
        return self.Gymnast_Name


class Addresses_Gymnasts(models.Model):
    Address_ID = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    Gymnast_ID = models.ForeignKey(Gymnasts, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = "Адрес Участника"
        verbose_name_plural = "Адреса Участников"

    #def __str__(self) -> str:
    #    return self.Gymnast_ID