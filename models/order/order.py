from models.product.product import Product

class Order:
    def __init__(self, id_order, customer):
        self.id_order = id_order
        self.customer = customer

    def add_product(self, product, qty):
        pass

    def calculate_total(self):
        pass

    def show_info(self):
        return ""

    def __str__(self):
        return(
            "============Order===========\n"
            #f"{self.show_info()} "
            f"{self.id_order}\n"
            f"{self.customer}"
            "\n============================\n"
        )