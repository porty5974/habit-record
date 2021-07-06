import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from workrecord.models import Habit, Impression
from workrecord.forms import HabitForm, ImpressionForm
from django.utils.timezone import utc



def habit_list(request):
    """書籍の一覧"""
    # return HttpResponse('書籍の一覧')
    habits = Habit.objects.all().order_by('id')
    context = {
        'habits' : habits,
    }

    return render(request,
                  'workrecord/habit_list.html',     # 使用するテンプレート
                  context)         # テンプレートに渡すデータ

def habit_edit(request, habit_id=None):
    """書籍の編集"""
    # return HttpResponse('書籍の編集')
    if habit_id:   # habit_id が指定されている (修正時)
        habit = get_object_or_404(Habit, pk=habit_id)
    else:         # habit_id が指定されていない (追加時)
        habit = Habit()

    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            habit = form.save(commit=False)
            habit.save()
            return redirect('workrecord:habit_list')
    else:    # GET の時
        form = HabitForm(instance=habit)  # book インスタンスからフォームを作成

    return render(request, 'workrecord/habit_edit.html', dict(form=form, habit_id=habit_id))


def habit_del(request, habit_id):
    # return HttpResponse('タスクの削除')
    habit = get_object_or_404(Habit, pk=habit_id)
    habit.delete()
    return redirect('workrecord:habit_list')


class ImpressionList(ListView):
    """感想の一覧"""
    context_object_name = 'impressions'
    template_name = 'workrecord/impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        habit = get_object_or_404(Habit, pk=kwargs['habit_id'])  # 親の書籍を読む
        impressions = habit.impressions.all().order_by('id')  # 書籍の子供の、感想を読む
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, habit=habit)
        return self.render_to_response(context)


def impression_edit(request, habit_id, impression_id=None):
    """感想の編集"""
    habit = get_object_or_404(Habit, pk=habit_id)  # 親の書籍を読む
    if impression_id:  # impression_id が指定されている (修正時)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:  # impression_id が指定されていない (追加時)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            impression = form.save(commit=False)
            impression.habit = habit  # この感想の、親の習慣をセット
            impression.save()
            return redirect('workrecord:impression_list', habit_id=habit_id)
    else:  # GET の時
        form = ImpressionForm(instance=impression)  # impression インスタンスからフォームを作成

    return render(request,
                  'workrecord/impression_edit.html',
                  dict(form=form, habit_id=habit_id, impression_id=impression_id))


def impression_del(request, habit_id, impression_id):
    """感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('workrecord:impression_list', habit_id=habit_id)