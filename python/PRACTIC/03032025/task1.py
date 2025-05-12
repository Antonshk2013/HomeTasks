from functools import partial


def get_area(side1, side2, is_triangle=False):
    if side2 is None:
        side2 = side1
    if is_triangle:
        return side1 * side2 * 0.5
    return side1 * side2


square_area = partial(get_area, side2=None)
rectangle_area = partial(get_area)
right_triangle_area = partial(get_area, is_triangle=True)


print(square_area(3))  # 9
# print(rectangle_area(2, 3))  # 6
# print(right_triangle_area(2, 3))  # 3.0