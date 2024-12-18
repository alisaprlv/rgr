import random


def computer_turn(stones):
    if stones % 4 == 0:
        return random.randint(1, 3)
    else:
        return stones % 4 or random.randint(1, 3)


def play_game():
    stones = random.randint(4, 30)

    print("🎲 Игра начинается! В куче", stones, "камней.")

    current_player = "human"

    while stones > 0:
        if current_player == "human":
            while True:
                try:
                    take = int(input("Сколько камней заберёте (1-3)? "))
                    if 1 <= take <= 3 and take <= stones:
                        break
                    else:
                        print("Некорректный ввод. Можно взять от 1 до 3 камней.")
                except ValueError:
                    print("Введите число!")

            stones -= take
            print(f"Вы взяли {take} камней. Осталось: {stones}")

            if stones == 0:
                print("🏆 Компьютер победил!")
                return

            current_player = "computer"

        else:
            take = computer_turn(stones)
            stones -= take
            print(f"Компьютер взял {take} камней. Осталось: {stones}")
            if stones == 0:
                print("🏆 Поздравляю! Вы победили!")
                return

            current_player = "human"


print("Добро пожаловать в игру 'Камни'!")
play_game()

while True:
    play_again = input("Хотите сыграть еще? (да/нет): ").lower()
    if play_again == 'да':
        play_game()
    else:
        print("Спасибо за игру!")
        break
