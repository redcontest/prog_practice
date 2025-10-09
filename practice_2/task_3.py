def main():
    cakes = input("Введите целое число (количество пирожных): ")
    while not (all(i in "0123456789" for i in cakes) and cakes != ''):
        cakes = input("Ошибка! Требуется целое положительное число: ")
    print_pack_report(int(cakes))


def print_pack_report(total_cakes: int):
    for cakes in range(total_cakes, 0, -1):
        if cakes % 5 == 0 and cakes % 3 == 0:
            print(f"{cakes} - расфасуем по 3 или по 5")
        elif cakes % 5 == 0 and cakes % 3 != 0:
            print(f"{cakes} - расфасуем по 5")
        elif cakes % 5 != 0 and cakes % 3 == 0:
            print(f"{cakes} - расфасуем по 3")
        else:
            print(f"{cakes} - не заказываем!")


if __name__ == '__main__':
    main()
