from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'get_books', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(models.Genre)


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'initials')


# admin.site.register(models.Book)
# admin.site.register(models.BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance


# Register the Admin classes for Book using the decorator

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('title', 'author', 'genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'imprint', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
