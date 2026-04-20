from flask inport Flask, jsonify
from domain.product import Product
from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository
from service.order_service import OrderService

app = Flask(__name__)

product_repo = ProductRepository()
order_repo = OrderRepository()
service = OrderService(product_repo, order_repo)

def startup_data():
  product_repo.add_product(Product(1, "Mug", 12.50))
  product_repo.add_product(Product(2, "Scarf", 25.00))
  product_repo.add_product(Product(3, "Notebook", 7.99))
  
startup_data()

def startup_order():
  items = [
    {"id": 1, "qty": 2},
    {"id": 2, "qty": 1}
  ]
  service.create_order(items)

startup_order()
