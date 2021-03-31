# Generated by Django 3.1.7 on 2021-03-31 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210331_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymnasts',
            name='Gymnast_Photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='gymnasts',
            name='Gymnast_Address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.addresses', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='gymnasts_addresses',
            name='Address_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.addresses', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='gymnasts_addresses',
            name='Gymnasts_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.gymnasts', verbose_name='Гимнаст'),
        ),
        migrations.AlterField(
            model_name='meets',
            name='Meet_Date',
            field=models.DateField(verbose_name='Дата встречи'),
        ),
        migrations.AlterField(
            model_name='meets',
            name='Meet_Location',
            field=models.TextField(verbose_name='Место встречи'),
        ),
        migrations.AlterField(
            model_name='meets',
            name='Meet_Score',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговые баллы'),
        ),
        migrations.AlterField(
            model_name='meets',
            name='Other_Details',
            field=models.TextField(blank=True, verbose_name='Прочие детали встречи'),
        ),
        migrations.AlterField(
            model_name='university_meet_participation',
            name='Meet_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.meets', verbose_name='Встреча'),
        ),
        migrations.AlterField(
            model_name='university_meet_participation',
            name='Overall_University_Scores',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общие баллы Университета'),
        ),
        migrations.AlterField(
            model_name='university_meet_participation',
            name='University_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.university', verbose_name='Университет'),
        ),
    ]
