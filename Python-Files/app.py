from vehicle import *
from dealership import Dealership
from order import *


class App:
    def __init__(self) -> None:
        self.__dealership = Dealership("XYZ", "4711 Warm Springs Blvd")
        self.__dealership.get_orders_from_db()
        self.__dealership.get_vehicles_from_db()
    
    # @property
    # def dealership(self) -> Dealership:
    #     return self.__dealership

    def show_title(self) -> None:
        print(f"Name = {self.__dealership.name}, Address = {self.__dealership.address}")
    
    def show_customer_menu(self):
        print("===== CUSTOMER MENU =====")
        print("1. Display all vehicles in inventory")
        print("2. Search vehicles")
        print("3. Create custom vehicle")
        print("4. Order vehicle from inventory")
        print("5. Exit")
    
    def show_dealer_menu(self):
        print("===== DEALERSHIP MENU =====")
        print("11. Add a New Vehicle")
        print("12. Display all available vehicles")
        print("13. Remove a vehicle")
        # print("14. Remove order for a customer")
        print("14. Exit")

    def show_menu(self) -> None:
        print("=====  MENU =====")
        print("1. Log on as a Dealer.")
        print("2. Log on as a customer.")
        print("3. Exit")
        u_input = int(input("Select from the above options (1/2): "))
        if u_input == 1:
            cont = True
            while cont:
                self.show_dealer_menu()
                command = int(input("Enter your choice: "))
                print("#*#*#*##*#*#*##*#*#*##*#*#*##*#*#*##*#*#*#")
                cont = self.process_command(command)
                print("#*#*#*##*#*#*##*#*#*##*#*#*##*#*#*##*#*#*#")
        elif u_input == 2:
            cont = True
            while cont:
                self.show_customer_menu()
                command = int(input("Enter your choice: "))
                print("#*#*#*##*#*#*##*#*#*##*#*#*##*#*#*##*#*#*#")
                cont = self.process_command(command)
                print("#*#*#*##*#*#*##*#*#*##*#*#*##*#*#*##*#*#*#")
        elif u_input == 3:
            print("Bye!")
            cont = False
            return None
        else:
            print("Invalid input! 😞 Please enter numbers from the displayed menu!")

    def process_command(self, command: int) -> bool:
            cont = True
            if command == 1 or command == 12:
                print("Vehicles in inventory: ")
                print(self.__dealership.displayVehicles())
            elif command == 2:
                self.__dealership.searchModality()
            elif command == 3:
                print("Creating a custom vehicle: ")
                self.__dealership.createCustomVehicle()
            elif command == 4:
                print("Vehicles in inventory: ")
                print(self.__dealership.displayVehicles())
                u_input = int(input("Enter the number of the vehicle you are interested in: "))
                self.__dealership.orderFromInventory(u_input)
            elif command == 5 or command == 14:
                print("Bye!")
                cont = False
            elif command == 11:
                self.__dealership.addCustomVehicle()
            elif command == 13:
                print("Vehicles in inventory: ")
                print(self.__dealership.displayVehicles())
                u_input = int(input("Enter the number of the vehicle you want to delete: "))
                self.__dealership.removeCustomVehicleByDealer(u_input)
            # elif command == 14:
            #     print("All Orders To Date: ")
            #     print(self.__dealership.displayOrders())
            #     u_input = int(input("Enter the number of the order you want to delete: "))
            #     self.__dealership.removeOrderByDealer(u_input)
            else:
                print("Invalid input! 😞 Please enter numbers from the displayed menu!")
            return cont


def main():
    app = App()
    app.show_title()
    # print(str(app.dealership))

    while True:
        app.show_menu()
        break
        # command = int(input("Enter your choice: "))
        # print("#*#*#*##*#*#*##*#*#*##*#*#*##*#*#*##*#*#*#")
        # cont = app.process_command(command)
        # print("#*#*#*##*#*#*##*#*#*##*#*#*##*#*#*##*#*#*#")


if __name__ == "__main__":
    main()
