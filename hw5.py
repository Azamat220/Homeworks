import random

from random import randint

spisok_slot = []
for i in range(1,31):
    spisok_slot.append(i)
print(spisok_slot)

kapital = 1000
print(f'Ваш  начальный капитал: 1000 СОМ'
      f'\nВаш выбор слоты: ')
slota = int(input())
print(f'Ваша ставка: ')
stavka = int(input())

victory = random.randint(1, 30)

if slota <= kapital:
    if slota == victory:
        stavka *= stavka
        kapital += stavka
        print(f'Вы выйграли ставку!')
    else:
        kapital -= stavka
        print(f'Вы проиграли ставку!')
else:
    print(f'Ваша ставка больше той суммы, которая у вас есть!'
          f'Попробуйте еще раз.')

print(f'Ваш капитал:',kapital)