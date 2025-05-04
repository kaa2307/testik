# Программа для расчета площади прямоугольника

def calculate_area(length, width):
    """
    Функция для расчета площади прямоугольника.

    :param length: длина прямоугольника
    :param width: ширина прямоугольника
    :return: площадь прямоугольника
    """
    return length * width


if __name__ == "__main__":
    try:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = calculate_area(length, width)
        print(f"Площадь прямоугольника: {area}")
    except ValueError:
        print("Ошибка: введите числовое  значение.")
