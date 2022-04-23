
from rest_framework import mixins, viewsets
from v1.models import Alerts
from v1.serializers.alerts_serializer import AlertsSerializer

import logging


logger = logging.getLogger('dataminr')

class AlertsView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):

    serializer_class = AlertsSerializer
    queryset = Alerts.objects.all()
