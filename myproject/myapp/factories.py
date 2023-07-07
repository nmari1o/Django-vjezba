import factory
from faker import Faker
from .models import Book

fake = Faker()

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')
    description = factory.Faker('paragraph', nb_sentences=3)
    publication_year = factory.Faker('random_int', min=1800, max=2022)
