# Generated by Django 3.0.2 on 2021-04-16 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecord', '0007_auto_20210415_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2021, 4, 17, 2, 21, 51, 63379), verbose_name='終了時間'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 4, 17, 2, 21, 51, 63379), verbose_name='開始時間'),
        ),
    ]
