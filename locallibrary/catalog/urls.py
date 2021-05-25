from django.conf.urls import url
from django.urls import path

from . import views
from .models import Book, Author
from django.contrib import admin

app_name = "catalog"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'^admin/$', admin.site.urls, name='admin'),
    url(r'^books/$', views.BookListView.as_view(model=Book), name='books'),
    url(r'^authors/$', views.AuthorListView.as_view(model=Author, template_name='authors.html',
                                                    context_object_name='authors'), name='authors'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
