# Generated by Django 3.0.2 on 2021-04-12 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecord', '0003_auto_20210409_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2021, 4, 12, 21, 42, 24, 205820), verbose_name='終了時間'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 4, 12, 21, 42, 24, 205820), verbose_name='開始時間'),
        ),
    ]
