
# from django.core.exceptions import ValidationError
# from datetime import datetime, timedelta
# from .models import Book

# def validate_popular_author_borrowing(author_name, user_email):
#     if author_name.startswith('J'):
#         borrowed_books = Book.objects.filter(borrower_email=user_email, author=author_name)
#         if borrowed_books.exists():
#             last_borrowed_date = borrowed_books.order_by('-borrowed_at').first().borrowed_at
#             if (datetime.now().date() - last_borrowed_date.date()).days <= 180:
#                 raise ValidationError("You can only borrow books from this author once every 6 months.")
