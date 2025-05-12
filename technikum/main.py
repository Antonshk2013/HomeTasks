"""
 Verwenden Sie collections.Counter, um die Anzahl jedes Zeichens in einer Zeichenkette zu zählen. Schreiben Sie
eine Funktion count_characters, die eine Zeichenkette annimmt und ein CounterObjekt mit der Anzahl der
einzelnen Zeichen zurückgibt. Geben Sie anschließend die 3 am häufigsten vorkommenden Zeichen aus.
"""

from collections import Counter, deque, namedtuple
from math import dist

def count_characters(s: str):
    return Counter(s).most_common(3)




"""
Verwenden Sie collections.deque, um eine Warteschlange mit fester Länge zu erstellen. Schreiben Sie eine
Funktion fixed_queue, die eine Liste von Zahlen und die maximale Länge der Warteschlange annimmt, die
Elemente der Liste zur Warteschlange hinzufügt und den endgültigen Zustand der Warteschlange zurückgibt.
"""


def fixed_queue(numbers, max_length):
    queue = deque(maxlen=max_length)
    print(queue)
    for number in numbers:
        queue.append(number)
    return list(queue)
"""
Erstellen Sie ein benanntes Tupel Point mit den Feldern x, y und z. Schreiben Sie eine Funktion calculate_distance,
die zwei PointObjekte annimmt und den Abstand zwischen ihnen im dreidimensionalen Raum berechnet.
"""

def calculate_distance(p1, p2):
    return dist(p1, p2)


if __name__ == '__main__':
    # print(count_characters("fastretrewgr"))
    # list_numbers = [1, 2, 3, 4, 5, 6]
    # print(fixed_queue(list_numbers, 3))
    # print(list_numbers[-3:])
    Point = namedtuple('point', 'x, y, z')
    point1 = Point(1, 2, 3)
    point2 = Point(100, 200, 300)
    print(round(calculate_distance(point1, point2), 2))