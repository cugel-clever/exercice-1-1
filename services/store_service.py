
class StoreService:
    def __init__(self, name):
        self.lst_products = []
        self.lst_customers = []
        self.lst_orders = []
    
    def add_product(self, product):
        self.lst_products.append(product)

    def add_customer(self, customer):
        self.lst_customers.append(customer)

    def pass_order(self, order):
        pass

    def show_products(self, product):
        pass

    def show_orders(self, order):
        pass
