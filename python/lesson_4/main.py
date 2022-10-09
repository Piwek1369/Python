import csv
import os
from pprint import pprint
from enum import Enum
from dataclasses import dataclass
import sqlite3

import click

class NPC():
    _id = None

class Shopkeeper(NPC):
    _id = "Shopkeeper"

class MountainMark(Shopkeeper):
    name = "Mountain Mark"


# baza danych: world.db
# tabela: shopkeeper
# Index | Nazwa
# tabela: shopkeeper_items
# Index | Index_shopkeepera | Nazwa | Ilość

# SELECT Index FROM shopkeeper WHERE Nazwa = "Mountain Mark";
# SELECT Ilość FROM shopkeeper_items WHERE Index_shopkeepera = 1 AND Nazwa = "sword";


class DBClient:
    def __init__(self, db_name: str) -> None:
        self._con = sqlite3.connect(f"{db_name}.db")
        self._cur = self._con.cursor()
    def get_items(self, item):
        res = self._cur.execute(f"SELECT {item} FROM items_db")
        res.fetchall()
        return res


def get_sword():
    db_name = "items_db"
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    # cur.execute("CREATE TABLE movie(title, year, score)")
    res = cur.execute(f"SELECT sword FROM {db_name}")
    res.fetchone()


    db_client = DBClient("items_db")
    db_client.get_items("sword")

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


@click.command()
@click.option("--file-path", "-f", help="Path to csv with data", default=os.path.join(os.path.expanduser("~"), "Downloads", "Mieszkania_roczne.csv"))
def main(file_path: str) -> None:
    apartments = []
    with open(file_path, encoding='utf-8') as csvfile:
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