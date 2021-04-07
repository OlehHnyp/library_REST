from django.urls import path, include
from .views import AuthorListView, AuthorCreateView, AuthorDetailView


app_name = 'author'

urlpatterns = [
    path('', AuthorListView.as_view(),),
    path('create/', AuthorCreateView.as_view(),),
    path('<int:pk>/', AuthorDetailView.as_view(),),
]
