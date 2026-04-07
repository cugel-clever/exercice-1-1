
class StoreService:
    def __init__(self, name):
        self.lst_products = []
        self.lst_customers = []
        self.lst_orders = []
        self.lst_orderitems = []
    
    def add_product(self, product):
        self.lst_products.append(product)

    def add_customer(self, customer):
        self.lst_customers.append(customer)

    def add_order(self, order):
        self.lst_orders.append(order)

    def add_orderitem(self, orderitem):
        self.lst_orderitems.append(orderitem)

    def show_products(self, product):
        i = 0 #Index to iterate through the list (VERY inefficient...)
        j = len(self.lst_products)
        produit_existant = False
        while i < len(self.lst_products):
            if product.upper() == "TOUS":
                print(f"Produits disponibles : {len(self.lst_products)}")
                for prod_item in self.lst_products:
                    print(f"{prod_item}")
                i = j #To get out ASAP of the while!
            elif product is not None:
                for prod_item in self.lst_products:
                    if product.upper() == self.lst_products[i].id_product:
                        print(f"{prod_item}\n")
                        i = j #To get out ASAP of the while!
                        produit_existant = True
                        break
                #Else implicite: idéalement, we should check for errors, but time is of the essence!
                if not produit_existant:
                    print(f"Le produit {product} ne fait pas partie de l'inventaire actuel. Réessayez.")
                    i = j #To get out ASAP of the while!

    def show_customers(self):
        print(f"Clients inscrits : {len(self.lst_customers)}")
        for cust_item in self.lst_customers:
            print(f"{cust_item}")

    def show_orders(self):
        print(f"Afficher les commandes : {len(self.lst_orders)}")
        for order_index in self.lst_orders:
            print(f"{order_index}")

    def show_orderitems(self):
        print(f"Afficher les détails de la commande : {len(self.lst_orderitems)}")
        for orderitem_index in self.lst_orderitems:
            print(f"{orderitem_index}")

    def calculate_order_total(self, id_order, id_order_name):
        i = 0 #Index to iterate through the list (VERY inefficient...)
        total = 0
        print(f"Calculer le total de la commande : {id_order_name}")

        while i < len(self.lst_orderitems):
            if id_order_name.upper() == self.lst_orderitems[i].order.id_order:
                total += (self.lst_orderitems[i].product.price * self.lst_orderitems[i].qty)
                i += 1
            else:
                i += 1
        return total