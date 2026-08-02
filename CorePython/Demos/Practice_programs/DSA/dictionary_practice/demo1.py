#WAP to print dicationary 

student = {
    "name" : "Hanmant" , 
    "Age" : 24 , 
    "Education" : "CS and IT " , 
    "City" : "pune"
}


print(student)



print(student.get("Age" , "Key is not present in the dictionary ")) #get() function is used to get value from the key  , syntax dictName.get(Key , default value)



print(student.keys())  #keys() method is used to print all keys in the dictionary 
#dict_keys(['name', 'Age', 'Education', 'City'])


print(student.values()) #values() method is used to print all values in the dictionary 
#dict_values(['Hanmant', 24, 'CS and IT ', 'pune'])


print(student.items()) #items() method is used to print all key values pairs in the dictionary 
#dict_items([('name', 'Hanmant'), ('Age', 24), ('Education','CS and IT '), ('City', 'pune')])


#update() method is used to update the values of key in the dictionary
student.update({
    "Education":"MCA" , 
    "City" :"Latur"
})

print(student)



#pop() it is used to removes specific key and returns its value 

age = student.pop("Age")
print(age)

print(student)


#popitems() it is used to removes and returns last inserted key value pair 

print(student.popitem())



