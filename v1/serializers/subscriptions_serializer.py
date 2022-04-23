from rest_framework import serializers
from v1.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    """Serializer for Subscription model."""
    address = serializers.EmailField(max_length=254)
    location = serializers.CharField(max_length=254)
    observer = serializers.JSONField()

    class Meta:
        """Meta class."""

        model = Subscriptions
        fields = "__all__"