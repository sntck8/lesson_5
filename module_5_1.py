class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f" {self.name} {self.number_of_floors}-этажное здание")
        if new_floor <= self.number_of_floors:
            print(f"Поднимаемся на {new_floor}-й этаж")
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"{new_floor} - такого этажа в здании НЕТ")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 3)
h1.go_to(5)
h2.go_to(10)