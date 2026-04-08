import logging
from abc import ABC, abstractmethod
from typing import Type

# Налаштування логування: рівень INFO, вивід у консоль
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# 1. Абстрактний базовий клас Vehicle з типізацією
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make: str = make
        self.model: str = model
        self.spec: str = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass

# 2. Реалізація Car та Motorcycle з використанням logging 
class Car(Vehicle):
    def start_engine(self) -> None:
        # Заміна print на logging.info
        logger.info(f"Car: {self.make} {self.model} ({self.spec}): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        # Заміна print на logging.info 
        logger.info(f"Motorcycle: {self.make} {self.model} ({self.spec}): Мотор заведено")

# 3. Абстрактний клас VehicleFactory з анотаціями типів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass

# 4. Конкретні фабрики з типізацією повертаємих об'єктів
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")

# 5. Використання фабрик (клієнтський код)
def run_factory_demo(factory: VehicleFactory) -> None:
    # Типізація локальних змінних
    car: Car = factory.create_car("Toyota", "Corolla")
    bike: Motorcycle = factory.create_motorcycle("Harley-Davidson", "Sportster")
    
    car.start_engine()
    bike.start_engine()

if __name__ == "__main__":
    logger.info("--- Створення техніки для США ---")
    run_factory_demo(USVehicleFactory())

    logger.info("\n--- Створення техніки для ЄС ---")
    run_factory_demo(EUVehicleFactory())