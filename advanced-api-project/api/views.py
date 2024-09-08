from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public read access

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authentication required for creation

    def perform_create(self, serializer):
        # saving the instance
        serializer.save()

    def create(self, request, *args, **kwargs):
        # Customize the response or handle exceptions
        response = super().create(request, *args, **kwargs)
        return response

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public read access

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authentication required for updates

    def perform_update(self, serializer):
        # Add custom behavior before saving the updated instance, if needed
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Customize the response or handle exceptions
        response = super().update(request, *args, **kwargs)
        return response

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authentication required for deletion