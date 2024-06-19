from rest_framework import serializers
from .models import Book
# from .validators import validate_popular_author_borrowing

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
#     def validate(self, data):
#         if not data['available']:
#             raise serializers.ValidationError("This book is not available for borrowing")
#         author_name= data['author']
#         user_email= self.context['request'].user.email
#         validate_popular_author_borrowing(author_name, user_email) 

#         return data 

    
     

