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

# tests/test_models.py

from django.test import TestCase
from myapp.models import Product  # Replace with your actual app and model

class ProductModelTest(TestCase):
    def setUp(self):
        # Create multiple product instances for listing
        Product.objects.create(name="Product 1", description="Description 1", price=19.99, stock=50)
        Product.objects.create(name="Product 2", description="Description 2", price=29.99, stock=30)
        Product.objects.create(name="Product 3", description="Description 3", price=39.99, stock=20)

    def test_list_all_products(self):
        # Retrieve all products
        products = Product.objects.all()

        # Check that the number of products retrieved matches the number created
        self.assertEqual(products.count(), 3)
        
        # Optional: Verify each product's data
        self.assertEqual(products[0].name, "Product 1")
        self.assertEqual(products[1].name, "Product 2")
        self.assertEqual(products[2].name, "Product 3")

# tests/test_models.py

from django.test import TestCase
from myapp.models import Product  # Replace 'myapp' with the actual app name

class ProductModelTest(TestCase):
    def setUp(self):
        # Set up products in the database for testing
        Product.objects.create(name="Sample Product", description="A sample product", price=10.99, stock=15)
        Product.objects.create(name="Another Product", description="Another sample product", price=15.99, stock=10)

    def test_find_product_by_name(self):
        # Fetch the product by name
        product = Product.objects.get(name="Sample Product")
        
        # Verify that the fetched product has the expected name
        self.assertEqual(product.name, "Sample Product")
        self.assertEqual(product.description, "A sample product")
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.stock, 15)


# tests/test_models.py

from django.test import TestCase
from myapp.models import Product, Category  # Replace 'myapp' with the actual app name

class ProductModelTest(TestCase):
    def setUp(self):
        # Set up a category and related products in the database for testing
        self.category = Category.objects.create(name="Electronics")
        Product.objects.create(name="Smartphone", category=self.category, price=599.99, stock=50)
        Product.objects.create(name="Tablet", category=self.category, price=399.99, stock=30)

    def test_find_product_by_category(self):
        # Fetch products by category
        products = Product.objects.filter(category=self.category)
        
        # Verify the correct number and details of products in the "Electronics" category
        self.assertEqual(products.count(), 2)
        self.assertTrue(all(product.category == self.category for product in products))
# tests/test_models.py

from django.test import TestCase
from myapp.models import Product  # Replace 'myapp' with the actual app name

class ProductModelTest(TestCase):
    def setUp(self):
        # Set up available and unavailable products in the database for testing
        Product.objects.create(name="Laptop", price=999.99, stock=10)  # In stock
        Product.objects.create(name="Headphones", price=199.99, stock=0)  # Out of stock

    def test_find_product_by_availability(self):
        # Fetch products that are available (stock > 0)
        available_products = Product.objects.filter(stock__gt=0)
        
        # Verify that only products with stock greater than zero are returned
        self.assertEqual(available_products.count(), 1)
        self.assertEqual(available_products[0].name, "Laptop")
        self.assertGreater(available_products[0].stock, 0)

