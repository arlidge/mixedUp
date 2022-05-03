import json
import requests
from colorama import colorama_text, Fore, Back, Style

print(Fore.RED+'This will print cocktail recipes'+Fore.RESET)
print(Fore.BLUE+'')

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f="+ input('Search by Letter '))
data = response.json()

for i, item in enumerate(data['drinks']):
    print(Fore.YELLOW+'----------------------------------------------------------------------------------------------')
    print(Fore.RED+data['drinks'][i]['strDrink'])
    print(Fore.BLUE+data['drinks'][i]['strCategory'])
    print(Fore.GREEN+data['drinks'][i]['strGlass'])
    print(data['drinks'][i]['strMeasure1'],'',data['drinks'][i]['strIngredient1'])
    print(data['drinks'][i]['strMeasure2'],'',data['drinks'][i]['strIngredient2'])
    print(data['drinks'][i]['strMeasure3'],'',data['drinks'][i]['strIngredient3'])
    print(data['drinks'][i]['strMeasure4'],'',data['drinks'][i]['strIngredient4'])
    print(data['drinks'][i]['strMeasure5'],'',data['drinks'][i]['strIngredient5'])
    print(data['drinks'][i]['strMeasure6'],'',data['drinks'][i]['strIngredient6'])
    print(data['drinks'][i]['strMeasure7'],'',data['drinks'][i]['strIngredient7'])
    print(data['drinks'][i]['strMeasure8'],'',data['drinks'][i]['strIngredient8'])
    print(data['drinks'][i]['strMeasure9'],'',data['drinks'][i]['strIngredient9'])
    print(data['drinks'][i]['strMeasure10'],'',data['drinks'][i]['strIngredient10'])
    print('')
    print(Fore.MAGENTA+data['drinks'][i]['strInstructions'])
    print(''+Fore.RESET)
