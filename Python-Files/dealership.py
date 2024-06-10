from typing import Optional
from order import *
from vehicle import *
from VehicleRepository import VehicleRepository
from OrderRepository import OrderRepository


class Dealership:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address
        self.__vehicles : list[Vehicle] = []
        self.__orders : list[Order] = []

    @property
    def vehicles(self) -> list[Vehicle]:
        return self.__vehicles

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def address(self) -> str:
        return self.__address
      
    def addVehicle(self, vehicle: Vehicle) -> None:
        self.get_vehicles_from_db()
        if vehicle not in self.__vehicles:
            self.__vehicles.append(vehicle)
            self.save_vehicles_to_db()
        else:
            print("Vehicle already in inventory!")
          
    def removeVehicle(self, vehicle: Vehicle) -> None:
        self.get_vehicles_from_db()
        if vehicle in self.__vehicles:
            self.__vehicles.remove(vehicle)
            self.save_vehicles_to_db()
            print("Vehicle removed successfully! 🤩")
        else:
            print("Vehicle doesn't exist! 😞")
           
    # add and remove order
    def addOrder(self, order: Order) -> None:
        self.get_orders_from_db()
        if order not in self.__orders:
            self.__orders.append(order)
            self.removeVehicle(order.vehicle) # removes the vehicle from inventory when an order is placed in its name
            self.save_orders_to_db()
            
    def removeOrder(self, order1: Order) -> None:
        print(str(order1))
        self.get_orders_from_db()
        for order in self.__orders:
            if order == order1:
                self.__orders.remove(order)
                self.addVehicle(order.vehicle) # adds the vehicle back to the inventory when its no longer spoken for
                self.save_orders_to_db()
                print("Order removed successfully! 🤩")
        else:
            print("Order doesn't exist! 😞")

    def searchModality(self) -> None:
        self.get_vehicles_from_db()
        print("Search for Vehicles by: ")
        print("1. Vehicle type")
        print("2. Most expensive")
        print("3. Least expensive")
        print("4. Specific feature such as cargo bed size or roof rack type.")
        u_input = int(input("Choose from the above menu and enter the corresponding number: "))
        if u_input == 1:
            user_input = input("Enter the type of car to search (suv, sedan, truck, minivan): ")
            output = self.searchForVehiclesByType(user_input)
            if output:
                print(f"Vehicles of type {output[0].__name__}")
                print(output[1])
            else:
                print("No vehicle of such type in inventory! 😞")
        elif u_input == 2:
            if len(self.__vehicles) == 0:
                print("Apologies. 😞 Inventory is empty.")
            else:
                print("The most expensive vehicle is: ")
                print(str(self.searchForMostExpensiveVehicle()))
        elif u_input == 3:
            if len(self.__vehicles) == 0:
                print("Apologies. 😞 Inventory is empty.")
            else:
                print("The least expensive vehicle is: ")
                print(str(self.searchForLeastExpensiveVehicle()))
        elif u_input == 4:
            vehicles_list: list[Vehicle] = []
            user_input = input("Enter the specific feature you want to search with (short bed/long bed/standard/heavy duty): ")
            for vehicle in self.__vehicles:
                if (hasattr(vehicle, "additionalAttr") and getattr(vehicle, "additionalAttr") == user_input.lower()):
                    vehicles_list.append(vehicle)
            if vehicles_list:
                print(f"vehicles with specific feature {user_input}: ")
                [print(str(vehicle)) for vehicle in vehicles_list]
            else:
                print(f"No vehicles with the specific feature {user_input}. 😞")

    def searchForLeastExpensiveVehicle(self) -> Vehicle:
        self.get_vehicles_from_db()
        min = self.__vehicles[0].getFinalPrice()
        target = self.__vehicles[0]
        for vehicle in self.__vehicles:
            if vehicle.getFinalPrice() <= min:
                min = vehicle.getFinalPrice()
                target = vehicle
        return target

    def searchForMostExpensiveVehicle(self) -> Vehicle:
        self.get_vehicles_from_db()
        max = 0
        target = self.__vehicles[0]
        for vehicle in self.__vehicles:
            if vehicle.getFinalPrice() >= max:
                max = vehicle.getFinalPrice()
                target = vehicle
        return target

    def searchForVehiclesByType(self, type: str) -> Optional[tuple[type, str]]:
        self.get_vehicles_from_db()
        options = {"sedan": Sedan, "suv": SUV, "truck": Truck, "minivan": Minivan}
        v_type = options.get(type)
        if v_type:
            return (v_type, "\n".join(str(vehicle) for vehicle in self.__vehicles if isinstance(vehicle, options[type.lower()])))
        else:
            return None
        
    def addOptionalFeatures(self) -> FeaturePackage:
        package = FeaturePackage() # Create a single FeaturePackage instance
        while True:
            features = {
                1: Option.EnhancedSafetyFeatures,
                2: Option.Security,
                3: Option.EntertainmentSystem,
                4: Option.Sunroof
            }
            for k, v in features.items():
                print(f"{k}. {v.name}")
            if input("Do you want to add from the above optional features? (y/n): ").lower() == "n":
                break
            u_input = int(input("Enter the number of the feature you want to add from 1-4: "))
            if u_input in features:
                package.addOption(features[u_input])  # Add the selected Option to the package
            else:
                print("Invalid feature number. 😞")
                continue
        print("Selected features: ")
        [print(str(pack)) for pack in package]
        return package
    
    def addCustomVehicle(self) -> Optional[Vehicle]:
        options = {"sedan": Sedan, "suv": SUV, "truck": Truck, "minivan": Minivan}
        type = input("Enter vehicle type from suv/sedan/truck/minivan: ").lower()
        vehicle = None
        v_type = options.get(type)
        if v_type: # checking if the user input exists in the vehicle type dictionary
            if type == "sedan":
                model = input("Enter model of vehicle: ")
                color = input("Enter preferred color of vehicle: ")
                year = int(input("Enter model year of vehicle (yyyy): "))
                vehicle = Sedan(model, color, year)
            elif type == "minivan":
                model = input("Enter model of vehicle: ")
                color = input("Enter preferred color of vehicle: ")
                year = int(input("Enter model year of vehicle (yyyy): "))
                vehicle = Minivan(model, color, year)           
            elif type in ["suv", "truck"]:
                model = input("Enter model of vehicle: ")
                color = input("Enter color of vehicle: ")
                year = int(input("Enter model year of vehicle (yyyy): "))
                if type == "suv":
                    rack_type = input("Enter rack type of vehicle from either standard/heavy duty: ")
                    vehicle = SUV(rack_type, model, color, year)
                else:  # truck
                    bed_size = input("Enter bed size of truck from either short/long: ")
                    vehicle = Truck(bed_size, model, color, year)
            if vehicle:
                self.addVehicle(vehicle)
                print("Custom vehicle created successfully! 🤩")
                print("Custom Vehicle:")
                print(str(vehicle))
        return vehicle
        
    def createCustomVehicle(self) -> None:
        vehicle = self.addCustomVehicle()
        if isinstance(vehicle, Vehicle):
            package = self.addOptionalFeatures()
            if input("Do you want to place the order? (y/n): ").lower() == "y":
                order = Order(vehicle, package)
                if order:
                    self.addOrder(order)
                    print("Order placed successfully! 🤩")
                else:
                    print("Order was not placed! 😞 Please try again.")
            else:
                self.removeVehicle(vehicle)
                print("You have chosen not to place the order. 😞")
        else:
            print("Vehicle was not added! 😞 Please try again.")
    
    def displayVehicles(self) -> str:
        self.get_vehicles_from_db()
        self.vehicle_index_mapping: dict[int, Vehicle] = {}
        output = ""
        for count, vehicle in enumerate(self.__vehicles, 1):
            self.vehicle_index_mapping[count] = vehicle
            output += f"{count}. {str(vehicle)}\n"
        return output
    
    def displayOrders(self) -> str:
        self.get_orders_from_db()
        self.order_index_mapping: dict[int, Order] = {}
        output = ""
        for count, order in enumerate(self.__orders, 1):
            self.order_index_mapping[count] = order
            output += "*******************************************"
            output += f"\n{count}. {str(order)}\n"
            output += "*******************************************"
        return output
    
    def orderFromInventory(self, u_input: int) -> None:
        vehicle = self.vehicle_index_mapping.get(u_input)
        if vehicle:
            print("Selected vehicle: ")
            print(str(vehicle))
            package = self.addOptionalFeatures()
            if input("Do you want to place the order? (y/n): ").lower() == "y":
                order = Order(vehicle, package)
                if order:
                    self.addOrder(order)
                    print("Order placed successfully! 🤩")
                else:
                    print("Order was not placed! 😞 Please try again.")
            else:
                print("You have chosen not to place the order. 😞")
        else:
            print("Invalid input! 😞 Please try again.")

    def removeCustomVehicleByDealer(self, u_input: int) -> None:
        vehicle = self.vehicle_index_mapping.get(u_input)
        if vehicle:
            print("Vehicle to be deleted: ")
            print(str(vehicle)) 
            conf = input("Please confirm that you want to delete this vehicle: (y/n): ").lower()
            if conf == "y":
                self.removeVehicle(vehicle)
        else:
            print("Invalid input! 😞 Please try again.")

    # def removeOrderByDealer(self, u_input: int) -> None:
    #     # order = self.order_index_mapping.get(u_input)
    #     self.get_orders_from_db()
    #     for order in self.__orders:
    #         if order.id == u_input:
    #             print("Order to be removed: ")
    #             print(str(order))
    #             conf = input("Please confirm that you want to delete this order: (y/n): ").lower()
    #             if conf == "y":
    #                 self.removeOrder(order)
    #     else:
    #         print("Invalid input! 😞 Please try again.")             
   
    # Retriving and Saving Vehicles from and to database  
    def get_vehicles_from_db(self) -> None:
        repo = VehicleRepository("vehicles.csv")
        self.__vehicles = repo.read_vehicles()
        
    def save_vehicles_to_db(self) -> None:
        repo = VehicleRepository("vehicles.csv")
        repo.write_vehicles(self.__vehicles)
        
    # Retrieving and Saving Orders from and to Database
    def get_orders_from_db(self) -> None:
        repo = OrderRepository("orders.csv")
        self.__orders = repo.read_orders()
    
    def save_orders_to_db(self) -> None:
        repo = OrderRepository("orders.csv")
        repo.save_orders(self.__orders)
    
    def __str__(self) -> str:
        inventory_str = '\n'.join(str(vehicle) for vehicle in self.__vehicles)
        orders_str = '\n'.join(str(order) for order in self.__orders)
        return f"Dealer name = {self.__name}, address = {self.__address}\n" \
            f"Vehicles in firm inventory:\n{inventory_str}\n" \
            f"Orders:\n{orders_str}"

    def display(self) -> None:
        print(self)
        

def main() -> None:
    # Create vehicles
    sedan2 = Sedan("Toyota Camry", "Silver", 2017)
    luxury_sedan = Sedan("Mercedes-Benz S-Class", "Black", 2020)

    pickup_truck = Truck("Long Bed", "Ford F-150", "Red", 2016)
    compact_truck = Truck("short bed", "Nissan Frontier", "White", 2014)

    compact_suv = SUV("standard", "Honda CR-V", "Blue", 2019)
    crossover_suv = SUV("Heavy Duty", "Subaru Outback", "Black", 2021)

    family_minivan = Minivan("Honda Odyssey", "White", 2020)
    luxury_minivan = Minivan("Mercedes-Benz Metris", "Silver", 2019)
    
    # create featurePackages
    s_package = FeaturePackage()
    s_package.addOption(Option.EnhancedSafetyFeatures)
    s_package.addOption(Option.Sunroof)
    
    t_package = FeaturePackage()
    t_package.addOption(Option.Security)
    t_package.addOption(Option.EntertainmentSystem)
    
    # Create orders with vehicles and packages
    order1 = Order(sedan2, s_package)
    order4 = Order(luxury_minivan, FeaturePackage())
    
    # create dealership and add vehicles and orders
    dealership = Dealership("XYZ", "24 Bullevard Street")
    dealership.addVehicle(crossover_suv)
    dealership.addVehicle(family_minivan)
    dealership.addVehicle(compact_truck)
    dealership.addVehicle(compact_suv)
    dealership.addVehicle(luxury_minivan)
    dealership.addVehicle(pickup_truck)
    dealership.addVehicle(luxury_sedan)
    dealership.addVehicle(sedan2)
    
    dealership.addOrder(order1)
    dealership.removeOrder(order1)
    dealership.addOrder(order4)

    dealership.display()
    print("hala")
    dealership.displayOrders()

if __name__ == "__main__":
    main()
