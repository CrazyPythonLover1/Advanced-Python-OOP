class PlayerCharacter: 
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')

player1 = PlayerCharacter('Mainul', 24)
player2 = PlayerCharacter('Tommy', 19)

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)