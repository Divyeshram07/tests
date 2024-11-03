# tests/test_models.py

from django.test import TestCase
from myapp.models import Product  # Replace with your actual app and model

class ProductModelTest(TestCase):
    def setUp(self):
        # Create a sample product instance to delete later
        self.product = Product.objects.create(
            name="Sample Product",
            description="A product description",
            price=29.99,
            stock=100
        )
    
    def test_delete_product(self):
        # Delete the product
        product_id = self.product.id
        self.product.delete()

        # Try to retrieve the deleted product, expecting it not to be found
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)
