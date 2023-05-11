# class dreptunghi:
#
#     lungime = 0
#     latime = 0
#     def calculare_arie(self):
#         return (f"aria este {self.lungime*self.latime}")
#
# podea = dreptunghi()
# podea.lungime = 20
# podea.latime = 10
#
# print(podea.latime)
# print(podea.calculare_arie())

#2222

# class dreptunghi:
#     def __init__(self, nume, lungime, latime):
#         self.nume = nume
#         self.lungime = lungime
#         self.latime = latime
#     def arie(self):
#         return(self.latime*self.lungime)
#
# podeaua = dreptunghi("podea_code_school", 20, 30)
#
# print(podeaua.arie())

###3  __str__

###The string representation of an object WITHOUT the __str__() function:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1)

# The string representation of an object WITH the __str__() function:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)