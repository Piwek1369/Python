import csv
import os
from pprint import pprint
from enum import Enum
from dataclasses import dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    @staticmethod
    def total_cost_static(unit_price: float, quantity_on_hand: int = 0) -> float:
        return unit_price * quantity_on_hand

    @classmethod
    def total_cost_class(cls) -> float:
        return cls.unit_price * cls.quantity_on_hand

    # To jest najlepsza metoda :)
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


class ApartmentType(str, Enum):
    APPROVALS = "Approvals"
    STARTED = "Started"
    IN_PROGRESS = "In progress"
    FINISHED = "Finished"

@dataclass
class Apartments:
    type: ApartmentType
    quantity: int 
    year: int
    unit: int = 1000


def main():
    csv_filepath =  os.path.join(os.path.expanduser("~"), "Downloads", "Mieszkania_roczne.csv")   
    apartments = []
    with open(csv_filepath, encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter=";")
        for row in data:
            if "pozwolenia" in row[0]:
                type = ApartmentType.APPROVALS
            elif "rozpoczęto" in row[0]:
                type = ApartmentType.STARTED
            elif "w budowie" in row[0]:
                type = ApartmentType.IN_PROGRESS
            elif "oddane do" in row[0]:
                type = ApartmentType.FINISHED
            else:
                continue
            if row[2] == "tys.":
                unit = 1000
            for i, year in enumerate(range(2000, 2022)):
                column_number = 3 + i
                print(f"{column_number=}")
                apartments.append(
                    Apartments(type=type, quantity=row[column_number], year=year, unit=unit)
                )
    pprint(apartments)

if __name__ == "__main__":
    main()