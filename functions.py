from random import randrange


# функция взаимодействующая с вводом пользователя
def IntInput():
    while True:
        try:
            inp = str(input())  # пользователь вводит данные
            x = int(inp)  # введенную строку пытаемся конвертировать в целове счисло и вернуть
            return x
        except:
            # отслеживаем ошибки, если введено не число - ValueError, если команда
            # (Ctrl + C ; Ctrl + Z) - Keyboard  Interrupt
            print("Неверный ввод данных, введите число: ")


def cell_condition_rand_choice(Gameboard):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]  # Массив создан так, чтобы при выборе между состоянием 0/1, предпочтение отдавалось 0
    for i in Gameboard.cell_matrix:
        for j in i:
            j.condition = x[randrange(0, 10)]


def cell_condition_manual_choice(Gameboard):
    for i in Gameboard.cell_matrix:
        for j in i:
            print("Введите цифру 1, если хотите заполнить клетку, иначе 0: ")
            temp = IntInput()

            while temp != 0 and temp != 1:
                print("Неверный формат ввода, введите 1 или 0: ")
                temp = IntInput()

            j.condition = temp
