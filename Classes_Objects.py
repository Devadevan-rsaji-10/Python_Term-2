class Animal:
  def __init__(self,name,age):
    self.name=name
    self.age=age


  def sound(self,s):
    self.sound=s
    print(self.sound)

dog = Animal("nero","12")
print("Hello",dog.name,"You are",dog.age,"years old.")
dog.sound("bow bow")
