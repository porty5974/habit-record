from django.forms import ModelForm
from workrecord.models import Habit, Impression


class HabitForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Habit
        fields = ('name', 'quantity', 'date','start_time', 'end_time',)


class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )
