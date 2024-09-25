from django.contrib import admin

from app_01.models import Logg


@admin.register(Logg)
class LoggAdmin(admin.ModelAdmin):
    list_display = ["address_ip", "date", "time", "method", "answer","answer_size"]
    search_fields = ["address_ip", "date"]
    list_filter = ["date", "method", "answer"]
    fields = [
        'address_ip',
        'date',
        'time',
        'method',
        'answer',
        'answer_size'
        ]