from Inheritance.Parent1 import Parent1
from Inheritance.Parent2 import Parent2
from Inheritance.GrandParent import GrandParent

class Child(Parent1, Parent2): 
    Cname='Child'
    def __init__(self,name):
        self.Cname=name


'''Example of static calling'''
print('Calling the class members as static:\n')
print(GrandParent.GPname,' => Here value is not changed because calling as static')
print(Parent1.P1name,' => Here value is not changed because calling as static')
print(Parent2.P2name,' => Here value is not changed because calling as static')
print(Child.Cname,' => Here value is not changed because calling as static\n')


'''Example of class instance calling'''
print('calling the class members as instances of the class:\n')
GP=GrandParent('GP')
P1=Parent1('P1')
P2=Parent2('P2')

print(GP.GPname,' => Here values are changed because instantiated dynamically')
print(P1.P1name,' => Here values are changed because instantiated dynamically')
print(P2.P2name,' => Here values are changed because instantiated dynamically\n')


'''Example of simple inheritance'''
print('calling inherited members directly:\n')
C=Child('CH')

print(C.GPname,' => Here value is not changed because not instantiated dynamically')
print(C.P1name,' => Here value is not changed because not instantiated dynamically')
print(C.P2name,' => Here value is not changed because not instantiated dynamically')
print(C.Cname,' => Here value is changed because instantiated dynamically\n')


'''Example of inheritance + polymorphism'''
print('calling inherited members as instance of child class instance:\n')
C=GrandParent('GP')
print(C.GPname," => Here values are changed because instantiated dynamically")

C=Parent1('P1')
print(C.P1name," => Here values are changed because instantiated dynamically")

C=Parent2('P2')
print(C.P2name," => Here values are changed because instantiated dynamically")