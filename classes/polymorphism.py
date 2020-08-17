#Just a basic example of polymorphism
class Kitty:
  def __init__(this,name):
    this.name = name

  def speak(this):
    print(f'My name is {this.name} and I am a kitty')

class Doggy:
  def __init__(this,name,spots):
    this.name = name
    this.spots = spots

  def speak(this):
    print(f'My name is {this.name},I have {this.spots} spots, and I am a doggy')


Goose = Kitty('Goose')
Kaia = Doggy('Kaia',12)

def poly(thing):
  thing.speak()

poly(Goose)
#=>My name is Goose and I am a kitty
poly(Kaia)
#=>My name is Kaia,I have 12 many spots, and I am a doggy