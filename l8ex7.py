class ComplNum:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Комплексное число {self.number}"

    def __add__(self, other):
        return ComplNum(self.number + other.number)

    def __mul__(self, other):
        return ComplNum(self.number * other.number)


while True:
    try:
        n_1 = ComplNum(complex(input("Введите первое комплексное число ")))
        n_2 = ComplNum(complex(input("Введите второе комплексное число ")))
        n_3 = ComplNum(complex(input("Введите третье комплексное число ")))
    except ValueError as err1:
        print("Ошибка ввода")
        break
    print(n_1 * n_2)
    print(n_1 + n_3)
    print(n_1 * n_2 * n_3)
    print(n_1 + n_2 + n_3)
    break
