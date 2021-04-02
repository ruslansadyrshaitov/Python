class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input("Введи делимое "))
    b = float(input("Введи делитель "))
    if b == 0:
        raise MyOwnErr("На 0 делить нельзя")
    print(f"Частное {a / b:.2f}")
except (ValueError, MyOwnErr) as err:
    print(err)
