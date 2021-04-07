from django.urls import path, include
from .views import BookListView, BookCreateView, BookDetailView


app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(),),
    path('create/', BookCreateView.as_view(),),
    path('<int:pk>/', BookDetailView.as_view(),),
]
