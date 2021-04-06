from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer
from . models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
