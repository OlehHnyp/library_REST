from django.urls import path, include
from .views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/<int:pk>/', include(router.urls)),
]
