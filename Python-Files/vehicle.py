from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model: str, color: str, year: int, basePrice: float) -> None:
        self.__model = model
        self.__basePrice = basePrice
        self.__color = color
        self.__year = year

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model: str) -> None:
        self.__model = new_model

    @property
    def basePrice(self) -> float:
        return self.__basePrice
    
    @basePrice.setter
    def basePrice(self, basePrice: float) -> None:
        self.__basePrice = basePrice

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str) -> None:
        self.__color = new_color

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year: int) -> None:
        self.__year = new_year

    def __str__(self) -> str:
        return f"Model = {self.__model}, Base Price = {self.basePrice}, Color = {self.__color}, Model Year = {self.__year}"
    
    def display(self) -> None:
        print(self)

    def convert_to_list(self, vehicleId: str) -> list[ str]:
        lst = [vehicleId]
        lst.append(self.__model)
        lst.append(self.__color)
        lst.append(str(self.__year))
        lst.append(str(self.__basePrice))

        return lst
    
    @abstractmethod
    def getFinalPrice(self) -> float:
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return False
        return (self.__model == other.__model and
                self.__basePrice == other.__basePrice and
                self.__color == other.__color and
                self.__year == other.__year)


class Truck(Vehicle):
    def __init__(self, bedSize: str, model: str, color: str, year: int, price: float = 35000) -> None:
        super().__init__(model, color, year, price)
        self.__additionalAttr = bedSize.lower()

    def getFinalPrice(self) -> float:
        if self.__additionalAttr == "short bed":
            return self.basePrice + 150
        elif self.__additionalAttr == "long bed":
            return self.basePrice + 250
        else: 
            return self.basePrice
        
    @property
    def additionalAttr(self) -> str:
        return self.__additionalAttr
    
    @additionalAttr.setter
    def additionalAttr(self, size: str) -> None:
        self.__additionalAttr = size.lower()
    
    def __str__(self) -> str:
        return super().__str__() + f"\nCargo Bed Size = {self.__additionalAttr}, Total Price = {self.getFinalPrice()}"


class SUV(Vehicle):
    def __init__(self, rackType: str, model: str, color: str, year: int, price: float = 40000) -> None:
        super().__init__(model, color, year, price)
        self.__additionalAttr = rackType.lower()

    def getFinalPrice(self) -> float:
        if self.__additionalAttr == "standard":
            return self.basePrice + 150
        elif self.__additionalAttr == "heavy duty":
            return self.basePrice + 250
        else: 
            return self.basePrice
        
    @property
    def additionalAttr(self) -> str:
        return self.__additionalAttr
    
    @additionalAttr.setter
    def additionalAttr(self, rack: str) -> None:
        self.__additionalAttr = rack.lower()

    def __str__(self) -> str:
        return super().__str__() + f"\nRoof Rack Type = {self.__additionalAttr}, Total Price = {self.getFinalPrice()}"


class Minivan(Vehicle):
    def __init__(self, model: str, color: str, year: int, price: float = 45000) -> None:
        super().__init__(model, color, year, price)

    def getFinalPrice(self) -> float:
        return self.basePrice
    
    def __str__(self) -> str:
        return super().__str__() + f"\nTotal Price = {self.getFinalPrice()}"


class Sedan(Vehicle):
    def __init__(self, model: str, color: str, year: int, price: float = 30000) -> None:
        super().__init__(model, color, year, price)

    def getFinalPrice(self) -> float:
        return self.basePrice
    
    def __str__(self) -> str:
        return super().__str__() + f"\nTotal Price = {self.getFinalPrice()}"


# def main() -> None:
#     sedan = Sedan("Honda Accord", "White", 2015)
#     print(sedan)
#     truck = Truck("Short Bed", "Chevrolet Silverado", "Blue", 2019)
#     print(truck)
#     suv = SUV("Heavy Duty", "Toyota RAV4", "Green", 2022)
#     print(suv)
#     minivan = Minivan("Chrysler Pacifica", "Gray", 2018)
#     print(minivan)


# if __name__ == "__main__":
#     main()
