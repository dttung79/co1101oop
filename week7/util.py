# Dictionary containing the shipping methods and their corresponding costs
shipping_methods = {
    'Standard': 5.0,
    'Express': 10.0,
    'Priority': 15.0
}

def cal_cost(weight_method, weight, distance_method, distance, selected_method):
    if weight <= 0:
        raise ValueError('Weight must be greater than 0')
    if distance <= 0:
        raise ValueError('Distance must be greater than 0')
    
    if weight_method == 'Pounds':
        weight *= 0.45
    if distance_method == 'Miles':
        distance *= 1.61
    total_cost = (weight * 0.1) + (distance * 0.05) + shipping_methods[selected_method]
    return total_cost