from django.http import JsonResponse
from django.views import View

import logging

logger = logging.getLogger('dataminr')


class TestView(View):

    def get(self, request):
        payload = {"message": "Hello World!"}
        return JsonResponse(payload)