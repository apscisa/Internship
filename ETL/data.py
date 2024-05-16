import pandas as pd
import requests
import json


#making of a dataframe that contains an excel file
otherIngredients = pd.read_excel("Other_ingredients.xlsx")

#reading data from a database
from sqlalchemy import create_engine

engine = create_engine('mssql+pyodbc://OMEGA-PC-10663/SmoothieFruit?Trusted_Connection=yes&driver=ODBC Driver 17 for SQL Server')
connection = engine.connect()

def query(table):
    query = f"SELECT * FROM {table}"
    return query

smoothies = pd.read_sql(query('Smoothies'), con=connection)
fruits = pd.read_sql(query('Fruits'), con=connection)

#reading a data from an api and asigning it to a dataframe
allFruits = pd.DataFrame()
for i in range(len(fruits)):
    name = fruits.loc[i, "Fruit_Name"]
    apiUrl = f"https://www.fruityvice.com/api/fruit/{name}"
    JSONContent = requests.get(apiUrl).json()
    temp = pd.DataFrame([JSONContent])
    allFruits = pd.concat([allFruits, temp], ignore_index=True)


#merging dataframes for fruits in one single dataframe 
fruits = fruits.rename(columns={"Fruit_Name":'name'})
finalFruits = pd.merge(fruits[['Fruit_Id', 'name']], allFruits[['name', 'nutritions']], on='name')

#print(otherIngredients)

print(finalFruits)

finalSmoothies = pd.DataFrame(columns=['Smoothie_Name', 'Fat', 'Carbohydrates', 'Sugar', 'Protein', 'Calories'])

def calculate_nutritional_values(grams, ingredients_data, k=None):
    ingr_nutritions = {}
    if k is not None:
        for nutrient, value in ingredients_data.items():
            ingr_nutritions[nutrient] = value[k] * (float(grams) * 0.01)
    else:
        keys = list(ingredients_data.keys())[1:]
        for nutrient in keys:
            ingr_nutritions[nutrient] = ingredients_data[nutrient] * (float(grams) * 0.01)
    return ingr_nutritions

print(smoothies)
print(otherIngredients)


def calculate_nutritional_values(grams, k):
    ingrNutritions = {}
    keys = list(otherIngredients.keys())[1:]  
    for nutrient in keys:
        ingrNutritions[nutrient] = otherIngredients[nutrient][k] * (float(grams) * 0.01)
    return ingrNutritions

print(calculate_nutritional_values(10, 10))

def calculate_nutritional_values_from_fruits(grams_of_ingr, k):
    ingrNutritions = {}
    keys = list(otherIngredients.keys())[1:]
    fruitNutritions = finalFruits["nutritions"][k]
    for nutrient in keys:
        ingrNutritions[nutrient] = fruitNutritions[nutrient.lower()] * (float(grams_of_ingr) * 0.01)
    return ingrNutritions


def insertingSmoothies():
   
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
                for k in range(len(finalFruits)):
                    if(ingr[0] == finalFruits["name"][k].lower()):
                        break

                ingrNutritions = calculate_nutritional_values_from_fruits(gramsOfIngr, k)
            except:
                for k in range(len(otherIngredients)):
                    if(ingr[0] == otherIngredients["Ingredient"][k].lower()):
                        break

                ingrNutritions = calculate_nutritional_values(gramsOfIngr, k)


            newSmoothie["Fat"] = newSmoothie['Fat']+ingrNutritions['Fat']
            newSmoothie["Carbohydrates"] = newSmoothie['Carbohydrates']+ingrNutritions['Carbohydrates']
            newSmoothie["Sugar"] = newSmoothie['Sugar']+ingrNutritions['Sugar']
            newSmoothie["Protein"] = newSmoothie['Protein']+ingrNutritions['Protein']
            newSmoothie["Calories"] = newSmoothie['Calories']+ingrNutritions['Calories']

        finalSmoothies.loc[len(finalSmoothies)] = newSmoothie
    print(finalSmoothies)
                    

insertingSmoothies()


#finalSmoothies.to_csv("finalSmoothies.csv", sep=',', index=False, encoding='utf-8')
#finalSmoothies.to_json("finalSmoothies.json")


