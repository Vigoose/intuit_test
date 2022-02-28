https://packaging.python.org/en/latest/tutorials/packaging-projects/

docker run -it ecommerce python3 main_function.py
source ~/intuit_test/venv/bin/activate
kubectl describe -n kube-system pods/etcd-minikube
docker build -t ecommerce .
kubectl apply -t deployment.yaml

Buyer:
  register
  Login
  Search product
  list all product
  Add product to cart
  Checkout (make payment)
  List all orders

Seller:
  register
  Add a new product
  Edit a product
  check orders [list of orders]

Address:
  street number
  street
  city
  country


Category:
  parents
  children

User:
  user_id
  user_name
  pass_word
  address
  register_date
  viewed_items [list of product]
  account_balance

Seller:
  owned_product(list of product)
  Address
  create_product(name, description, quantity) -> Product

Buyer:
  Payment_info
  Address
 

  def login()



Product:
  name
  id
  description
  image_url
  quantity
  parents/children
  price

  __init__(self, name, description=None, image_url=''):
    


Order:
  order_id
  list of product
  buyer
  seller
  date_placed


Cart:
  total
  timestamp
  products
  user




Transaction:
  id
  account
  order
  date
  amount
  customer