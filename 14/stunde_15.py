 class Person:
         age: 0
         name: ""

         def __init__(self, name, age):
             self.name = name
             self.age = age

         def get_name(self):
             return self.name

         def get_age(self):
             return self.age

         def set_age(self, age):
             self.age = age

         def toString(self):
             return "name: " + self.name + ", age: " + str(self.age)
class Person:
   age: 0
   name: ""

   def __init__(self, name, age):
      self.name = name
      self.age = age

   def get_name(self):
      return self.name

   def get_age(self):
      return self.age

   def set_age(self, age):
      self.age = age

   def toString(self):
      return "name: " + self.name + ", age: " + str(self.age)
