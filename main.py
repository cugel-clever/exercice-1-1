from models.product.product import Product
from models.customer.customer import Customer

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

# b) Ajouter un client
print(f"\nb) Ajouter un client :")
c1 = Customer("C01", "Burger", "George", "thisburger@coco.com")
store_service.add_customer(c1)
c2 = Customer("C02", "King", "Paul", "pking@tortoro.com")
store_service.add_customer(c2)
c3 = Customer("C03", "Bake", "Shaken", "sbake@foodoo.com")
store_service.add_customer(c3)

# c) Afficher les produits disponibles
# Se fera à partir du controller... à retirer
print(f"\nc) Afficher les produits disponibles :")
show_info(p1)
print(f"\nc) Afficher les clients inscrits :")
show_info(c1)

# d) Gérer le stock (ajout/suppression)
print(f"\nd) Gérer le stock (ajout/suppression) :")
p1.add_stock(5)
print(p1)

p1.remove_stock(5)
print(p1)

# e) Créer une commande

