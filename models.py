# tests/test_models.py

from django.test import TestCase
from myapp.models import Product  # replace with your actual app and model

class ProductModelTest(TestCase):
    def setUp(self):
        # Create a sample product instance to read later
        self.product = Product.objects.create(
            name="Sample Product",
            description="A product description",
            price=29.99,
            stock=100
        )
    
    def test_read_product(self):
        # Test the retrieval of the product
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.name, "Sample Product")
        self.assertEqual(product.description, "A product description")
        self.assertEqual(product.price, 29.99)
        self.assertEqual(product.stock, 100)
