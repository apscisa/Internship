nums = (4, 100, 25, 11, 2, 99, 11)
print("Tuple: ", nums);

#1. Get the number of elements in the tuple.
print("Number of elements in the tuple is ", len(nums))

#2. Get the smallest number from the tuple.
print("Smallest number from the tuple is ", min(nums))

#3. Get the largest number from the tuple.
print("Smallest number from the tuple is ", max(nums))

#4. Print the first and the last element of the tuple.
print("The first element of the tuple is ", nums[0], ", while the last element is ", nums[-1])

#5. Check if the number 11 exists in the tuple.
print("Element 11 exists in the tuple: ", 11 in nums)

#6. Sort the tuple in ascending order.
#listNums = [2, 4, 11, 11, 25, 99, 100]
#sorted_nums = sorted(listNums)         --metod "sort()" changes the list that its been called upon, it you want to add sorted list to another list use "sorted(list)"
#print(sorted_nums)

listNums = list(nums)
listNums.sort()
print("Tuble sorted in ascending order: ", listNums)

#7. Try to assign 1 to the first element.
numsList = list(nums)
numsList[0]=1
print("Assigning 1 to the first element by turning tuple into a list: ", numsList)

#8. Define the following tuple: (2,2,2) and join it with the first tuple in order to get the result: (4,100,25,11,2,99,11,2,2,2)
newTuple = (2, 2, 2)
resultTuple = nums + newTuple 
print("Joined two tuples: ", resultTuple)

#9. Create a list out of the tuple.
    #already did in 7.