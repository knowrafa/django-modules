from django.utils.deprecation import MiddlewareMixin
from management.log.tasks import registrar_log


class LogMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_response(self, request, response):
        registrar_log.apply_async(args=(request, response))
        return response
