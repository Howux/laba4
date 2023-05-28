# Пракитическое задание 4

def one(number):
    if int(number) % 3 == 0:
        return print("Число делится на 3")
    else:
        print("Число не делится на 3")


def two():
    number = input("Введите число: ")

    if number.isdigit() == False:
        return print("Вы ввели не число")
    if int(number) == 0:
        return print("На ноль делить нельзя. Введите другое число")

    def divide(number):
        anwser = 100 / int(number)
        return print(f"100 : {number} = {anwser}")

    divide(number)


def three():
    data = input("Введите дату (дд.мм.гггг): ")

    def magic(data):
        if int(data[:2]) * int(data[3:5]) == int(data[-2:]):
            return print("True")
        else:
            return print("False")

    magic(data)


def four():
    number = input("Введите номер билета (кол-во чисел должно быть четным): ")

    def lucky_ticket(number):

        quantity = len(number) // 2
        if sum(list(map(int, number[:quantity]))) == sum(list(map(int, number[quantity:]))):
            print("Это счастливый билет")
        else:
            print("Это не счастливый билет")

    if len(number) % 2 != 0:
        return print("Вы ввели число с нечетным кол-вом чисел")
    else:
        lucky_ticket(number)


# three()
# four()