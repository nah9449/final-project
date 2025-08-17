# Test to ensure the reciepe response includes the main ingredient

main_ingredient="Tequila"
ingredient_list=[]

test_drink="Margarita"

test_drinks_url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={test_drink}"

response = requests.get(test_drinks_url)
drink_test_pull = response.json()

ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient1"])
ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient2"])
ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient3"])
ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient4"])
ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient5"])
ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient6"])
ingredient_list.append(drink_test_pull["drinks"][0]["strIngredient7"])

assert main_ingredient in ingredient_list
print('Test Passed')


# test to ensure the correct drink is pulled

test_drink="Margarita"

test_drinks_url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={test_drink}"

response = requests.get(test_drinks_url)
drink_test_pull = response.json()

assert test_drink == drink_test_pull["drinks"][0]["strDrink"]
print('Test Passed')