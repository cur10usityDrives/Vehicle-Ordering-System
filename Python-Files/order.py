from vehicle import *
from enum import Enum


class Option(Enum):
    EnhancedSafetyFeatures = 3000
    Security = 1000
    EntertainmentSystem = 2000
    Sunroof = 2500
    
    def __str__(self):
        return f"{self.name}: {self.value}"
    

class FeaturePackage:
    def __init__(self) -> None:
        self.__options: list[Option] = []
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index >= len(self.__options):
            raise StopIteration
        value = self.__options[self.__index]
        self.__index += 1
        return value
    
    def addOption(self, option: Option) -> None:
        if option not in self.__options:
            self.__options.append(option)

    def removeOption(self, option: Option) -> None:
        if option in self.__options:
            self.__options.remove(option)
    
    def getPrice(self) -> float:
        return sum(option.value for option in self.__options)
    
    def __str__(self) -> str:
        output = "Optional Features selected:\n"
        output += "\n".join(option.name for option in self.__options)
        output += f"\nFeatures Total = {self.getPrice()}"
        return output

    def display(self):
        print(self)

class Order:
    orderID = 0
    def __init__(self, vehicle: Vehicle, feature: FeaturePackage) -> None:
        Order.orderID += 1
        self.__id = Order.orderID
        self.__vehicle = vehicle
        self.__feature_package = feature

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def vehicle(self) -> Vehicle:
        return self.__vehicle
    
    @property
    def feature_package(self) -> FeaturePackage:
        return self.__feature_package

    def getTotalPrice(self) -> float:
        return self.__vehicle.getFinalPrice() + self.__feature_package.getPrice() 
    
    def convertToListPackages(self) -> list[str]:
        return [option.name for option in self.__feature_package]
            
    def __str__(self) -> str:
        return f"Order details:\nOrderId = {self.__id}\n{self.__vehicle}\n{self.__feature_package}\nFeatures Inclusive Price of Order = {self.getTotalPrice()}"
    
    def display(self):
        print(self)

    def __eq__(self, __object: object) -> bool:
        if not isinstance(__object, Order):
            return False
        return (self.__id == __object.__id)
        
        
# def main() -> None:
#     sedan = Sedan("Honda Accord", "White", 2015)
#     print(sedan)
#     print("Final price:", sedan.getFinalPrice())

#     print()
#     truck = Truck("Short Bed", "Chevrolet Silverado", "Blue", 2019)
#     print(truck)
#     print("Final price:", truck.getFinalPrice())

#     print()
#     suv = SUV("Heavy Duty", "Toyota RAV4", "Green", 2022)
#     print(suv)
#     print("Final price:", suv.getFinalPrice())

#     print()
#     minivan = Minivan("Chrysler Pacifica", "Gray", 2018)
#     print(minivan)
#     print("Final price:", minivan.getFinalPrice())
#     print()
    
#     fp = FeaturePackage()
#     fp.addOption(Option.Security)
#     fp.addOption(Option.Sunroof)
#     fp.display()
    
#     print("\nThe first order:")
#     order1 = Order(truck, fp)
#     print(order1)


# if __name__ == "__main__":
#     main()
