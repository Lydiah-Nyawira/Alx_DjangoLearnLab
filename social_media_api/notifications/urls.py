from django.urls import path
from .views import NotificationViewSet

urlpatterns = [
    path('', NotificationViewSet.as_view({'get': 'list'}), name='user-notifications'),  # URL for viewing notifications
]