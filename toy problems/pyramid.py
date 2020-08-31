from colorama import init
init()
from colorama import Fore

class Pyramid:
  maxTo = int(input('How many pieces should this pyramid be? : '))
  i = 0
  def __init__(this):
    print('Making Pyramid...')
    this.generate()

  def is_even(this,num):
    return num % 2 == 0

  def is_odd(this,num):
    return num % 3 == 0

  def is_quint(this,num):
    return num % 4 == 0

  def generate(this):
    for this.i in range(this.maxTo):
      row = '*' * (this.i+1)
      if this.is_even(this.i):
        print(Fore.RED + row)
      elif this.is_odd(this.i):
        print(Fore.BLUE + row)
      elif this.is_quint(this.i):
        print(Fore.GREEN + row)
      else:
        print(Fore.YELLOW + row)

    while not this.maxTo == 0:
      this.maxTo = this.maxTo - 1
      row2 = '*' * (this.maxTo)
      if this.is_even(this.maxTo):
        print(Fore.BLUE + row2)
      elif this.is_odd(this.maxTo):
        print(Fore.RED + row2)
      elif this.is_quint(this.maxTo):
        print(Fore.YELLOW + row2)
      else:
        print(Fore.GREEN + row2)

      continue


make = Pyramid()