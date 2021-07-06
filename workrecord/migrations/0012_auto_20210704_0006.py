# Generated by Django 3.2.5 on 2021-07-03 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecord', '0011_auto_20210623_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continuationdays',
            name='habit',
        ),
        migrations.RemoveField(
            model_name='continuationdays',
            name='user',
        ),
        migrations.AlterField(
            model_name='habit',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 4, 0, 6, 5, 79356), verbose_name='終了時間'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 4, 0, 6, 5, 79338), verbose_name='開始時間'),
        ),
        migrations.DeleteModel(
            name='achieve',
        ),
        migrations.DeleteModel(
            name='ContinuationDays',
        ),
    ]