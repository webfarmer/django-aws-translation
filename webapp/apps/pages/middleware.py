from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse


class MaintenanceMiddleware:
    def __call__(self, request):
        response = self.get_response(request)
        if settings.SITE_DOWN and request.path != reverse("site-down"):
            return HttpResponseRedirect(reverse("site-down"))
        return response

    def __init__(self, get_response):
        self.get_response = get_response