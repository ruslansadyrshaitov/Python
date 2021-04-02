class OfficeEquipment():
    def __init__(self, name, model, speed):
        self.name = name
        self.model = model
        self.speed = speed

    def oneq(self):
        return f"{self.name} {self.model} is On"

    def insteq(self):
        return f"{self.name} {self.model} driver is installed successfully"

    def offeq(self):
        return f"{self.name} {self.model} is Off"


class Printer(OfficeEquipment):
    def prin(self):
        return f"{self.name} prints at a speed of {self.speed} ppm"


class Scanner(OfficeEquipment):
    def scan(self):
        return f"{self.name} scans at a speed of {self.speed} ppm"


class Xerox(OfficeEquipment):
    def xer(self):
        return f"{self.name} copies at a speed of {self.speed} ppm"


printers, scaners, xeroxes = [], [], []
while True:
    eqtype = input("Тип устройства: для принтера - 1, сканера - 2, ксерокса - 3, выход - пробел ")
    if eqtype == " ":
        break
    eqname = input("Производитель устройства ")
    eqmodel = input("Модель устройства ")
    eqspeed = input("Скорость печати ")
    if eqtype == "1" and eqspeed.isdigit() == True:
        printers.append({"Производитель": eqname, "Модель": eqmodel, "Скорость": eqspeed})
    elif eqtype == "2" and eqspeed.isdigit() == True:
        scaners.append({"Производитель": eqname, "Модель": eqmodel, "Скорость": eqspeed})
    elif eqtype == "3" and eqspeed.isdigit() == True:
        xeroxes.append({"Производитель": eqname, "Модель": eqmodel, "Скорость": eqspeed})
    else:
        print("Ошибка ввода")

print(f"Принтеры\n{printers}")
i = 0
for _ in range(len(printers)):
    a = Printer(list(printers[i].values())[0], list(printers[i].values())[1], list(printers[i].values())[2])
    print(a.oneq())
    print(a.insteq())
    print(a.prin())
    print(a.offeq(), "\n")
    i += 1
print(f"Сканеры\n{scaners}")
i = 0
for _ in range(len(scaners)):
    a = Scanner(list(scaners[i].values())[0], list(scaners[i].values())[1], list(scaners[i].values())[2])
    print(a.oneq())
    print(a.insteq())
    print(a.scan())
    print(a.offeq(), "\n")
    i += 1
print(f"Ксероксы\n{xeroxes}")
i = 0
for _ in range(len(xeroxes)):
    a = Xerox(list(xeroxes[i].values())[0], list(xeroxes[i].values())[1], list(xeroxes[i].values())[2])
    print(a.oneq())
    print(a.insteq())
    print(a.xer())
    print(a.offeq(), "\n")
    i += 1
