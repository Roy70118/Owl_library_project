from django.db import models

# # Create your models here.
class Book(models.Model):
     Book_Types=(
          ('paperback', 'Paperback'),
          ('hardcover', 'Hardcover'),
          ('handmade','Handmade'),
     
     )

     title= models.CharField(max_length=100)
     author= models.CharField(max_length=100)
     book_type= models.CharField(max_length=20,choices=Book_Types)
     owl_id= models.CharField(max_length=50, unique=True)
     available= models.BooleanField(default=True)
     borrowed_at= models.DateField(null=True, blank=True)
     returned_at= models.DateField(null=True, blank=True)
     borrower_email= models.EmailField(null=True, blank=True)


