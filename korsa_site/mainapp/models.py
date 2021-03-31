from django.db import models
from django.urls import reverse

#Start DB University Gymnastics


class Addresses(models.Model):
    Address_Details = models.TextField()

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"


class Meets(models.Model):
    Meet_Date = models.DateField()
    Meet_Location = models.TextField()
    Meet_Score = models.DecimalField(max_digits=5, decimal_places=2)
    Other_Details = models.TextField(blank=True)

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"


class University(models.Model):
    University_Name = models.TextField()
    Other_Details = models.TextField(blank=True)

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"


class University_Meet_Participation(models.Model):
    University_ID = models.ForeignKey(University, on_delete=models.CASCADE)
    Meet_ID = models.ForeignKey(Meets, on_delete=models.CASCADE)
    Overall_University_Scores = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta: 
        verbose_name = "Университетская встреча"
        verbose_name_plural = "Университетские встречи" 


class Gymnasts(models.Model):
    Gymnast_Name = models.CharField(max_length=50)
    Gymnast_Hometown = models.CharField(max_length=50)
    Other_Gymnast_Details = models.TextField(blank=True)
    University_ID = models.ForeignKey(University, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Гимнаст"
        verbose_name_plural = "Гимнасты"


class Members_Addresses(models.Model):
    Gymnasts_ID = models.ForeignKey(Gymnasts, on_delete=models.CASCADE)
    Address_ID = models.ForeignKey(Addresses, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = "Адрес Участника"
        verbose_name_plural = "Адреса Участников"