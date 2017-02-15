class Animal(object):
  def __init__(self, name):
    print 'aniaml!'
    self.health = 100
    self.name = name
  def walk(self):
      self.health -= 1
      print "walking..."
      return self
  def run(self):
      self.health -= 5
      print "running!"
      return self
  def displayHealth(self):
      print self.name
      print "health:" + str(self.health)
      return self

NewAnimal = Animal("Animal1")

NewAnimal.walk().walk().walk().run().run().displayHealth()
#NewAnimal.pet().fly()
class Dog(Animal):
  def __init__(self, name):
      super(Dog, self).__init__(name)
      self.health = 150
  def pet(self):
    self.health += 5
    return self
class Dragon(Animal):
  def __init__(self, name):
      super(Dragon, self).__init__(name)
      self.health = 170
  def displayHealth(self):
    print "This IS a dragon!"
    super(Dragon, self).displayHealth()
  def fly(self):
    self.health -= 10
    return self
Dog("dog1").walk().walk().walk().run().run().pet().displayHealth()
Dragon("redDragon").walk().walk().walk().run().run().fly().fly().displayHealth()
