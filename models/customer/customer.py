class Customer:
    def __init__(self, id_customer, name, firstname, email):
        self.id_customer = id_customer
        self.name = name
        self.firstname = firstname
        self.email = email

    def show_info(self):
        return "\nCustomer : "
    
    def __str__(self):
        return(
            "==========Customer==========\n"
            #f"{self.show_info()} "
            f"{self.id_customer}\n"
            f"Name : {self.name}\n"
            f"First name : {self.firstname}\n"
            f"Email : {self.email}\n"
            "============================"
        )