from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('books/', BookListApiView.as_view()),
    path('book/<int:book_id>/', BookDetailApiView.as_view())

]