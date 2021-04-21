from django.contrib import admin
from .models import *


class PollsAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'end_date')
    list_filter = ('create_date', 'end_date')

    ordering = ['create_date']
    search_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['create_date']
        else:
            return []


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'poll')
    list_filter = ('poll__name', 'type')

    ordering = ['text']
    search_fields = ['text']


admin.site.register(Polls, PollsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
