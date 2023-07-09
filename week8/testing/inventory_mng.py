inventory = {}

def add_item(item, quantity):
    if quantity < 0:
        print('Invalid quantity')
        return
    if quantity > 100:
        print('Quantity exceeds 100')
        return
    if item not in inventory:
        print('Item does not exist in inventory')
        return
    
    inventory[item] += quantity

def remove_item(item, quantity):
    if item not in inventory:
        print('Item does not exist in inventory')
        return
    
    if inventory[item] < quantity:
        print('Quantity exceeds inventory')
        return
    
    if quantity < 0:
        print('Invalid quantity')
        return
    
    inventory[item] -= quantity

def search_more_than(quantity):
    items = []
    for item in inventory:
        if inventory[item] > quantity:
            items.append(item)
    return items

def search_less_than_or_equal(quantity):
    items = []
    for item in inventory:
        if inventory[item] <= quantity:
            items.append(item)
    return items