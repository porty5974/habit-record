from django.contrib import admin
from workrecord.models import Habit, Impression, Achieve

# admin.site.register(Book)
# admin.site.register(Impression)
admin.site.register(Achieve)

class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'date', 'start_time', 'end_time' )  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Habit, HabitAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('habit',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）


admin.site.register(Impression, ImpressionAdmin)
