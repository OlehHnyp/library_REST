from rest_framework import serializers
from .models import Book
from author.serializers import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
