class MyList:
    def __init__(self):
        self.lst = []
    
    def aggiungi(self, val: int):
        self.lst.append(val)

    def fing(self, val: int) -> bool:
        return val in self.lst

mylist = MyList()
mylist.aggiungi(10)
print(mylist)
    