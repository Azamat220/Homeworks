import random
from decouple import config


def play():
    money = int(config('MY_MONEY'))
    while True:
        print(f"На вашем счету {money}$")
        bet = int(input("Введите свою ставку: "))
        if bet > money:
            print("Недостаточно средств")
            continue
        slot = int(input("Введите номер слота (1-30): "))
        if slot < 1 or slot > 30:
            print("Недопустимый номер слота!")
            continue
        winning_slot = random.randint(1, 30)
        if slot == winning_slot:
            print("Поздравляю! Вы победили!")
            money += bet * 2
        else:
            print("Извините, вы проиграли!")
            money -= bet
        print(f"Ваш баланс теперь: {money}$")
        play_again = input("Хотите сыграть еще? (y/n): ")
        if play_again.lower() == "n":
            print("Игра завершена!")
            break

if __name__ == "__main__":
    play()