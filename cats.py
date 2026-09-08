class Cat:
    
    cat_count = 0

    def __init__(self, name="Кіт", age=1, hunger=50):
        self.name = name
        self.age = age
        self.hunger = hunger
        print(f"Народилося кошеня на ім'я {self.name}")
        Cat.cat_count += 1

    def eat(self, food=20):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} поїв. Голод: {self.hunger}")

    def __str__(self):
        return f"Кіт {self.name}: вік {self.age}, голод {self.hunger}"


first_cat = Cat()
second_cat = Cat(name="Барсик", age=3)

print(first_cat)
print(second_cat)

first_cat.eat()

print(first_cat)
print("Всього котів:", Cat.cat_count)
