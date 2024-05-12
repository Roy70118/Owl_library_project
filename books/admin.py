from django.contrib import admin
from .models import Book

# # Register your models here.
# from .models import    author, book_type, owl_id, available, borrowed_at,returned_at,borrower_email

# admin.site.register( Title)
admin.site.register(Book)
