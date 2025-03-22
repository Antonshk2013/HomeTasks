# 1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.




def gome_task_1():
    try:
        with open("additional_files/22.txt", "r") as f:
            for line in f.readlines():
                if int(line)<0:
                    raise ValueError

    except ValueError as e:
        return f'Одно из чисел является отрицательным {e.__class__.__name__} {e}'

    else:
        with open("additional_files/22.txt", "r") as f:
            a, b = f.readlines()
            return int(a)/int(b)

# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами
# (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений и закрытия
# файла в блоке finally.

def gome_task_2():
    try:
        with open("additional_files/23.txt", "r") as f:
            a, b = f.readlines()
            return int(a) / int(b)

    except ZeroDivisionError as e:
        return f'Чтслитель не может быть 0 {e.__class__.__name__} {e}'

    except ValueError as e:
        return f'Одна из строк не является чиалом {e.__class__.__name__} {e}'

    except FileNotFoundError as e:
        return f'файл не найден {e.__class__.__name__} {e}'

    finally:
        print("Ну файл мне закрывать не нужно")




if __name__ == '__main__':
    print(gome_task_1())
    print(gome_task_2())

