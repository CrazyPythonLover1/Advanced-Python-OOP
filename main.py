class PlayerCharacter: 
  # Class Object Attribute
  membership = True
  def __init__(self, name, age):
    self.name = name # Attribute
    self.age = age

  # Method
  def run(self):
    print(f'{self.name} run fast')

  @classmethod
  def cls_method(cls, param1, param2):
    #Code 
    return
  @staticmethod
  def stc_method(param1, param2):
    #Code
    return


player1 = PlayerCharacter('Mainul', 24)
player2 = PlayerCharacter('Tommy', 19)

print(player1.run())
print(player1.membership)
print(player2.name)
print(player1.age)
print(player2.age)