x = 120
from logging import basicConfig
import os
import csv
from contextlib import contextmanager


class NowyIterator:
    def __init__(self):
        pass
    def __iter__(self):
        pass
    def __next__(self):
        pass

@contextmanager
def contextmanager_example():
    zmienna = 1
    print("poczatek")
    zmienna += 1
    yield zmienna
    print("koniec")

# with contextmanager_example() as example:
#     print(example + 1)

class Product:
    name: str
    probability: int

    @classmethod
    def quantity(cls, probability: int) -> int:
        return probability - cls.probability + 1
        
class Wood(Product):
    name = "Wood"
    probability: int = 10

print(Wood.quantity())



def basic_datatypes():

    lista = ["ala", "ma", "kota", "ale", "kot", "ma", "ale"]
    set_example = {"ala", "ma", "kota", "ale", "kot", "ma", "ale"}
    print("nasza lista")
    for index in range(0, len(lista)):
        print(f"{index=}")
        elem = lista[index]
        print(elem)
    print("nasz set")
    tuple_example = (0, "ala")
    # tuple_example[2] = "table" # nie mozna modyfikowac elemntow w krotce
    # tuple is immutable
    for index, elem in enumerate(set_example):
        print(f"{index=}")
        print(elem)
    ilosc_zasobow = {
        "drewno" : 1,
        "stal" : 5
    }
    cena_zasobow = {
        "drewno" : 4,
        "stal" : 9,
    }
    print(f"Mamy tyle drewna: {ilosc_zasobow['drewno']}")
    zasoby = {
        "drewno": {
            "value" : 100,
            "probability": 4
        },
        "stal": {
            "value" : 100,
            "probability": 9
        }
    }
    print(f"Mamy tyle drewna: {zasoby['drewno']['quantity']}")
    
    for key, value in dict_example.items():
        print(f"key is: {key}")
        print(f"value is: {value}")
    for key in dict_example:
        elem = dict_example[key]



def main():
    csv_filepath =  os.path.join(os.path.expanduser("~"), "Downloads", "Mieszkania_roczne.csv")   
    with open(csv_filepath) as csvfile:
        data = csv.reader(csvfile, delimiter=";")
        faulty_data = csv.reader(csvfile)
        for row in data:
            print(row)

def zle_uzycie_open():
    z = open("file.txt")
    try: 
        x = "hi" + 5
    finally:
        z.close()
    with open("file.txt") as of:
        x = "hi" + 5

try:
    zle_uzycie_open()
except TypeError:
    print("polecial typerror")

print("kod dalej")


if __name__ == "__main__":
    # main()
    basic_datatypes()

