from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from .permissions import IsOwnerOrReadOnly, AdminOnly
from order.models import Order
from datetime import timedelta
from django.utils import timezone


class CustomUserAdminDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.middle_name = validated_data['middle_name']
        instance.last_name = validated_data['last_name']
        instance.role = validated_data['role']
        instance.is_active = validated_data['is_active']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class CustomUserDetailSerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(default=0)
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.middle_name = validated_data['middle_name']
        instance.last_name = validated_data['last_name']
        instance.is_active = validated_data['is_active']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserOrderDetailSerializer(serializers.ModelSerializer):
    end_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        read_only_fields = ('user', 'plated_end_at')
        fields = ('__all__')
