from product import Product
def load_products():
    products = []
    # products.append(Product('iPhone 12', 1000, 10))
    # products.append(Product('iPhone 12 Pro', 1200, 5))
    # products.append(Product('iPhone 12 Pro Max', 1400, 3))
    # products.append(Product('iPhone 12 Mini', 800, 10))
    # products.append(Product('iPhone 11', 700, 20))
    # products.append(Product('iPhone 11 Pro', 900, 30))
    # products.append(Product('iPhone 11 Pro Max', 1100, 30))

    f = open('products.csv', 'r')
    lines = f.readlines()[1:] # read all lines except the first line
    for li in lines:
        li = li.strip() # remove the \n at the end of the line
        name, price, stock = li.split(',')
        p = Product(name, float(price), int(stock))
        products.append(p)
    f.close()
    return products

def save_products(products):
    f = open('products.csv', 'w')
    f.write('Name,Price,Stock\n')
    for p in products:
        f.write(f'{p.name},{p.price},{p.stock}\n')
    f.close()