from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields = ['title', 'published_data']
    pagination_class = None

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookBySlugAPIView(APIView):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)