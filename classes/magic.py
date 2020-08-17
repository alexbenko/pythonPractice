#how to use built in python methods like print on custom objects
class Car():
  speed = 0
  def __init__(this,color,make,model):
    this.color = color
    this.make  = make
    this.model = model

  def __str__(this):
    return f'Your {this.make},{this.model} is {this.color} and is currently going {this.speed} mph'

  def accelerate(this,toGoTo):
    print(f'Accelerating car to {toGoTo},currently going {this.speed} mph...')
    while this.speed < toGoTo:
      this.speed += 1
      print(f'{this.speed} mph...')
    print(f'Accelerated to {toGoTo} !')


volt = Car(color='White',make='Chevorlet',model='Volt')
print(volt)
#=>Your Chevorlet,Volt is White and is currently going 0 mph
volt.accelerate(100)
print(volt)
#=>Your Chevorlet,Volt is White and is currently going 100 mph

