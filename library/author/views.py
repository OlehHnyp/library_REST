from django.shortcuts import render
from rest_framework import generics
from .models import Author
from .serializers import AuthorDetailSerializer
from authentication.permissions import AdminOnly
from rest_framework.permissions import IsAuthenticated
from functools import partial


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer
    permission_classes = (IsAuthenticated, partial(
        AdminOnly, ['GET', "POST"]),)


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticated,
                          partial(AdminOnly, ['GET', "POST", 'PUT', 'DELETE']),)
