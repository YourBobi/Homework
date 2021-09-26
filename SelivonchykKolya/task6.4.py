"""
### Task 4.4
Create hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.
"""


class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} bird can walk")

    def fly(self):  # Не все птицы летают
        ...

    def __str__(self):
        return self.name + " can walk"


class FlyingBird(Bird):

    def __init__(self, name):
        super().__init__(name)
        self.ration = "mostly grains"

    def fly(self):
        print(f"{self.name} bird can fly")

    def eat(self):
        print(f"It eats {self.ration}")

    def __str__(self):
        return self.name + " can walk and fly"


class NonFlyingBird(Bird):

    def __init__(self, name):
        super().__init__(name)
        self.ration = "mostly fish"

    def eat(self):
        print(f"It eats {self.ration}")

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def swim(self):
        print(f"{self.name} bird can swim")

    def __str__(self):
        return self.name + " can walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name):
        super().__init__(name)
        self.ration = "fish"

    def __str__(self):
        return self.name + " can walk, fly and swim"


b = SuperBird("Bob")
b.eat()
b.fly()
b.swim()
print(b)
