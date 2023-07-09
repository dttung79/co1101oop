from product import Product
def load_products():
    products = []
    products.append(Product('iPhone 12', 1000, 10))
    products.append(Product('iPhone 12 Pro', 1200, 5))
    products.append(Product('iPhone 12 Pro Max', 1400, 3))
    products.append(Product('iPhone 12 Mini', 800, 10))
    products.append(Product('iPhone 11', 700, 20))
    products.append(Product('iPhone 11 Pro', 900, 30))
    products.append(Product('iPhone 11 Pro Max', 1100, 30))

    return products