

def sum_prod(x:int, y:int):
    print(f"Сумма и произведение чисел: {(x + y ,x * y)}")


def count_min_max(int_list:list):
    print(f"Сумма чисел: {sum(int_list)}")
    print(f"Минимальное значение: {min(int_list)}")
    print(f"Максимальное значение: {max(int_list)}")


if __name__ == '__main__':
    sum_prod(3, 4)
    count_min_max([3, 7, 2, 9, 1, 5])
