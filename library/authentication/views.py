from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserDetailSerializer, CustomUserListSerializer, CustomUserAdminDetailSerializer, CustomUserOrderDetailSerializer
from .permissions import IsOwnerOrReadOnly, AdminOnly, SelfOnlyOrder
from rest_framework.permissions import IsAuthenticated
from functools import partial
from rest_framework import status
from rest_framework.response import Response
from book.models import Book
from datetime import timedelta
from django.utils import timezone


class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserDetailSerializer


class CustomUserAdminCreateView(generics.CreateAPIView):
    serializer_class = CustomUserAdminDetailSerializer
    permission_classes = (IsAuthenticated,partial(AdminOnly, ['GET', "POST"]),)


class CustomUserListView(generics.ListAPIView):
    serializer_class = CustomUserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, partial(AdminOnly, ['GET']),)


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)


class CustomUserOrderCreateView(generics.CreateAPIView):
    serializer_class = CustomUserOrderDetailSerializer
    permission_classes = (IsAuthenticated, partial(
        SelfOnlyOrder, ['GET', 'POST']),)

    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=CustomUser.objects.get(
            pk=self.kwargs['pk']), plated_end_at=timezone.now() + timedelta(days=15))

        book = Book.objects.get(id=request.data['book'])
        book.count -= 1
        book.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
