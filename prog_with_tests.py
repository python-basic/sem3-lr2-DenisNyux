import math


def g_square(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def main():
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    assert b + c >= a, "it`s not a triangle"
    assert a + c >= b, "it`s not a triangle"
    assert a + b >= c, "it`s not a triangle"

    print('Результат: ', round(g_square(a, b, c), 5))


main()


if __name__ == "__main__":
    
    assert round(g_square(2.0, 3.0, 2.0), 5) == 1.98431, "Wrong counting"

    assert g_square(1, 2, 1) == 0.0, "Wrong counting"

    assert type(g_square(2.0, 3.0, 2.0)) == float, "Wrong type"
