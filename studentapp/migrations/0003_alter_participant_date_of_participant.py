# Generated by Django 3.2.10 on 2022-03-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_auto_20220309_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='date_of_participant',
            field=models.DateField(verbose_name='Дата участие'),
        ),
    ]
