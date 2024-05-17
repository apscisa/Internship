import pandas as pd 
import requests

def query(table):
    query = f"SELECT * FROM {table}"
    return query

def readAPI(df):
    dfFromAPI = pd.DataFrame()

    for i in range(len(df)):
        name = df.loc[i, "Fruit_Name"]
        apiUrl = f"https://www.fruityvice.com/api/fruit/{name}"
        JSONContent = requests.get(apiUrl).json()
        temp = pd.DataFrame([JSONContent])
        dfFromAPI = pd.concat([dfFromAPI, temp], ignore_index=True)

    return dfFromAPI

def calculateNutritionalValues(grams, position, nutritions, dfWithKeys):
    ingrNutritions = {}
    keys = list(dfWithKeys.keys())[1:]  

    if("Fruit_Id" in nutritions.columns):
        fruitNutritions = nutritions["nutritions"][position]
        for nutrient in keys:
            ingrNutritions[nutrient] = fruitNutritions[nutrient.lower()] * (float(grams) * 0.01)
            
    else:
        for nutrient in keys:
            ingrNutritions[nutrient] = nutritions[nutrient][position] * (float(grams) * 0.01)

    return ingrNutritions

def addSmoothieValues(newSmoothie, ingrNutritions):
    keys = list(newSmoothie.keys())[1:]

    for key in keys:
        newSmoothie[key]=newSmoothie[key]+ingrNutritions[key]

    return newSmoothie

def insertingSmoothies(smoothies, fruits, ingredients):
    finalSmoothies = pd.DataFrame(columns=['Smoothie_Name', 'Fat', 'Carbohydrates', 'Sugar', 'Protein', 'Calories'])
   
    for i in range(len(smoothies)):
         
        newSmoothie = {'Smoothie_Name': '', "Fat":0, 'Carbohydrates':0, 'Sugar':0, 'Protein':0, 'Calories':0}
        newSmoothie["Smoothie_Name"] = smoothies.loc[i, "Smoothie_Name"]
        ingredientsStr = smoothies.loc[i, "Smoothie_Ingredients"]
        ingredientsList = ingredientsStr.split(",")

        for j in range(len(ingredientsList)):
            ingr = ingredientsList[j]
            ingr = ingr.split(":")

            gramsOfIngr = ingr[1][:-1]

            try:
                int(ingr[0])
                for position in range(len(fruits)):
                    if(ingr[0] == fruits["name"][position].lower()):
                        break

                #ingrNutritions = calculate_nutritional_values_from_fruits(gramsOfIngr, k)
                ingrNutritions = calculateNutritionalValues(gramsOfIngr, position, fruits, ingredients)
            except:
                for position in range(len(ingredients)):
                    if(ingr[0] == ingredients["Ingredient"][position].lower()):
                        break

                #ingrNutritions = calculate_nutritional_values(gramsOfIngr, k)
                ingrNutritions = calculateNutritionalValues(gramsOfIngr, position, ingredients, ingredients)

            newSmoothie = addSmoothieValues(newSmoothie, ingrNutritions)
        
        finalSmoothies.loc[len(finalSmoothies)] = newSmoothie

    return finalSmoothies