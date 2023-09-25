
def process_orders(orders, criterion):
    if criterion != 'all':
        filtered_orders = filter(lambda item: item.status == criterion, orders)
    else:
        filtered_orders = orders
    return sum(o.price*o.quantity for o in filtered_orders)
