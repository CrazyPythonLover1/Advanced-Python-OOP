class PlayerCharacter: 
  def __init__(self, name):
    self.name = name

  def run(self):
    print('run')

player1 = PlayerCharacter('Mainul')
player2 = PlayerCharacter('Tommy')

print(player1.name)
print(player2.name)