"""Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer entgegen nimmt und grundlegende mathematische Operationen
durchführt: Addition, Subtraktion, Multiplikation, Division, Ganzzahldivision und Potenzieren. Geben Sie die
Ergebnisse im Format "Operation: Ergebnis" aus."""


num1 = float(input("Bitte schreiben Sie eine Zahl"))  # Werte vom Typ String = Zeichenkette (Deutsch)
num2 = float(input("Schreiben Sie bitte eine zweite Zahl"))


# int, bool, str()

def addition(my_num1: float, my_num2: float):
    return my_num1 + my_num2


def subtraktion(my_num1: float, my_num2: float):
    return my_num1 - my_num2


def multiplikation(my_num1: float, my_num2: float):
    return my_num1 * my_num2


def division(my_num1: float, my_num2: float):
    return my_num1 / my_num2


def ganzzahldivision(my_num1: float, my_num2: float):
    return my_num1 // my_num2


def potenzieren(my_num1: float, my_num2: float):
    return my_num1 ** my_num2




