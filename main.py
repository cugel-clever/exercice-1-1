from models.product.product import Product
from models.customer.customer import Customer
from models.order.order import Order
from models.order.orderitem import OrderItem

from services.store_service import StoreService
from controllers.controller import Controller
from views.console_view import show_info

# Init
store_service = StoreService("Quebec")
controller = Controller(store_service) #possiblement inutile à retirer

# Data
# a) Ajouter un produit
print(f"\na) Ajouter un produit :")
p1 = Product("P01", "Hammer P10", 15.99, 4)
store_service.add_product(p1)
p2 = Product("P02", "Screwdriver", 12.99, 10)
store_service.add_product(p2)
p3 = Product("P03", "Deluxe Drill", 38.99, 3)
store_service.add_product(p3)
p4 = Product("P04", "Paintbrush", 5.99, 6)
store_service.add_product(p4)
p5 = Product("P05", "Seven Inch Nails (pkg-100)", 7.99, 10)
store_service.add_product(p5)
lst_product_main = [p1.id_product,p2.id_product,p3.id_product,p4.id_product,p5.id_product]
print(f"a) Ajouter produit(s) OK : \n{lst_product_main}\n")

# b) Ajouter un client
print(f"\nb) Ajouter client(s) :")
c1 = Customer("C01", "Burger", "George", "thisburger@coco.com")
store_service.add_customer(c1)
c2 = Customer("C02", "King", "Paul", "pking@tortoro.com")
store_service.add_customer(c2)
c3 = Customer("C03", "Bake", "Shaken", "sbake@foodoo.com")
store_service.add_customer(c3)
lst_customer_main = [c1.id_customer,c2.id_customer,c3.id_customer]
print(f"b) Ajouter client(s) OK : \n{lst_customer_main}\n")

# c) Afficher les produits disponibles
print(f"\nc) Afficher les produits disponibles :")
store_service.show_products("TOUS")
print("\n")

# c) Afficher les clients inscrits
store_service.show_customers()
print("\n")

# d) Gérer le stock (ajout/suppression)
print(f"\nd) Gérer le stock (ajout/suppression) :")
p1.add_stock(5)
print(p1)

p1.remove_stock(5)
print(p1)

# e) Créer une commande
o1 = Order("O01", c1)
store_service.add_order(o1)

o2 = Order("O02", c3)
store_service.add_order(o2)

print(f"\ne) Créer commande(s) :")
lst_order_main = [o1.id_order, o2.id_order]
print(f"e) Créer commande(s) OK : \n{lst_order_main}\n")

# f) Ajouter plusieurs produits à une commande
OI01 = OrderItem(o1, p1, 1)
store_service.add_orderitem(OI01)
OI02 = OrderItem(o1, p2, 2)
store_service.add_orderitem(OI02)

lst_order_main = ["OI01","OI02"]
print(f"f) Ajouter produit(s) à une commande OK  \n{lst_order_main}\n")
#print(f"\n{oi1}")
store_service.show_orderitems()

# g) Calculer le total d'une commande
print(f"\ng) Calculer le total d'une commande : \n")
total = store_service.calculate_order_total(o1,"O01")

print(f"{total}")

# h) Afficher toutes les commandes
print(f"\nh) Afficher toutes les commandes : \n")
store_service.show_orders()

# i) Vérifier la disponibilité du stock, par exemple le produit "P01"
print(f"\ni) Vérifier la disponibilité du stock : \n")
store_service.show_products("P01")

#Valider avec un produit inexistant
store_service.show_products("P00")