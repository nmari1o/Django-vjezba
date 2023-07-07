from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    # Add your view logic here
    return HttpResponse("This is my view!")


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *

class BookListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        books = Book.objects.filter()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookDetailApiView(APIView):
    def get_object(self,book_id):
        try:
            return Book.objects.get(id=book_id)        
        except Book.DoesNotExist:
            return None    

    def get(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)  

    '''
    # 2. Create
    def post(self, request, *args, **kwargs):
        
        data = {
            'title': request.data.get('title'), 
            'author': request.data.get('author'), 
            'description': request.data.get('description'),
            'publication_year':request.data.get('publication_year')
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
        