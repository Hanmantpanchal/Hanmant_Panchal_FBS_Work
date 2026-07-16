#convert hours , minutes and seconds into seconds

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))


#perform operation 

total_seconds = hours*3600 + minutes*60 + seconds

#Display the result

print(f'total seconds: {total_seconds}')