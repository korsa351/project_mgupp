# Generated by Django 3.1.7 on 2021-04-02 12:00

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gymnasts',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]