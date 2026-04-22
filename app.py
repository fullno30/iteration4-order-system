from flask import Flask, jsonify

from domain.product import Product
from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository
from service.order_service import OrderService

app = Flask(__name__)

product_repo = ProductRepository()
order_repo = OrderRepository()
service = OrderService(product_repo, order_repo)

# Seed products
def startup_data():
  product_repo.add(Product(1, "Mug", 12.50))
  product_repo.add(Product(2, "Scarf", 25.00))
  
startup_data()

# Seed order using dictionaries
def startup_order():
  items = [
    {"id": 1, "qty": 2},
    {"id": 2, "qty": 1}
  ]
  service.create_order(items)

startup_order()

# Get /products
@app.route('/products')
def get_products():
  products = product_repo.list_all()
  return jsonify([p.to_dict() for p in products])
  
# Get /orders/<id>
@app.route('/orders/<int:order_id>')
def get_order(order_id):
  order = order_repo.get(order_id)
  if order is None:
    return jsonify({"error": "Order not found"}), 404
  return jsonify(order.to_dict())

if __name__ == "__main__":
  app.run(debug=True)
