class Date:
    def __init__(self, d):
        self.d = d

    @classmethod
    def m_1(cls, d):
        a, b, c = d.split("-")
        a, b, c = int(a), int(b), int(c)
        return f"Число {a} {type(a)} Месяц {b} {type(b)} Год {c} {type(c)}"

    @staticmethod
    def m_2(d):
        a, b, c = d.split("-")
        a, b, c = int(a), int(b), int(c)
        if 1 <= a <= 31 and b in [1, 3, 5, 7, 8, 10, 12] and 1 <= c <= 2021:
            return f"Данные верны"
        elif 1 <= a <= 30 and b in [4, 6, 9, 11] and 1 <= c <= 2021:
            return f"Данные верны"
        elif 1 <= a <= 28 and b == 2 and 1 <= c <= 2021 and c % 4 != 0:
            return f"Данные верны"
        elif 1 <= a <= 29 and b == 2 and 1 <= c <= 2021 and c % 4 == 0:
            return f"Данные верны"
        else:
            return f"Неверные данные"


d_1 = Date("10-12-2021")
d_2 = Date("02-03-1995")
d_3 = Date("30-12-1998")
print("Первый метод")
print(d_1.m_1("29-02-2020"))
print(Date.m_1("29-02-2020"))
print("Второй метод")
print(d_1.m_2("29-02-2020"))
print(Date.m_2("29-02-2021"))
