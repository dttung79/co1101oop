from util import cal_cost, shipping_methods

def test_cal_cost_01():
    weight_unit = 'Pounds'
    weight = 1.0
    distance_unit = 'Kilometers'
    distance = 10
    selected_method = 'Standard'

    cost = cal_cost(weight_unit, weight, distance_unit, distance, selected_method)
    assert cost == 5.545

def test_cal_cost_02():
    weight_unit = 'Pounds'
    weight = -1.0
    distance_unit = 'Kilometers'
    distance = 10
    selected_method = 'Standard'
    # check ValueError
    try:
        cost = cal_cost(weight_unit, weight, distance_unit, distance, selected_method)
        assert False
    except ValueError as e:
        assert e.args[0] == 'Weight must be greater than 0'
        assert True

def test_cal_cost_03():
    weight_unit = 'Pounds'
    weight = 1.0
    distance_unit = 'Kilometers'
    distance = -10
    selected_method = 'Standard'
    # check ValueError
    try:
        cost = cal_cost(weight_unit, weight, distance_unit, distance, selected_method)
        assert False
    except ValueError as e:
        assert e.args[0] == 'Distance must be greater than 0'
        assert True