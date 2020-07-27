def farenheightToCelcius(temp):
  return round((temp - 32) * (5/9),2)


farenheight = [99,103,87,84,81]

celcius = [farenheightToCelcius(temp) for temp in farenheight]
print(celcius)