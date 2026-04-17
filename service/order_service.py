from domain.order import Order
from domain.order_item import OrderItem

class OrderService:
    def __init__(self, product_repo, order_repo):
        self.product_repo = product_repo
        self.order_repo = order_repo
        self._next_order_id = 1

    def create_order(self, items_data):
        order = Order(self._next_order_id)
        self._next_order_id += 1

        for product_id, quantity in items_data:
            product = self.product_repo.get(product_id)
            if product is None:
                raise ValueError(f"Product with ID {product_id} does not exist.")

            order_item = OrderItem(product, quantity)
            order.add_item(order_item)

        self.order_repo.save(order)
        return order
