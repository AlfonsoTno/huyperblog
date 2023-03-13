import unittest

from product import Product
from shopping_cart import ShoppingCart

class TestShopingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>>> método setUpClass se ejecuta antes de las pruebas')

    @classmethod    
    def tearDownClass(cls):
        print('>>> El método tearDownClass se ejecuta despues de las pruebas')
    
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product (self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        

    def tearDown(self):
        pass

    def test_product_objet(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos el carrito de conmpras no se encuntra vacio')
        

if __name__ == '__main__':
    unittest.main()