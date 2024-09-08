from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class BookListView(generics.ListCreateAPIView):
    """
    GET: Retrieve a list of all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book by ID
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT: Update an existing book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

class CustomBookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =IsAuthenticated

    def perform_create(self, serializer):
        # Custom logic before saving a new book
        serializer.save()

class CustomBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =IsAuthenticated

    def perform_update(self, serializer):
        # Custom logic before updating a book
        serializer.save()