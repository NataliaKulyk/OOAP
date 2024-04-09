from abc import ABC, abstractmethod

# Абстрактний клас, що представляє базовий двоповерховий будинок
class TwoStoreyHouse(ABC):

    def build_house(self):
        # Побудова першого поверху
        self.build_first_floor()
        # Побудова другого поверху
        self.build_second_floor()
        # Додавання даху до будинку
        self.add_roof()
        # Додавання вікон до будинку
        self.add_windows()
        # Додавання дверей до будинку
        self.add_doors()

    @abstractmethod
    def build_first_floor(self):
        pass

    @abstractmethod
    def build_second_floor(self):
        pass

    def add_roof(self):
        # Вивід повідомлення про додавання даху
        print("Додаємо дах до будинку")

    def add_windows(self):
        # Вивід повідомлення про додавання вікон
        print("Додаємо вікна до будинку")

    def add_doors(self):
        # Вивід повідомлення про додавання дверей
        print("Додаємо двері до будинку")


# Конкретний клас, що представляє конкретний тип будинку з мансардою
class MansardHouse(TwoStoreyHouse):

    def build_first_floor(self):
        # Вивід повідомлення про побудову першого поверху
        print("Будуємо перший поверх будинку")

    def build_second_floor(self):
        # Вивід повідомлення про побудову другого поверху з мансардою
        print("Будуємо другий поверх будинку з мансардою")


# Конкретний клас, що представляє конкретний тип будинку з балконом
class BalconyHouse(TwoStoreyHouse):

    def build_first_floor(self):
        # Вивід повідомлення про побудову першого поверху
        print("Будуємо перший поверх будинку")

    def build_second_floor(self):
        # Вивід повідомлення про побудову другого поверху з балконом
        print("Будуємо другий поверх будинку з балконом")


# Конкретний клас, що представляє конкретний тип будинку з гаражем
class GarageHouse(TwoStoreyHouse):

    def build_first_floor(self):
        # Вивід повідомлення про побудову першого поверху з гаражем
        print("Будуємо перший поверх будинку з гаражем")

    def build_second_floor(self):
        # Вивід повідомлення про побудову другого поверху
        print("Будуємо другий поверх будинку")


# Конкретний клас, що представляє конкретний тип будинку з верандою
class VerandaHouse(TwoStoreyHouse):

    def build_first_floor(self):
        # Вивід повідомлення про побудову першого поверху з верандою
        print("Будуємо перший поверх будинку з верандою")

    def build_second_floor(self):
        # Вивід повідомлення про побудову другого поверху
        print("Будуємо другий поверх будинку")


# Клієнтський код
def main():
    # Будуємо будинок з мансардою
    print("Будуємо будинок з мансардою:")
    mansard_house = MansardHouse()
    mansard_house.build_house()

    # Будуємо будинок з балконом
    print("\nБудуємо будинок з балконом:")
    balcony_house = BalconyHouse()
    balcony_house.build_house()

    # Будуємо будинок з гаражем
    print("\nБудуємо будинок з гаражем:")
    garage_house = GarageHouse()
    garage_house.build_house()

    # Будуємо будинок з верандою
    print("\nБудуємо будинок з верандою:")
    veranda_house = VerandaHouse()
    veranda_house.build_house()


if __name__ == "__main__":
    main()
