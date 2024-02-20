from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

class MailingSettings(models.Model):
    start_date = models.DateTimeField(default=timezone.now, verbose_name="начало рассылки")
    finish_date = models.DateTimeField(verbose_name="конец рассылки")
    period = models.CharField(max_length=300, choices=(
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ))
    status = models.CharField(max_length=300, choices=(
        ('completed', 'Завершено'),
        ('created', 'Создано'),
        ('launched', 'Запущенно'),
    ))

    def __str__(self):
        return f'{self.start_date} - {self.finish_date}'

    class Meta:
        verbose_name = "настройка"
        verbose_name_plural = "настройки"



class MailingMessage(models.Model):
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name="лог рассылки")
    theme = models.CharField(max_length=100, verbose_name="тема сообщения")
    body = models.TextField(verbose_name="сообщение")

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'{self.theme}, {self.body}'


class MailingLog(models.Model):
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name="лог рассылки")
    last_date_time = models.DateTimeField(auto_now_add=True, verbose_name="последняя отправка")
    status = models.CharField(max_length=300, choices=(
        ('complete', 'Успешно'),
        ('fail', 'Провал'),
    ))
    server_response = models.TextField(verbose_name="ответ почтового сервиса", **NULLABLE)

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

