from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, BookBySlugAPIView


urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('book/<slug:slug>/', BookBySlugAPIView.as_view(), name='book-by-slug'),
]