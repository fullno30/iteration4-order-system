class Order:
  def __init__(self, order_id):
    self.id = order_id
    self.items = []

  def add_item(self, order_item):
    self.items.append(order_item)

  def total(self):
    return sum(item.subtotal() for item in self.items)
