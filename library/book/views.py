from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookDetailSerializer
from authentication.permissions import AdminOnly
from rest_framework.permissions import IsAuthenticated
from functools import partial


class BookListView(generics.ListAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthenticated, partial(
        AdminOnly, ['GET', "POST"]),)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,
                          partial(AdminOnly, ['GET', "POST", 'PUT', 'DELETE']),)
