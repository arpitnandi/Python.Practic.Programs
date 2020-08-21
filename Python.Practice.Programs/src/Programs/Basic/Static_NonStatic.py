class Static_NonStatic_1:
 
    static="Static"
    nonStatic="NonStatic"
 
    def __init__(self, nonStatic, static):
        self.nonStatic=nonStatic
        self.static=static


class Static_NonStatic_2:
    
    static="Static"
    nonStatic="NonStatic"
    
    def __init__(self, nonStatic, static):
        self.nonStatic=nonStatic
        self.static=static

    
Obj1=Static_NonStatic_1("NST11","ST11")
Obj2=Static_NonStatic_1("NST21","ST21")
 
print(Static_NonStatic_1.static)
print(Static_NonStatic_1.nonStatic)
print(Obj1.static)
print(Obj1.nonStatic)
print(Obj2.static)
print(Obj2.nonStatic,'\n')

    
Obj1=Static_NonStatic_2("NST12","ST12")
Obj2=Static_NonStatic_2("NST22","ST22")

print(Static_NonStatic_2.static)
print(Static_NonStatic_2.nonStatic)
print(Obj1.static)
print(Obj1.nonStatic)
print(Obj2.static)
print(Obj2.nonStatic)