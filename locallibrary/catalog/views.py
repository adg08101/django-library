from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # El 'all()' esta implícito por defecto.
    num_genres = Genre.objects.count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_genres': num_genres},
    )


class AuthorListView(generic.ListView):

    def get_queryset(self):
        return Author.objects.all()


class BookListView(generic.ListView):

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['view'] = 'Books'
        return context


class BookDetailView(generic.DetailView):
    model = Book


"""def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book': book_id, }
    )"""
