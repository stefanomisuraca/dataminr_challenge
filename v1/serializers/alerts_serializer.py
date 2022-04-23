from rest_framework import serializers
from v1.models import Alerts


class AlertsSerializer(serializers.ModelSerializer):
    """Serializer for Subscription model."""

    class Meta:
        """Meta class."""

        model = Alerts
        fields = "__all__"