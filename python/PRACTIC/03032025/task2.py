import _sha1

"""Это хвостовая рекурсия (tail recursion) или не хвостовая (non-tail recursion)?

    def sum_list(lst):
        if not lst:
            return 0
        return lst[0] + sum_list(lst[1:])

Как преобразовать её в рекурсию (не) хвостового типа?
"""


def sum_list_tail_or_non_tail_recursion(lst, accumulation=0):
    if not lst:
        return accumulation
    accumulation += lst[-1]
    lst.pop()
    return sum_list_tail_or_non_tail_recursion(lst, accumulation)

def sum_list_tail_recursion(lst,accumulator=0):
    if not lst:
        return accumulator
    return sum_list_tail_recursion(lst[1:], accumulator + lst[0])

if __name__ == '__main__':
    # print(sum_list_tail_or_non_tail_recursion([1, 2, 3, 4, 5]))  # 15
    # print(_sha1(None))
    print({1, 1.0, True})
