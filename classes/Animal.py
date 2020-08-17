class Animal:
  def __init__(this,legs,diet,name,sound):
    this.legs = legs
    this.diet = diet
    this.name = name
    this.sound = sound


  def growl(this):
    print(f'{this.sound}... I am a {this.name}')

