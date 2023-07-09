from inventory_mng import add_item, inventory, search_more_than

def test_add_item_valid_quantity():
    item = "Item 1"
    initial_quantity = 10
    quantity = 5
    inventory[item] = initial_quantity

    add_item(item, quantity)

    assert inventory[item] == initial_quantity + quantity

def test_add_item_invalid_quantity(capsys):
    item = "Item 2"
    quantity = -5

    add_item(item, quantity)

    captured = capsys.readouterr()
    assert captured.out == "Invalid quantity\n"
    assert item not in inventory

def test_add_item_exceeds_limit(capsys):
    item = "Item 3"
    quantity = 110

    add_item(item, quantity)

    captured = capsys.readouterr()
    assert captured.out == "Quantity exceeds 100\n"
    assert item not in inventory

def test_add_item_item_not_exist(capsys):
    item = "Item 4"
    quantity = 5

    add_item(item, quantity)

    captured = capsys.readouterr()
    assert captured.out == "Item does not exist in inventory\n"
    assert item not in inventory

# TODO: Write test cases for remove_item


def test_search_items_upper(capsys):
    add_item("Iphone", 100)
    add_item("Samsung", 50)
    add_item("Nokia", 20)

    items = search_more_than(50)

    assert items == ["Iphone"]
    assert "Samsung" not in items
    assert "Nokia" not in items


# TODO: Write test cases for search_less_than_or_equal