# задание 1
cel = float(input("Введите температуру в Цельсиях: "))
kel = cel + 273.15
far = (cel * (9 / 5)) + 32
print(f'{cel} °C = {round(kel, 2)} K')
print(f'{cel} °C = {round(far, 2)} °F')


# задание 2
cel = int(cel)
if cel % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')

if cel > 0:
    print('Число положительное')
elif cel < 0:
    print('Число отрицательное')
else:
    print('Число равно нулю')

if cel in range(10, 51):
    print('Число в диапазоне [10, 50]')
else:
    print('Число вне диапазона [10, 50]')
