from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MainView

app_name = MailingConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]