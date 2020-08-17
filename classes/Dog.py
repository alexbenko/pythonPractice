from Animal import Animal

class Dog(Animal):
  def __init__(this,legs,diet,name,sound,trick):
    super().__init__(legs,diet,name,sound)
    this.trick = trick

  def doTrick(this):
    print(f'Ta Daa... I Just Did a {this.trick}')


fido = Dog(4,'dog food','Fido','Bark','Backflip')

fido.doTrick()
fido.growl()