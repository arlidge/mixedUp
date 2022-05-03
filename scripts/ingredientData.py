import json
import requests
from colorama import colorama_text, Fore, Back, Style

print(Fore.RED+'This will print a description of the searched ingredient'+Fore.RESET)
print(Fore.BLUE+'')

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?i="+ input('Ingredient '))
data = response.json()

for i, item in enumerate(data['ingredients']):
    print(Fore.YELLOW+'----------------------------------------------------------------------------------------------')
    print(Fore.RED+data['ingredients'][i]['strIngredient'])
    print(Fore.GREEN+data['ingredients'][i]['strDescription'])


    print(''+Fore.RESET)
