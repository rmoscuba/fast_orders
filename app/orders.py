
def process_orders(orders, criterion):
            
    filtered_orders = filter(lambda item: item.status == criterion, orders)
    return sum(o.price*o.quantity for o in filtered_orders)
