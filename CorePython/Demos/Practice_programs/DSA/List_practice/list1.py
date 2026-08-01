#list methods :
#append(),insert(),remove(),pop(),clear(),index(),count(),sort(),reverse(),copy()

#1 : append() method
#append are used to add element at the end of the list
list1 = [1,2,3,4,5]

list = [10 , 20 , 30 , 40 , 50]

# list.append([6,7,8,9])
# print(list)

#2 : extend
#extend are used to add multiple elements at the end of the list

list.extend([6,7,8,9])
list1.insert(0,0)
print(list1)
print(list)

#3 : insert
#insert are used to add element at the specific index
list3 = [1,2,3,4,5]
list3.insert(0,0)
print(list3)


#4 : remove() method
#remove are used to remove the specific element from the list
#if the element is not present in the list then it will throw an error
list4 = [1,2,3,4,5,6,7,8,9,10]
list4.remove(5)
print(list4) 

#5 : pop() method
#pop are used to remove the element from the specific index
#if the index is not present in the list then it will remove the last element
list5 = [1,2,3,4,5,6,7,8,9,10]
list5.pop(0)
print(list5)



#6 : clear() method
#clear are used to remove all the elements from the list
list6 = [1,2,3,4,5,6,7,8,9,10]
list6.clear()
print(list6)


#7 : index() method
#index are used to find the index of the specific element
list7 = [1,2,3,4,5,6,7,8,9,10]
print(list7.index(5))

#8 : count() method
#count are used to count the number of specific element in the list
list8 = [1,2,3,4,5,6,7,8,9,10]
print(list8.count(5))

#9 : sort() method
#sort are used to sort the list in ascending order
list9 = [1,2,3,4,5,6,7,8,9,10]
list9.sort()
print(list9)

#10 : reverse() method
#reverse are used to reverse the list
list10 = [1 , 2 , 3 , 4, 5, 6 ,7 ]
list10.reverse()
print(list10)

#11 : copy() method
#copy are used to copy the list
list11 = [1,2,3,4,5,6,7,8,9,10]
list12 = list11.copy()
print(list12)





