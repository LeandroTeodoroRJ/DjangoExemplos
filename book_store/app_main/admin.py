from django.contrib import admin
from .models import Book, Author, Address


class BookAdmin(admin.ModelAdmin):  #Some configurations for admin site
    #readonly_fields = ("slug",)  #If you use prepopulated_fields you must disable readonly
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "is_bestselling",)
    list_display = ("title", "author",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)

class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city",)


# Register your models here.
#admin.site.register(Book)  #if you don't want to use ModelAdmin class to configure
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
