from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Sepatu Bola",
            price=500000,
            description="Sepatu bola kualitas premium",
            thumbnail="http://example.com/sepatu.jpg",
            category="Shoes",
            is_featured=True,
            stock=10
        )
        self.assertEqual(product.name, "Sepatu Bola")
        self.assertEqual(product.price, 500000)
        self.assertTrue(product.is_featured)
        self.assertFalse(product.is_out_of_stock)

    def test_default_values(self):
        product = Product.objects.create(
            name="Bola",
            price=150000,
            description="Bola futsal standar",
            thumbnail="http://example.com/bola.jpg",
            category="Ball",
        )
        self.assertEqual(product.stock, 0)  # default
        self.assertFalse(product.is_featured)  # default
        self.assertTrue(product.is_out_of_stock)

    def test_decrease_stock_success(self):
        product = Product.objects.create(
            name="Jersey",
            price=250000,
            description="Jersey home warna merah",
            thumbnail="http://example.com/jersey.jpg",
            category="Apparel",
            stock=5
        )
        result = product.decrease_stock(3)
        self.assertTrue(result)
        self.assertEqual(product.stock, 2)

    def test_decrease_stock_fail(self):
        product = Product.objects.create(
            name="Gloves",
            price=100000,
            description="Sarung tangan kiper",
            thumbnail="http://example.com/gloves.jpg",
            category="Apparel",
            stock=2
        )
        result = product.decrease_stock(5)  # lebih besar dari stock
        self.assertFalse(result)
        self.assertEqual(product.stock, 2)  # tidak berubah

    def test_is_out_of_stock_property(self):
        product = Product.objects.create(
            name="Kaos Kaki",
            price=50000,
            description="Kaos kaki putih",
            thumbnail="http://example.com/socks.jpg",
            category="Apparel",
            stock=0
        )
        self.assertTrue(product.is_out_of_stock)
