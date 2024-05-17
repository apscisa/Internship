import pandas as pd
from functions import query, readAPI, calculateNutritionalValues, insertingSmoothies
from conn import conn

#making of a dataframe that contains an excel file
otherIngredients = pd.read_excel("ETL/Other_ingredients.xlsx")

#reading data from a database
connection = conn('mssql+pyodbc://OMEGA-PC-10663/SmoothieFruit?Trusted_Connection=yes&driver=ODBC Driver 17 for SQL Server')
smoothies = pd.read_sql(query('Smoothies'), con=connection)
fruits = pd.read_sql(query('Fruits'), con=connection)

#reading data from an api and asigning it to a dataframe
allFruits = readAPI(fruits)

#merging dataframes for fruits in one single dataframe 
fruits = fruits.rename(columns={"Fruit_Name":'name'})
finalFruits = pd.merge(fruits[['Fruit_Id', 'name']], allFruits[['name', 'nutritions']], on='name')


finalSmoothies = insertingSmoothies(smoothies, finalFruits, otherIngredients)               
print(finalSmoothies)


#finalSmoothies.to_csv("finalSmoothies.csv", sep=',', index=False, encoding='utf-8')
#finalSmoothies.to_json("finalSmoothies.json")


