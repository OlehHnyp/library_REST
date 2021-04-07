from django.urls import path, include
from .views import OrderListView, OrderDetailView


app_name = 'order'
urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view()),
]
