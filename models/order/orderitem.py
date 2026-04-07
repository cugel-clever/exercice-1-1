class OrderItem:
    def __init__(self, order, product, qty):
        self.order = order
        self.product = product
        self.qty = qty

    def calculate_sub_total(self):
        pass

    def show_info(self):
        return ""
    
    def __str__(self):
        return(
            "==========Order Item==========\n"
            #f"{self.show_info()} "
            f"\n{self.order}\n"
            f"{self.product}\n"
            f"Qty ordered : {self.qty}\n"
            "=============================="
        )