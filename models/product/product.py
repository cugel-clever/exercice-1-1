class Product:
    def __init__(self, id_product, name, price, qty_stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.qty_stock = qty_stock

    def show_info(self):
        return "Product "

    def add_stock(self, qty):
        self.qty_stock += qty
        print(f"\nAdded stock for product {self.id_product} : {qty} units. Total in stock : {self.qty_stock}")

    def remove_stock(self, qty):
        self.qty_stock -= qty
        print(f"\nRemoved stock for product {self.id_product} : {qty} units. Total in stock : {self.qty_stock}")


    def __str__(self):
        return(
            f"==========Product==========\n"
            #f"{self.show_info()}"
            f"{self.id_product}\n"
            f"Name : {self.name}\n"
            f"Price : {self.price}\n"
            f"Quantity in stock : {self.qty_stock}\n"
            "==========================="
        )