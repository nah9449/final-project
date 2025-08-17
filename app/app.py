# This will tie it all together

print("Welcome to the Cocktail Recipe App")

print("----------------------------------")


import requests
drink_list=""
all_drinks_url="https://www.thecocktaildb.com/api/json/v2/1/filter.php?c=Cocktail"

while True:
    drink_list=input("Would you like a menu? Type Yes or No:").upper()
    print("----------------------------------")
    if drink_list=="YES" or drink_list=="NO":
        break
    else:
        print("That doesn't look right: Please select Yes or No")



if drink_list=="YES":
    print("Here is a list of our popular drinks")
    print("----------------------------------")
    response = requests.get(all_drinks_url)
    popular_drinks = response.json()
    for drink in popular_drinks["drinks"]:
        print(drink["strDrink"])

print("----------------------------------")

print("Please enter a cocktail")

print("----------------------------------")

while True:


   # Selecting a cocktail

    drink_input=""
    selected_drink=""


    while True:
        drink_input = input("What will be your libation: ").upper()

        selected_drink=drink_input.replace(" ","_")

        #Test to see if the selected drink is in the recipe book

        all_drinks_url= "https://www.thecocktaildb.com/api/json/v2/1/filter.php?c=Cocktail"
        all_drinks_upper=""
        all_drinks_list=[]

        response = requests.get(all_drinks_url)
        all_drinks = response.json()


        for drink in all_drinks["drinks"]:
            all_drinks_upper=(drink["strDrink"]).upper()
            all_drinks_list.append(all_drinks_upper)

        if drink_input in all_drinks_list:
            print("----------------------------------")
            print("Good Choice!")
            print("----------------------------------")
            break
        else:
            print("----------------------------------")
            print("I'm sorry. We don't serve that here please select another drink")
            print("----------------------------------")




    #If the drink passes the code will move on to providing the ingredients

    drinks_url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={selected_drink}"


    # Pulling the ingredients and the servings


    response = requests.get(drinks_url)
    drink_ingredients = response.json()

    Ingredient1=drink_ingredients["drinks"][0]["strIngredient1"]
    Ingredient2=drink_ingredients["drinks"][0]["strIngredient2"]
    Ingredient3=drink_ingredients["drinks"][0]["strIngredient3"]
    Ingredient4=drink_ingredients["drinks"][0]["strIngredient4"]
    Ingredient5=drink_ingredients["drinks"][0]["strIngredient5"]
    Ingredient6=drink_ingredients["drinks"][0]["strIngredient6"]
    Ingredient7=drink_ingredients["drinks"][0]["strIngredient7"]
    Ingredient8=drink_ingredients["drinks"][0]["strIngredient8"]
    Ingredient9=drink_ingredients["drinks"][0]["strIngredient9"]
    Ingredient10=drink_ingredients["drinks"][0]["strIngredient10"]
    Ingredient11=drink_ingredients["drinks"][0]["strIngredient11"]
    Ingredient12=drink_ingredients["drinks"][0]["strIngredient12"]

    Measure1=drink_ingredients["drinks"][0]["strMeasure1"]
    Measure2=drink_ingredients["drinks"][0]["strMeasure2"]
    Measure3=drink_ingredients["drinks"][0]["strMeasure3"]
    Measure4=drink_ingredients["drinks"][0]["strMeasure4"]
    Measure5=drink_ingredients["drinks"][0]["strMeasure5"]
    Measure6=drink_ingredients["drinks"][0]["strMeasure6"]
    Measure7=drink_ingredients["drinks"][0]["strMeasure7"]
    Measure8=drink_ingredients["drinks"][0]["strMeasure8"]
    Measure9=drink_ingredients["drinks"][0]["strMeasure9"]
    Measure10=drink_ingredients["drinks"][0]["strMeasure10"]
    Measure11=drink_ingredients["drinks"][0]["strMeasure11"]
    Measure12=drink_ingredients["drinks"][0]["strMeasure12"]

    print("Here is everything you will need:")
    print("----------------------------------")
    print("----------------------------------")

    #If an incredient is not included it will not show in the response
    if Ingredient1!=None:
        print(drink_ingredients["drinks"][0]["strIngredient1"])
        if Measure1!=None:
            print(drink_ingredients["drinks"][0]["strMeasure1"])
        print("----------------------------------")


    if Ingredient2!=None:
        print(drink_ingredients["drinks"][0]["strIngredient2"])
        if Measure2!=None:
            print(drink_ingredients["drinks"][0]["strMeasure2"])
        print("----------------------------------")

    if Ingredient3!=None:
        print(drink_ingredients["drinks"][0]["strIngredient3"])
        if Measure3!=None:
            print(drink_ingredients["drinks"][0]["strMeasure3"])
        print("----------------------------------")

    if Ingredient4!=None:
        print(drink_ingredients["drinks"][0]["strIngredient4"])
        if Measure4!=None:
            print(drink_ingredients["drinks"][0]["strMeasure4"])
        print("----------------------------------")

    if Ingredient5!=None:
        print(drink_ingredients["drinks"][0]["strIngredient5"])
        if Measure5!=None:
            print(drink_ingredients["drinks"][0]["strMeasure5"])
        print("----------------------------------")

    if Ingredient6!=None:
        print(drink_ingredients["drinks"][0]["strIngredient6"])
        if Measure6!=None:
            print(drink_ingredients["drinks"][0]["strMeasure6"])
        print("----------------------------------")

    if Ingredient7!=None:
        print(drink_ingredients["drinks"][0]["strIngredient7"])
        if Measure7!=None:
            print(drink_ingredients["drinks"][0]["strMeasure7"])
        print("----------------------------------")


    if Ingredient8!=None:
        print(drink_ingredients["drinks"][0]["strIngredient8"])
        if Measure8!=None:
            print(drink_ingredients["drinks"][0]["strMeasure8"])
        print("----------------------------------")

    if Ingredient9!=None:
        print(drink_ingredients["drinks"][0]["strIngredient9"])
        if Measure9!=None:
            print(drink_ingredients["drinks"][0]["strMeasure9"])
        print("----------------------------------")

    if Ingredient10!=None:
        print(drink_ingredients["drinks"][0]["strIngredient10"])
        if Measure10!=None:
            print(drink_ingredients["drinks"][0]["strMeasure10"])
        print("----------------------------------")

    if Ingredient11!=None:
        print(drink_ingredients["drinks"][0]["strIngredient11"])
        if Measure11!=None:
            print(drink_ingredients["drinks"][0]["strMeasure11"])
        print("----------------------------------")

    if Ingredient12!=None:
        print(drink_ingredients["drinks"][0]["strIngredient12"])
        if Measure12!=None:
            print(drink_ingredients["drinks"][0]["strMeasure12"])

        print("----------------------------------")


    print("----------------------------------")

    print("Here is how you'll make it:")
    print("----------------------------------")
    print("----------------------------------")

    print(drink_ingredients["drinks"][0]["strInstructions"])

    print("----------------------------------")
    print("----------------------------------")

    print("Cheers!")
    print("----------------------------------")

    another_drink=input("Would you like to make another drink? Type 'Yes' get another reciepe: ").upper()
    print("----------------------------------")
    if another_drink!="YES":
            print("Enjoy!")
            print("----------------------------------")
            break