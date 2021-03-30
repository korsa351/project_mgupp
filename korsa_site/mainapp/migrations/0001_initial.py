# Generated by Django 3.1.7 on 2021-03-29 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_Details', models.TextField()),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Gymnasts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gymnast_Name', models.CharField(max_length=50)),
                ('Gymnast_Hometown', models.CharField(max_length=50)),
                ('Other_Gymnast_Details', models.TextField()),
            ],
            options={
                'verbose_name': 'Гимнаст',
                'verbose_name_plural': 'Гимнасты',
            },
        ),
        migrations.CreateModel(
            name='Meets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meet_Date', models.DateField()),
                ('Meet_Location', models.TextField()),
                ('Meet_Score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Other_Details', models.TextField()),
            ],
            options={
                'verbose_name': 'Встреча',
                'verbose_name_plural': 'Встречи',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University_Name', models.TextField()),
                ('Other_Details', models.TextField()),
            ],
            options={
                'verbose_name': 'Университет',
                'verbose_name_plural': 'Университеты',
            },
        ),
        migrations.CreateModel(
            name='University_Meet_Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Overall_University_Scores', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Meet_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.meets')),
                ('University_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.university')),
            ],
            options={
                'verbose_name': 'Университетская встреча',
                'verbose_name_plural': 'Университетские встречи',
            },
        ),
        migrations.CreateModel(
            name='Members_Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.addresses')),
                ('Gymnasts_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.gymnasts')),
            ],
            options={
                'verbose_name': 'Адрес Участника',
                'verbose_name_plural': 'Адреса Участников',
            },
        ),
        migrations.AddField(
            model_name='gymnasts',
            name='University_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.university'),
        ),
    ]
