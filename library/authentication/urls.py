from django.urls import path, include
from .views import CustomUserCreateView, CustomUserListView, CustomUserDetailView, CustomUserAdminCreateView, CustomUserOrderCreateView


app_name = 'authentication'
urlpatterns = [
    path('create/', CustomUserCreateView.as_view()),
    path('create/admin/', CustomUserAdminCreateView.as_view()),
    path('', CustomUserListView.as_view()),
    path('<int:pk>/order/', CustomUserOrderCreateView.as_view()),
    path('<int:pk>/', CustomUserDetailView.as_view()),
]
