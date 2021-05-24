from django.conf.urls import url

from . import views
from .models import Book, Author

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(model=Book, template_name='books.html',
                                                context_object_name='books'), name='books'),
    url(r'^authors/', views.AuthorListView.as_view(model=Author, template_name='authors.html',
                                                   context_object_name='authors'), name='authors'),
]
