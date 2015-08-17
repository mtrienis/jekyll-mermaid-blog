class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next
    def __str__(self):
        return str(self.cargo)


c = Node("c")
b = Node("b", c)
a = Node("a", b)

print a.__str__()

# a -> b -> c



class Foo:
    myPublicVar = "a"
    __myPrivateVar = "b"
    def __str__(self):
        return str("Public var: "+self.myPublicVar+" Private var: "+self.__myPrivateVar)

foo = Foo()
print foo.myPublicVar
print foo.__myPrivateVar # throws AttributeError
print foo



