from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserDetailSerializer, CustomUserListSerializer, CustomUserAdminDetailSerializer
from .permissions import IsOwnerOrReadOnly, AdminOnly
from rest_framework.permissions import IsAuthenticated
from functools import partial


class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserDetailSerializer


class CustomUserAdminCreateView(generics.CreateAPIView):
    serializer_class = CustomUserAdminDetailSerializer
    permission_classes = (partial(AdminOnly, ['GET', "POST"]),)


class CustomUserListView(generics.ListAPIView):
    serializer_class = CustomUserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (partial(AdminOnly, ['GET']),)


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
