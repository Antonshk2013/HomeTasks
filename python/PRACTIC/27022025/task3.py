def sum_digits_non_tail(n):
    if n < 10:
        return n
    return n % 10 + sum_digits_non_tail(n // 10)


def sum_digits_tail(n, accumulator=0):
    if n < 10:
        return accumulator + n
    return sum_digits_tail(n // 10, accumulator + n % 10)


a = 12345
print("Сумма цифр: ", sum_digits_non_tail(a)) # 15
print("Сумма цифр: ", sum_digits_tail(a)) # 15
