from vehicle import *
import csv


class VehicleRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename
        
    def write_vehicles(self, vehicles: list[Vehicle]) -> None:
        with open(self.__filename, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["VehicleTypeId", "Model", "Color", "Year", "Price", "AdditionalAttribute"])
            for vehicle in vehicles:
                # arbitrary ids are assigned to each of the vehicle types
                if isinstance(vehicle, Sedan):
                    writer.writerow(vehicle.convert_to_list("1"))
                elif isinstance(vehicle, Truck):
                    truck_data = vehicle.convert_to_list("2")
                    truck_data.append(vehicle.additionalAttr)
                    writer.writerow(truck_data)
                elif isinstance(vehicle, SUV):
                    suv_data = vehicle.convert_to_list("3")
                    suv_data.append(vehicle.additionalAttr)
                    writer.writerow(suv_data)
                elif isinstance(vehicle, Minivan):
                    writer.writerow(vehicle.convert_to_list("4"))
    
    def read_vehicles(self) -> list[Vehicle]:
        vehicles: list[Vehicle] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == "1":
                    vehicle = Sedan(row[1], row[2], int(row[3]))
                elif row[0] == "2":
                    vehicle = Truck(row[5], row[1], row[2], int(row[3]))
                elif row[0] == "3":
                    vehicle = SUV(row[5], row[1], row[2], int(row[3]))
                elif row[0] == "4":
                    vehicle = Minivan(row[1], row[2], int(row[3]))
                vehicles.append(vehicle) # type: ignore
        return vehicles
    
    
def main():
    vehicles: list[Vehicle] = []
    vehicles.append(Sedan("Honda Accord", "White", 2015))
    vehicles.append(Truck("Short Bed", "Chevrolet Silverado", "Blue", 2019))
    vehicles.append(SUV("Heavy Duty", "Toyota RAV4", "Green", 2022))
    vehicles.append(Minivan("Chrysler Pacifica", "Gray", 2018))

    repo = VehicleRepository("vehicles.csv")
    repo.write_vehicles(vehicles)

    vehicles2 = repo.read_vehicles()
    print(list(str(v) for v in list(vehicles2)))


if __name__ == "__main__":
    main()
