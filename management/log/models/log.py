from django.conf import settings
from django.db import models

from utils.mixins.models import SetUpModel


class LogModel(SetUpModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='logs',
                             null=True, blank=True)

    nome = models.CharField(max_length=255, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    response_status_code = models.CharField(max_length=50, blank=True, null=True)
    error_request_log = models.TextField(null=True, blank=True)
    request_body = models.TextField(null=True, blank=True)
    error_request_body = models.TextField(null=True, blank=True)

    error_acao_log = models.TextField(null=True, blank=True)

    user_agent = models.TextField(blank=True, null=True)

    dispositivo = models.CharField(max_length=255, blank=True, null=True)

    error_user_agent = models.TextField(blank=True, null=True)

    response_body = models.TextField(blank=True, null=True)

    error_response_log = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log'
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
