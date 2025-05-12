def two_digit_operations(num1):
    first_digit = num1 // 10
    second_digit = num1 % 10
    # einzelne Zahlen bekommen und als Variabeln speichern
    print(f"Mein Produkt: {first_digit * second_digit} Meine Summe: {first_digit + second_digit}")

user_input = int(input("Geben Sie bitte eine zweistellige Zahl ein :"))
two_digit_operations(user_input)


def right_triangle(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2


lst = [6, 8, 10]
print(right_triangle(*lst))