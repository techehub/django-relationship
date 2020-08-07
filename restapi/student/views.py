
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializer import BookSerializer, PublisherSerializer,  AuthorSerializer
from .models import Book, Author , Publisher
from rest_framework.response import  Response


class AuthorView (ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PublisherView (ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class BookView (ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()