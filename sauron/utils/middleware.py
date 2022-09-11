from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AppendSlash(MiddlewareMixin):
    def process_request(self, request: WSGIRequest) -> HttpResponse:
        if not request.path.endswith("/"):
            return redirect(request.path + "/")

        return (
            self.get_response(request) if self.get_response else HttpResponse()
        )
