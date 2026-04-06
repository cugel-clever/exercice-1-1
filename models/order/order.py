class Order:
    def __init__(self, id_order, customer, lstproduct, total):
        self.id_order = id_order
        self.customer = customer
        self.lstproduct = lstproduct
        self.total = total

    def add_product(self, product, qty):
        pass

    def calculate_total(self):
        pass

    def show_order(self):
        pass
