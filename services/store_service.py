
class StoreService:
    def __init__(self, name):
        self.lst_products = []
        self.lst_customers = []
        self.lst_orders = []
    
    def add_product(self, product):
        self.lst_products.append(product)

    def add_customer(self, customer):
        self.lst_customers.append(customer)

    def add_order(self, order):
        self.lst_orders.append(order)

    def show_products(self):
        print(f"c) Afficher les produits disponibles : {len(self.lst_products)}")
        for prod_item in self.lst_products:
            print(f"{prod_item}")

    def show_customers(self):
        print(f"c) Afficher les clients inscrits : {len(self.lst_customers)}")
        for cust_item in self.lst_customers:
            print(f"{cust_item}")

    def show_orders(self):
        pass
