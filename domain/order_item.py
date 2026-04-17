class OrderItem:
  def __init__(self, product, quantity):
    self.product = product
    self.quantity = quantity

  def subtotal(self):
    return self.product.price * self.quantity

  def to_dict(self):
    return {
      "product": self.product.to_dict(),
      "quantity": self.quantity,
      "subtotal": self.subtotal()
    }
