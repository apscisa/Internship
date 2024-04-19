fruits = {"apple", "banana", "lemon", "orange"}
print("Assigned set: ", fruits)

#1. Check if “banana” is NOT present in the set.
print("'Banana' is not in the set: ", not("banana" in fruits) )

#2. Add “pineapple” to the set.
fruits.add("pineapple")
print("'pineapple' added to the set: ", fruits )

#3. Create the set: {“strawberry”, “blackberry”} and join it with the first set in order to get the result: {"apple", "banana", "lemon", “orange”, “strawberry”, “blackberry”}
newSet = {"strawberry", "blackberry"}
fruits.update(newSet)
print("'fruits' set updated with the new set: ", fruits)

#4. Remove “apple” from the set.
#fruits.discard("apple")            --pretty much the same but discard doesnt return an error when you insert an element that doesnt exist
fruits.remove("apple")
print("'apple' removed from the set: ", fruits)

#5. Print the first element of the set.
#                                   --will always return a different value bacause the order is never defined in a set
fruitsList = list(fruits) 
print("The first element of fruits set is: ", fruitsList[0])
