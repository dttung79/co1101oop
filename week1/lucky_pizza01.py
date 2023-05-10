from random import randint


def get_random_index(items):
    return randint(0, len(items) - 1)

def init_pizzas():
    pizza_types = ["margherita", "napoletana", "marinara"]
    pizza_prices = [6.0, 7.0, 7.5]
    extra_types = ["mushrooms", "cheese", "anchovies", "sausage"]
    extra_prices = [0.5, 1.0, 1.5, 1.8]

    return pizza_types, pizza_prices, extra_types, extra_prices

def get_random_pizza(pizza_types, pizza_prices):
    random = get_random_index(pizza_types)
    pizza_type = pizza_types[random]
    pizza_price = pizza_prices[random]

    return pizza_type, pizza_price

def add_extra(pizza_type, pizza_price, extra_types, extra_prices):
    pizza_description = pizza_type
    n_random_extras = randint(1, 3)
    for e in range(n_random_extras):
        random = get_random_index(extra_types)
        extra_type = extra_types[random]
        if e == 0:
            pizza_description += f" with extra {extra_type}"
        else:
            pizza_description += f", {extra_type}"
        extra_price = extra_prices[random]
        pizza_price += extra_price
    
    return pizza_description, pizza_price

### Main program ###
pizza_types, pizza_prices, extra_types, extra_prices = init_pizzas()
pizza_type, pizza_price = get_random_pizza(pizza_types, pizza_prices)
pizza_description, pizza_price = add_extra(pizza_type, pizza_price, extra_types, extra_prices)
print(f"You have won a {pizza_description} worth £{pizza_price:.2f}")
