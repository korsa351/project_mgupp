# Generated by Django 3.1.7 on 2021-03-31 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210401_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymnasts',
            name='Gymnast_Address',
            field=models.ManyToManyField(through='mainapp.Addresses_Gymnasts', to='mainapp.Addresses'),
        ),
    ]