import requests as r

getSquirtle = r.get("https://pokeapi.co/api/v2/pokemon/squirtle")

print(getSquirtle.text)