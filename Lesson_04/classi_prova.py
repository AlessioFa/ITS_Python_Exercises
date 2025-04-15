class MyList:
    def __init__(self):
        self.lst = []
    
    def aggiungi(self, val: int):
        self.lst.append(val)

    def fing(self, val: int) -> bool:
        return val in self.lst

mylist = MyList()
mylist.aggiungi(10)
print(mylist)  #stampa l indirizzo di memoria 


class Person:
    def __init__(self, name: str, age; int):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f"NAme: {self.name} - Age {self.age}")
    
p = Person()


class StaticMethod:
    
    @staticmethod
    def somma(a: int, b: int):
        return a + b

print(StaticMethod.somma(10, 20))
    