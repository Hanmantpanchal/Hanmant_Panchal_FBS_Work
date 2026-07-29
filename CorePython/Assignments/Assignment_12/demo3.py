#3. Python Program to Detect if Two Strings are Anagrams
def anagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")

str1=input("Enter first string:")
str2=input("Enter second string:")
anagram(str1,str2)
