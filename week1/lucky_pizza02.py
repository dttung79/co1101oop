from random import randint


def get_random_index(items):
    return randint(0, len(items) - 1)

def init_pizzas():
    pizza_types = ["margherita", "napoletana", "marinara"]
    pizza_prices = [6.0, 7.0, 7.5]
    extra_types = ["mushrooms", "cheese", "anchovies", "sausage"]
    extra_prices = [0.5, 1.0, 1.5, 1.8]
    print('Pizzas list')
    for i, p in enumerate(pizza_types):
        print(i+1, p, '$', pizza_prices[i])
    print('Extras list')
    for i, e in enumerate(extra_types):
        print(i+1, e, '$', extra_prices[i])

    return pizza_types, pizza_prices, extra_types, extra_prices

# def get_random_pizza(pizza_types, pizza_prices):
#     random = get_random_index(pizza_types)
#     pizza_type = pizza_types[random]
#     pizza_price = pizza_prices[random]

#     return pizza_type, pizza_price
def get_pizza(pizza_types, pizza_prices):
    # 1st way
    # pizza = input("What pizza do you want? ")
    # while pizza not in pizza_types:
    #     print(f"Sorry, we don't have {pizza}, please try again.")
    #     pizza = input("What pizza do you want? ")
    # pizza_price = pizza_prices[pizza_types.index(pizza)]
    # 2nd way
    choice = int(input('Enter pizza type number: '))
    while choice not in range(1, len(pizza_types) + 1):
        print(f"Sorry, we don't have {choice}, please try again.")
        choice = input('Enter pizza type number: ')

    print(f"You have chosen {pizza_types[choice-1]} $ {pizza_prices[choice-1]}")
    return pizza_types[choice-1], pizza_prices[choice-1]

def add_extra(pizza_type, pizza_price, extra_types, extra_prices):
    pizza_description = pizza_type
    n_extras = int(input('How many extras do you want? '))
    for e in range(n_extras):
        choice = int(input('Enter extra type number: '))
        extra_type = extra_types[choice]
        print(f"You have chosen {extra_type} $ {extra_prices[choice]}")
        if e == 0:
            pizza_description += f" with extra {extra_type}"
        else:
            pizza_description += f", {extra_type}"
        extra_price = extra_prices[choice]
        pizza_price += extra_price
    
    return pizza_description, pizza_price

### Main program ###
pizza_types, pizza_prices, extra_types, extra_prices = init_pizzas()
pizza_type, pizza_price = get_pizza(pizza_types, pizza_prices)
pizza_description, pizza_price = add_extra(pizza_type, pizza_price, extra_types, extra_prices)
print(f"You have won a {pizza_description} worth £{pizza_price:.2f}")
