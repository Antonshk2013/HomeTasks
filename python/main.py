import math
from decimal import Decimal

# 1. Дана строка с именем, например, “Иван”. Написать программу,
# которая печатает приветствие, например, “Привет, Иван!”.

def hello(name: str):
    return f"Hello, {name}"


# 2. Веб-страницы состоят из строк типа "<i>Yay</i>" - выводит текст Yay курсивом.
# В этом примере, строка-тег “i” означает <i> и </i>, которые окружают слово Yay.
# Нам дана строка-тэг и текст.
# Написать программу, которая выводит тег вокруг данного текста,
# например,  "<i>Yay</i>". Например, ('i', 'Hello') → '<i>Hello</i>'.

def render_html(tag, context):
    return f"<{tag}>{context}</{tag}>"

# 3. Дана строка. Написать программу, которая создает строку
# из трех копий последних двух символов данной строки.
# Данная строка должна быть длиной минимум 2.
# (('Hello') → 'lololo'), ('ab') → 'ababab'.

def ignorance_string(some_string: str):
    if len(some_string) > 1:
        return some_string[-2:]*3

# 4. Дана строка, написать программу, которая печатает строку без первого и последнего
# символа от данной строки, например, “Иван” - “ва”. “Python” -> “ytho”.

def get_midle_string(some_string: str):
    return some_string[1:-1]

# 5. Даны две строки разной длины (одна может быть пустой). Написать программу,
# которая печатает строку вида короткая+длинная+короткая,
# где короткая строка снаружи длинной.
# Например, 'Hello', 'hi' → 'hiHellohi'.

def two_string(some_string: str, some_string2: str):
    if len(some_string)==len(some_string2):
        return f"Error strin1 == string2"
    elif len(some_string)>len(some_string2):
        return f"{some_string2}{some_string}{some_string2}"
    else:
        return f"{some_string}{some_string2}{some_string}"

# 6. Написать программу, которая печатает True,
# если слова “cat” и “dog” встречаются в строке одинаковое количество раз
# (и напечатать False - если разное количество раз).
# 'catdog' → True,
# 'catcat' → False,
# '1cat1catodog' → True


# Важно: запрещено использовать методы count() и replace()

def find_tiere(some_string: str):
    if len(some_string) < 5:
        return False
    cat, dog = "cat", "dog"
    cat_count, dog_count = 0, 0
    start_position = 0
    while start_position+3 <= len(some_string):
        curent_string = some_string[start_position:start_position+3]
        start_position += 1
        if cat == curent_string:
            cat_count += 1
        elif dog == curent_string:
            dog_count += 1
    if cat_count == dog_count:
        return True
    return False


#
# 7. Написать программу, которая печатает количество вхождений данной подстроки в строк.
# Например, для подстроки hi, 'abc hi ho' → 1,
# для подстроки “well”,  'ABCwell well') → 2.
# Важно: запрещено использование метода count()

def count_sub_string_insert(some_string: str, sub_string: str):
    if (len(some_string) or len(sub_string)) == 0:
        return False
    start_position = 0
    count_sub_string = 0
    count_sab_string_insert = 0
    for varcha in sub_string:
        count_sub_string += 1
    while start_position + count_sub_string <= len(some_string):
        some_sub_string = some_string[start_position:start_position+count_sub_string]
        if some_sub_string == sub_string:
            count_sab_string_insert += 1
        start_position += 1
    return count_sab_string_insert


# 8. Для данной строки, напечатать строку, где каждый символ повторяется дважды,
# например, 'The' → 'TThhee', 'AAbb' → 'AAAAbbbb'.
# Подсказка: перебрать i по каждому значению индекса в строке 0, 1, 2, .. len-1.

def ignorance_buch(some_string: str):
    new_string = ""
    for buch in some_string:
        new_string += buch
        new_string += buch
    return new_string




# 9. Написать программу, которая по заданной длине катетов прямоугольного треугольника
# вычисляет длину гипотенузы.
# Поменяйте программу так, чтобы длина гипотенузы выводилась
# с точностью до двух знаков после запятой.

def calculation_of_hypotenuse(a: float):
    return round(math.sqrt((2*a)**2), 2)



# 10. Написать программу, которая по данному радиусу вычисляет:
# длину окружности (2pi*r), площадь круга (pi * r ^ 2), объем шара (4/3)*pi*r^3).


# 11. Написать программу, которая считывает 5 вещественных чисел с клавиатуры
# и печатает сумму этих чисел с точностью до одного знака после запятой.

def spin_words(sentence):
    # Your code goes here
    string_list = sentence.split(" ")
    for i in range(len(string_list)):
        if len(string_list[i]) >= 5:
            string_list[i] = string_list[i][::-1]
    return " ".join(string_list)

def replace_exclamation(st):
    return "".join([i if i not in 'aeiouAEIOU' else "!" for i in st])

def derive(coefficient, exponent):
    return f"{coefficient*exponent}x^{exponent-1}"

def positive_sum(arr):
    arr_sum = sum([number if number>0 else 0 for number in arr])
    #
    # for number in arr:
    #     arr_sum += number if number > 0 else 0
    # # [arr_sum = arr_sum + number for number in arr]
    return arr_sum\

def is_valid_parenthesses(sequense: str)->bool:
    return sum([1 if i == '(' else 0 for i in sequense]) == sum([1 if i == ')' else 0 for i in sequense])

def is_valid_parenthesses(sequense: str)->bool:
    return sum([1 if i == '3' else 0 for i in sequense]) == sum([1 if i == ')' else 0 for i in sequense])


"""На вход программе подается натуральное число n, а затем n строк. 
    Напишите программу, которая создает список из символов всех строк, а 
    затем выводит его. В результирующем списке могут содержаться одинаковые символы."""

def buils_string(index_count, *args):
    return "".join(map(str, args))

if __name__ == '__main__':
    # print(hello("Anastasia"))
    # print(render_html("div", "Anastasia"))
    # print(ignorance_string("Hello"))
    # print(get_midle_string("Python"))
    # print(two_string('hi',"Python"))
    # print(find_tiere("cotasdasdcatdog"))
    # print(count_sub_string_insert("catcatcatcatcatcatcatcatcat", "cat"))
    # print(ignorance_buch("Hello"))
    # print(calculation_of_hypotenuse(9.99))
    # print(spin_words("Hey wollef warriors"))
    # print(replac,_exclamation("ABCDE"))
    # print(derive(7,8))
    # print(positive_sum([1,2,3,-10, 10]))
    #
    # numbers = [1, 2, 3, 4]
    # next = [20, 30, 40]
    # numbers.append(next)
    # print(numbers)
    # next.append(50)
    # print(numbers)
    # print(is_valid_parenthesses('))'))

    """На вход программе подается натуральное число n, а затем n строк. 
    Напишите программу, которая создает список из символов всех строк, а 
    затем выводит его. В результирующем списке могут содержаться одинаковые символы."""

