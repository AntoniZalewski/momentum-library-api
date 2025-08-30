from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone
from .models import Book
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = (
        'title', 
        'author', 
        'serial_number', 
        'display_is_borrowed',
        'borrowed_date', 
        'borrower_id',
        'actions_column'
    )
    list_filter = ('is_borrowed',)
    search_fields = ('title', 'author', 'serial_number')
    list_editable = ('borrowed_date', 'borrower_id') # POPRAWKA TUTAJ
    actions = ['mark_as_borrowed', 'mark_as_returned']

    def display_is_borrowed(self, obj):
        if obj.is_borrowed:
            return format_html('<span style="color: red;">&#10008; Wypożyczona</span>')
        else:
            return format_html('<span style="color: green;">&#10004; Dostępna</span>')
    display_is_borrowed.short_description = "Status"
    display_is_borrowed.admin_order_field = 'is_borrowed'

    def get_readonly_fields(self, request, obj=None):
        if obj and not obj.is_borrowed:
            return ('borrowed_date', 'borrower_id')
        return super().get_readonly_fields(request, obj)

    def actions_column(self, obj):
        edit_url = reverse('admin:library_book_change', args=[obj.pk])
        delete_url = reverse('admin:library_book_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" class="btn btn-sm btn-primary">Edytuj</a>&nbsp;'
            '<a href="{}" class="btn btn-sm btn-danger">Usuń</a>',
            edit_url,
            delete_url
        )
    actions_column.short_description = "Akcje"

    def mark_as_borrowed(self, request, queryset):
        queryset.update(is_borrowed=True, borrowed_date=timezone.now())
    mark_as_borrowed.short_description = "Oznacz wybrane jako wypożyczone"

    def mark_as_returned(self, request, queryset):
        queryset.update(is_borrowed=False, borrowed_date=None, borrower_id=None)
    mark_as_returned.short_description = "Oznacz wybrane jako zwrócone (zwróć do biblioteki)"