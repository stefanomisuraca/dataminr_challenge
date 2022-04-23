
from rest_framework import viewsets
from v1.models import Subscriptions
from v1.serializers.subscriptions_serializer import SubscriptionsSerializer

import logging

logger = logging.getLogger('dataminr')

class SubscriptionsView(viewsets.ModelViewSet):

    serializer_class = SubscriptionsSerializer
    queryset = Subscriptions.objects.all()
