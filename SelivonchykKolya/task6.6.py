# task 4.6
# A singleton is a class that allows only a single instance of itself to be created and gives access to that created
# instance. Implement singleton logic inside your custom class using a method to initialize class instance.
class Sun:
    __instance = None

    def __init__(self):
        if not self.__instance:
            ...
        else:
            self.inst()

    @classmethod
    def inst(self):
        if not self.__instance:
            self.__instance = Sun()
        return self.__instance


p = Sun.inst()
f = Sun.inst()
print(p is f)