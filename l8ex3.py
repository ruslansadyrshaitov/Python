class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []
while True:
    b = input("Введите число, для выхода нажмите Enter ")
    if b == "":
        break
    try:
        if b.isdigit() == False:
            raise MyOwnErr("Вводить только числа!")
    except MyOwnErr as err:
        print(err)
    else:
        a.append(b)
print(a)
