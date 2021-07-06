import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class Habit(models.Model):
    """書籍"""
    name = models.CharField('習慣', max_length=255)
    date = models.DateTimeField('日付', default=timezone.now)
    achieve_day = models.IntegerField('達成日数', default=0)
    start_time = models.TimeField('開始時間', default=datetime.datetime.now())
    end_time = models.TimeField('終了時間', default=datetime.datetime.now())
    finish_judge = models.BooleanField('達成', default=False)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """メモ"""
    habit = models.ForeignKey(Habit, verbose_name='習慣', related_name='impressions',null=True, on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)
    quantity = models.IntegerField('作業時間', blank=True, default=0)
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.comment


