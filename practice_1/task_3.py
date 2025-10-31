# задача 4
s = input('Введите текст: ').upper()
count = []
symbols = set(s)

for c in symbols:
    count.append([c, s.count(c)])
    print(f'{c} встречается {s.count(c)} раз')

count.sort(key=lambda x: x[1], reverse=True)
print('3 самых частых символа:')
for i in range(3):
    print(f'{count[i][0]} (встречается {count[i][1]} раз)')
