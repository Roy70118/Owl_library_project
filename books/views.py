from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework. status import HTTP_400_BAD_REQUEST
from rest_framework. status import HTTP_200_OK
from rest_framework. status import HTTP_404_NOT_FOUND
from .models import Book
from .serializers import BookSerializer
from datetime import datetime, timedelta


# Create your views here.
class BookListView(APIView):
     def get(self,request):
          books= Book.objects.filter(available=True)
          serializer= BookSerializer(books, many=True)
          return Response(serializer.data)

class BookByAuthorView(APIView):
     def get(self,request,author_name):
          books= Book.objects.filter(author=author_name,available=True)
          serializer= BookSerializer(books,many=True)
          return Response(serializer.data)
          
class BookBorrowView(APIView):
     def put(self, request, owl_id):
          book= Book.objects.get(owl_id=owl_id)
          if  book.available:
               book.available=False
               book.borrower_email= request.data.get('borrower_email')
               book.borrowed_at= datetime.now().date()
               book.save()
               if request.data.get('borrower_email') is None:
                    return Response({'message': 'You are a new user, you can borrow the book'}, status= HTTP_200_OK)
               elif (datetime.now().date()- book.borrowed_at).days <=14:
                    return Response({'message': 'Book borrowed suceessfully'}, status= HTTP_200_OK)
               elif (datetime.now().date()- book.borrowed_at).days >90:
                    return Response({'message': 'You have borrowed this book within the last 3 months '}, status= HTTP_400_BAD_REQUEST)
               else:
                    return Response({'message':'you are returning the book within the 14 days'}, status=HTTP_200_OK)
          else:
               return Response({'message': 'Book is not available'}, status= HTTP_400_BAD_REQUEST)

class BookReturnView(APIView):
    def put(self, request, owl_id):
        book = Book.objects.get(owl_id=owl_id)
        if not book.available:
            book.available = True
            book.returned_at = datetime.now().date()
            book.borrower_email = None
            book.save()
            return Response({'message': 'Book returned successfully'}, status=HTTP_200_OK)
        else:
            return Response({'message': 'Book is already available'}, status=HTTP_400_BAD_REQUEST)



class BookBorrowabilityView(APIView):
    def get(self, request, owl_id):
        book = Book.objects.get(owl_id=owl_id)
        if book.available:
            return Response({'message': 'Book is available for borrowing.'})
        else:
            author_name = book.author
            borrower_email = book.borrower_email
            if author_name.startswith('J'):
                # Check if the borrower has borrowed a book from this author before
                borrowed_books = Book.objects.filter(borrower_email=borrower_email, author=author_name)
                if borrowed_books.exists():
                    # Get the date of the last borrowed book
                    last_borrowed_date = borrowed_books.order_by('-borrowed_at').first().borrowed_at
                    # Check if it's been at least 6 months since the last borrow
                    if (datetime.now().date() - last_borrowed_date).days >= 180:
                        return_date = book.borrowed_at + timedelta(days=14)
                        return Response({'message': f'Book will be available for borrowing on {return_date.strftime("%Y-%m-%d")}.'})
                    else:
                        return Response({'message': 'You can only borrow books from this author once every 6 months.'}, status=400)
                else:
                    return_date = book.borrowed_at + timedelta(days=14)
                    return Response({'message': f'Book will be available for borrowing on {return_date.strftime("%Y-%m-%d")}.'})
            else:
                return_date = book.borrowed_at + timedelta(days=14)
                return Response({'message': f'Book will be available for borrowing on {return_date.strftime("%Y-%m-%d")}.'})

      

               
          