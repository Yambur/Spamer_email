from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name ='mailing/main.html'
    extra_context ={
        'title': 'Рассылки - Главная'
    }

