# tests/test_models.py

from django.test import TestCase
from myapp.models import Product  # Replace with your actual app and model

class ProductModelTest(TestCase):
    def setUp(self):
        # Create a sample product instance to update later
        self.product = Product.objects.create(
            name="Sample Product",
            description="A product description",
            price=29.99,
            stock=100
        )
    
    def test_update_product(self):
        # Update the product's name and price
        self.product.name = "Updated Product Name"
        self.product.price = 39.99
        self.product.save()

        # Retrieve the updated product from the database
        updated_product = Product.objects.get(id=self.product.id)
        
        # Assert that the updates were saved correctly
        self.assertEqual(updated_product.name, "Updated Product Name")
        self.assertEqual(updated_product.price, 39.99)
