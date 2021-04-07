from rest_framework import serializers
from .models import Order


class OrderDetailSerializer(serializers.ModelSerializer):
    # plated_end_at = serializers.DateTimeField(read_only=True)
    # end_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        read_only_fields = ('user', 'plated_end_at', 'end_at', 'book')
        fields = '__all__'
