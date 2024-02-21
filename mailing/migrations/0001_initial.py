# Generated by Django 4.2 on 2024-02-20 05:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='начало рассылки')),
                ('finish_date', models.DateTimeField(verbose_name='конец рассылки')),
                ('period', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=300, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('completed', 'Завершено'), ('created', 'Создано'), ('launched', 'Запущенно')], max_length=300, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100, verbose_name='тема сообщения')),
                ('body', models.TextField(verbose_name='сообщение')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='лог рассылки')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_date_time', models.DateTimeField(auto_now_add=True, verbose_name='последняя отправка')),
                ('status', models.CharField(choices=[('complete', 'Успешно'), ('fail', 'Провал')], max_length=300)),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервиса')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='лог рассылки')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
            },
        ),
    ]
