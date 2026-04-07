
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

    def show_products(self):
        print(f"c) Afficher les produits disponibles : {len(self.lst_products)}")
        for prod_item in self.lst_products:
            print(f"{prod_item}")

    def show_customers(self):
        print(f"c) Afficher les clients inscrits : {len(self.lst_customers)}")
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

    #nouveau code en test
    def calculate_order_total(self, id_order, id_order_name):
        i = 0 #Index to iterate through the list (VERY inefficient...)
        total = 0
        print(f"Calculer le total de la commande : {id_order_name}")

        while i < len(self.lst_orderitems):
            if id_order_name.upper() == self.lst_orderitems[i].order.id_order:
                #print("Ça marche!!!")
                total += (self.lst_orderitems[i].product.price * self.lst_orderitems[i].qty)
                i += 1
            else:
                i += 1
        return total