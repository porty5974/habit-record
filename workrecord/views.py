import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from workrecord.models import Habit, Impression, Achieve
from workrecord.forms import HabitForm, ImpressionForm
from django.utils.timezone import utc



def book_list(request):
    """書籍の一覧"""
    # return HttpResponse('書籍の一覧')
    habits = Habit.objects.all()
    achieve_list = []
    for habit in habits:
        achieved = habit.achieve_set.filter(user=request.user)
        if achieved.exists():
            achieve_list.append(habit.id)

    context = {
        'habits' : habits,
        'achieve_list': achieve_list,
    }

    return render(request,
                  'workrecord/book_list.html',     # 使用するテンプレート
                  context)         # テンプレートに渡すデータ


def achieve(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    today = datetime.utcnow().replace(tzinfo=utc)
    next_day = today + datetime.timedelta(days=1)

    if next_day <= habit.date:
        habit.finish_judge = False

    if habit.finish_judge:
        habit.achieve_day -= 1
        habit.finish_judge = False
    else :
        habit.achieve_day += 1
        habit.finish_judge = True

    habit.date = today
    habit.save()
    return redirect('workrecord:book_list')


def book_edit(request, book_id=None):
    """書籍の編集"""
    # return HttpResponse('書籍の編集')
    if book_id:   # book_id が指定されている (修正時)
        habit = get_object_or_404(Habit, pk=book_id)
    else:         # book_id が指定されていない (追加時)
        habit = Habit()

    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            date = datetime.date.today()
            start_time = datetime.datetime.now()
            end_time = datetime
            habit = form.save(commit=False)
            habit.save()
            return redirect('workrecord:book_list')
    else:    # GET の時
        form = HabitForm(instance=habit)  # book インスタンスからフォームを作成

    return render(request, 'workrecord/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
    # return HttpResponse('書籍の削除')
    book = get_object_or_404(Habit, pk=book_id)
    book.delete()
    return redirect('workrecord:book_list')


class ImpressionList(ListView):
    """感想の一覧"""
    context_object_name = 'impressions'
    template_name = 'workrecord/impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        habit = get_object_or_404(Habit, pk=kwargs['book_id'])  # 親の書籍を読む
        impressions = habit.impressions.all().order_by('id')  # 書籍の子供の、感想を読む
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, habit=habit)
        return self.render_to_response(context)


def impression_edit(request, book_id, impression_id=None):
    """感想の編集"""
    book = get_object_or_404(Habit, pk=book_id)  # 親の書籍を読む
    if impression_id:  # impression_id が指定されている (修正時)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:  # impression_id が指定されていない (追加時)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            impression = form.save(commit=False)
            impression.habit = habit  # この感想の、親の書籍をセット
            impression.save()
            return redirect('workrecord:impression_list', book_id=book_id)
    else:  # GET の時
        form = ImpressionForm(instance=impression)  # impression インスタンスからフォームを作成

    return render(request,
                  'workrecord/impression_edit.html',
                  dict(form=form, book_id=book_id, impression_id=impression_id))


def impression_del(request, book_id, impression_id):
    """感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('workrecord:impression_list', book_id=book_id)