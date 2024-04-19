nums = [4, 100, 25, 11, 2, 99, 11]

#Check if the number 100 is included in the list.
print("1. Check if the number 100 is included in the list.")
print(100 in nums)

#Check how many times 11 occurs in the list.
print("2. Check how many times 11 occurs in the list.")
print(nums.count(11))

#Get the sum of all the items in the list


#Print the first and the last elements of the list.
print("4. Print the first and the last elements of the list.")
print(nums[0])
#last = len(nums)-1
print(nums[len(nums)-1])
print(nums[-1])


#Add a new element 200 to the list.
print("9. Add a new element 200 to the list.")
newNum = 200
nums.append(newNum)
print(nums)

#Add two new elements to the updated list: 300 and 400.
print("10. Add two new elements to the updated list: 300 and 400.")
nums.extend((300, 400))
print(nums)

#Remove the first and the last element from the list.
print("11. Remove the first and the last element from the list.")
nums.pop()
print(nums)
nums.pop(0)
print(nums)





