print()
print('Задача "Developer - не только разработчик"')
print('----------')
print()

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(self.name)
        if new_floor > self.number_of_floors or new_floor < 1:
            print(' Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(' ', i)
        print()

first = House('ЖК Горский', 20)
second = House('Домик в деревне', 3)
first.go_to(6)
second.go_to(5)
print('----------')