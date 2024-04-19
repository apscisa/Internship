student = {
    'name' : 'John Doe', 
    'age' : 20, 
    'major' :'Computer Science', 
    'grades': {'marth' : 90, 'science' : 85, 'history' : 88} }

#1. Print the number of key-value pairs.
print("Number of items in the dictionary: ", (len(student)+len(student['grades'])))

#2. Create a list containing only dictionary values.
listOfValues = list(student.values())
print("A list of all the values: ", listOfValues)

#3. Check if the key ‘major’ exists in the dictionary.
print("Key 'major' exists in the dictionary: ", 'major' in student)

#4. Print the age of the student.
print("Age of the student is ", student['age'])

#5. Add a new key named ‘clubs’ to the dictionary, and give it the following list as a value: ["Chess Club", "Debate Team"]
student["clubs"] = ["Chess Club", "Debate Team"]
print("Added clubs: ", student["clubs"] )

#6. Add ‘Advanced Mathematics Team’ to the list assigned to the key ‘clubs’.
student["clubs"].append("Advanced Mathematics Team")
print("Updated student's clubs are ", student["clubs"])

#7. Remove the key ‘clubs’ along with the values assigned to it.
student.popitem()
print("Student after removing clubs: ", student)

#8. Create the following dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

#9. Concatenate the dictionaries to create a new one: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print("Concatenated dictionaries: ", dic1)

#10. In the dictionary generated in the previous task, update the value associated with key ‘1’ to 15.
dic1[1] = 15
print("Updated key 1 to value 15: ", dic1.items())

#11. Calculate the sum of all values in the dictionary.
listDic1 = list(dic1.values())
print("Sum of all the values in the dictionary: ", sum(listDic1))

#12. Calculate the average of all values in the dictionary.
listDic1 = list(dic1.values())
print("average of all the values in the dictionary: ", (sum(listDic1)/len(listDic1)))

