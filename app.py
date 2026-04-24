from flask import Flask, jsonify, request

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

# GET /products
@app.route('/products')
def get_products():
    products = product_repo.list_all()
    return jsonify([p.to_dict() for p in products])

# POST /products
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(data['id'], data['name'], data['price'])
    product_repo.add(new_product)
    return jsonify(new_product.to_dict()), 201

# GET /orders
@app.route('/orders')
def get_all_orders():
    orders = order_repo.list_all()
    return jsonify([o.to_dict() for o in orders])

# POST /enter_orders
@app.route('/enter_orders', methods=['POST'])
def enter_order():
    items = request.get_json()
    new_order = service.create_order(items)
    return jsonify(new_order.to_dict()), 201

# GET /orders/<id>
@app.route('/orders/<int:order_id>')
def get_order(order_id):
    order = order_repo.get(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict())

if __name__ == "__main__":
    app.run(debug=True)

