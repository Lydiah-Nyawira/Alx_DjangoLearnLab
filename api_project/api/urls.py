from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]