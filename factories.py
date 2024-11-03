# tests/factories.py

from faker import Faker
import factory
from myapp.models import Product  # replace with your actual app and model

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    
    name = factory.LazyAttribute(lambda _: fake.name())
    description = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=200))
    price = factory.LazyAttribute(lambda _: round(fake.random_number(digits=5) / 100, 2))
    stock = factory.LazyAttribute(lambda _: fake.random_int(min=0, max=1000))
    sku = factory.LazyAttribute(lambda _: fake.unique.ean(length=13))
