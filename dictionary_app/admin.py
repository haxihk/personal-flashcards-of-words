from django.contrib import admin
from .models import CustomUser, Word, UserActivityLog

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'language', 'created_at', 'updated_at')
    search_fields = ('word', 'meaning')

@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('action', 'timestamp')

# ثبت مدل کاربر سفارشی (در صورت استفاده از CustomUser)
admin.site.register(CustomUser)
