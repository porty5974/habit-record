from django.urls import path
from workrecord import views

app_name = 'workrecord'
urlpatterns = [
    # 書籍
    path('habit/', views.habit_list, name='habit_list'),   # 一覧
    path('habit/add/', views.habit_edit, name='habit_add'),  # 登録
    path('habit/mod/<int:habit_id>/', views.habit_edit, name='habit_mod'),  # 修正
    path('habit/del/<int:habit_id>/', views.habit_del, name='habit_del'),   # 削除

    # 感想
    path('impression/<int:habit_id>/', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    path('impression/add/<int:habit_id>/', views.impression_edit, name='impression_add'),        # 登録
    path('impression/mod/<int:habit_id>/<int:impression_id>/', views.impression_edit, name='impression_mod'),  # 修正
    path('impression/del/<int:habit_id>/<int:impression_id>/', views.impression_del, name='impression_del'),   # 削除


]