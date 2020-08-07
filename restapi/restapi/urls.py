from django.contrib import admin
from django.urls import path, include
from student.views import AuthorView, BookView, PublisherView

from rest_framework.routers import DefaultRouter

author_router = DefaultRouter()
author_router.register('author', AuthorView)

pub_router = DefaultRouter()
pub_router.register('pub', PublisherView)

book_router = DefaultRouter()
book_router.register('book', BookView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pub_router.urls)),
    path('', include(book_router.urls)),
    path ('', include(author_router.urls)),

]