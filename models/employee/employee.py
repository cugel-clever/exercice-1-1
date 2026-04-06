class Employee:
    def __init__(self, id_employee, name, role):
        pass

    def show_info(self):
        return "\nEmployee : "
    
    def __str__(self):
        return(
            "==========Employee=========="
            f"{self.show_info()} "
            f"{self.id_employee}\n"
            f"Name : {self.name}\n"
            f"Role : {self.role}\n"
            "============================="
        )
