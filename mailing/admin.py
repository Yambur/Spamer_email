from django.contrib import admin

from mailing.models import MailingSettings, MailingMessage, MailingLog


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display =('pk', 'start_date', 'finish_date', 'period', 'status')


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body')
    list_filter = ('mailing',)

@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_play = ('last_date_time', 'status', 'server_response',)
    list_filter = ('mailing',)