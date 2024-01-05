class Animal:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def sound(self,s):
    self.sound=s
    print(self.sound)

dog = Animal("nero","12")
dog.sound("bow bow")
