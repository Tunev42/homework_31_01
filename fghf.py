import random


def create_3d_matrix():

    print("Создание 3D матрицы (x, y, z)")

    try:
        x = int(input("Введите размер по оси X: "))
        y = int(input("Введите размер по оси Y: "))
        z = int(input("Введите размер по оси Z: "))

        if x <= 0 or y <= 0 or z <= 0:
            print("Ошибка: размеры должны быть положительными числами")
            return None


        matrix = [[[random.randint(0, 9) for _ in range(z)] for _ in range(y)] for _ in range(x)]

        print(f"\nСоздана 3D матрица размером {x}x{y}x{z}")
        return matrix
    except ValueError:
        print("Ошибка: введите целые числа для размеров матрицы")
        return None


def find_coordinates(matrix, target):

    if matrix is None:
        return []

    coordinates = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                if matrix[i][j][k] == target:
                    coordinates.append((i, j, k))

    return coordinates


def print_matrix_full(matrix):

    if matrix is None:
        return



    for i in range(len(matrix)):
        print(f"\nСлой X={i}:")
        for j in range(len(matrix[i])):
            row = " ".join(str(matrix[i][j][k]) for k in range(len(matrix[i][j])))
            print(f"  Y={j}: [{row}]")


def calculate_memory_size(matrix):

    if matrix is None:
        return 0

    # Подсчет общего количества элементов
    total_elements = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total_elements += len(matrix[i][j])


    element_memory = total_elements * 28


    num_lists = len(matrix)
    for i in range(len(matrix)):
        num_lists += len(matrix[i])

    list_memory = num_lists * 72

    total_memory = element_memory + list_memory

    return total_memory, total_elements


def format_memory_size(size_bytes):

    if size_bytes < 1024:
        return f"{size_bytes} байт"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} КБ ({size_bytes} байт)"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} МБ ({size_bytes} байт)"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} ГБ ({size_bytes} байт)"


def analyze_digit_distribution(matrix):

    if matrix is None:
        return {}

    distribution = {i: 0 for i in range(10)}

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                digit = matrix[i][j][k]
                distribution[digit] += 1

    return distribution


def main():

    # Шаг 1: Создание 3D матрицы
    matrix = create_3d_matrix()

    if matrix is None:
        return


    print_matrix_full(matrix)


    try:
        target = int(input("\nВведите цифру для поиска (0-9): "))

        if target < 0 or target > 9:
            print("Ошибка: цифра должна быть в диапазоне 0-9")
            return

        coordinates = find_coordinates(matrix, target)

        if coordinates:
            print(f"\nЦифра {target} найдена в следующих координатах (X, Y, Z):")

            # Выводим все координаты в простом формате
            for coord in coordinates:
                x, y, z = coord
                print(f"  ({x}, {y}, {z})")

            print(f"\nВсего найдено: {len(coordinates)} позиций")
        else:
            print(f"\nЦифра {target} не найдена в матрице")

    except ValueError:
        print("Ошибка: введите целое число от 0 до 9")
        return



    total_memory, total_elements = calculate_memory_size(matrix)

    print(f"  Количество элементов: {total_elements}")
    print(f"  Примерный размер в памяти: {format_memory_size(total_memory)}")


    distribution = analyze_digit_distribution(matrix)

    for digit in range(10):
        count = distribution[digit]
        if count > 0:
            print(f"  Цифра {digit}: найдена {count} раз")


if __name__ == "__main__":
    main()