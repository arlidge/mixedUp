import json
import requests
from colorama import colorama_text, Fore, Back, Style

print(Fore.RED+'This will print cocktail recipes'+Fore.RESET)
print(Fore.CYAN+'Search cocktails by name of alcohol'+Fore.RESET)
print(Fore.BLUE+'')

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ input(' '+Fore.MAGENTA))
data = response.json()

for i, item in enumerate(data['drinks']):
    print(Fore.YELLOW+'----------------------------------------------------------------------------------------------')
    print(Fore.RED+data['drinks'][i]['strDrink'])
    print(''+Fore.RESET)
