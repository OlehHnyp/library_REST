from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderDetailSerializer
from .models import Order
from authentication.permissions import AdminOnly, IsOwnerOrReadOnly
from functools import partial
from django.utils import timezone
from book.models import Book
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta


class OrderListView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = (partial(AdminOnly, ['GET', ]),)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = (partial(AdminOnly, ['GET', "PUT"]),)

    def put(self, request,  pk):
        order = self.get_object()
        serializer = OrderDetailSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save(end_at=timezone.now())

        book = order.book
        book.count += 1
        book.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
