from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/<int:pk>/', include(router.urls)),
]
