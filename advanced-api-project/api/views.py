from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):
    """
    View to list all books.
    """
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookCreateView(APIView):
    """
    View to create a new book.
    """
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    """
    View to retrieve, update, or delete a specific book.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self.get_object(pk)
        if book is not None:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book is not None:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book is not None:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)