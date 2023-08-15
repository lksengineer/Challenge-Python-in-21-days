# Import Base Class / Super Class: Product
from product import Product


class Article(Product):
    """Class Article, Inherits from the Product Class"""
    def addToCart(self):
        """Add to cart method"""
        return f"Agregando {self.quantity} unidades del artículo {self.name} al carrito"


class Service(Product):
    """Class Service, Inherits from the Product Class"""
    def addToCart(self):
        """Add to cart method"""
        return f"Agregando el servicio {self.name} al carrito"


# polo = Article("Polo", 5, 500)
# backend = Service("Backend develop", 500, 1)
#
# print(polo.addToCart())
# print(backend.addToCart())


class Cart:
    """Class cart"""
    def __init__(self):
        self.products = []
        """Constructor and attributes from cart Class"""

    def addProduct(self, product):
        """Add product method from cart class"""
        product.addToCart()
        self.products.append(product)

    def deleteProduct(self, product):
        """Delete product method"""
        self.products = [prod for prod in self.products if prod.name != product.name]

    def calculateTotal(self):
        """Calculate Total method."""
        return sum(prod.price * prod.quantity for prod in self.products)

    def getProducts(self):
        """Get Products method"""
        return self.products

# Input 1:

# book = Article("Libro", 100, 2)
# course = Service("Curso", 120, 1)
#
# cart = Cart()
# cart.addProduct(book)
# cart.addProduct(course)
# cart.calculateTotal()

# Output:
#
# Agregando 2 unidades del artículo Libro al carrito
# Agregando el servicio Curso al carrito
# 320

# Input 2:

book = Article("Libro", 100, 2)
course = Service("Curso", 120, 1)

cart = Cart()
cart.addProduct(book)
cart.addProduct(course)
cart.deleteProduct(book)
cart.calculateTotal()
cart.getProducts()

# Output:

# Agregando 2 unidades del artículo Libro al carrito
# Agregando el servicio Curso al carrito
# 120