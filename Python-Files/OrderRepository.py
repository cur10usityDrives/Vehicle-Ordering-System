from order import *
from vehicle import *
import csv


class OrderRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename
        
    def save_orders(self, orders: list[Order]) -> None:
        with open(self.__filename, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["VehicleTypeId", "Model", "Color", "Year", "BasePrice", "TotalPrice", "AdditionalAttribute", "OptionalFeatures", "", "", ""])
            for order in orders:
                if isinstance(order.vehicle, Sedan):
                    vehicle = [str(order.id)] + order.vehicle.convert_to_list("1")
                    vehicle.append(str(order.getTotalPrice()))
                    writer.writerow(vehicle + order.convertToListPackages())
                elif isinstance(order.vehicle, Truck):
                    vehicle = [str(order.id)] + order.vehicle.convert_to_list("2")
                    vehicle.append(str(order.getTotalPrice()))
                    vehicle.append(order.vehicle.additionalAttr)
                    writer.writerow(vehicle + order.convertToListPackages())
                elif isinstance(order.vehicle, SUV):
                    vehicle = [str(order.id)] + order.vehicle.convert_to_list("3")
                    vehicle.append(str(order.getTotalPrice()))
                    vehicle.append(order.vehicle.additionalAttr)
                    writer.writerow(vehicle + order.convertToListPackages())
                elif isinstance(order.vehicle, Minivan):
                    vehicle = [str(order.id)] + order.vehicle.convert_to_list("4")
                    vehicle.append(str(order.getTotalPrice()))
                    writer.writerow(vehicle + order.convertToListPackages())
                    
    def read_orders(self) -> list[Order]:
        orders: list[Order] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[1] == "1":
                    vehicle = Sedan(row[2], row[3], int(row[4]))
                elif row[1] == "2":
                    vehicle = Truck(row[6], row[2], row[3], int(row[4]))
                elif row[1] == "3":
                    vehicle = SUV(row[6], row[2], row[3], int(row[4]))
                elif row[1] == "4":
                    vehicle = Minivan(row[2], row[3], int(row[4]))
                            
                # make a Feature package object from the row that is being read            
                if row[1] == "1" or row[1] == "4":
                    features = FeaturePackage()
                    for option in row[7:]:
                        features.addOption(Option[option])
                elif row[1] == "2" or row[1] == "3":
                    features = FeaturePackage()
                    for option in row[8:]:
                        features.addOption(Option[option])
                if features: # type: ignore
                    order = Order(vehicle, features) # type: ignore
                    orders.append(order)
        return orders

def main():
    # Create orders
    sedan = Sedan("Honda Accord", "White", 2015)
    truck = Truck("Short Bed", "Chevrolet Silverado", "Blue", 2019)
    suv = SUV("Heavy Duty", "Toyota RAV4", "Green", 2022)
    minivan = Minivan("Chrysler Pacifica", "Gray", 2018)
    
    s_package = FeaturePackage()
    s_package.addOption(Option.EnhancedSafetyFeatures)
    s_package.addOption(Option.Sunroof)
    
    t_package = FeaturePackage()
    t_package.addOption(Option.Security)
    t_package.addOption(Option.EntertainmentSystem)
    
    # Create orders with vehicles and packages
    order1 = Order(sedan, s_package)
    order2 = Order(truck, t_package)
    order3 = Order(suv, FeaturePackage())
    order4 = Order(minivan, FeaturePackage())
    

    # Save orders to a file
    order_repo = OrderRepository("orders.csv")
    order_repo.save_orders([order1, order2, order3, order4])

    
    # Read orders from the file
    orders = order_repo.read_orders()
    
    # Display read orders
    for order in orders:
        order.display()
        print()

if __name__ == "__main__":
    main()
