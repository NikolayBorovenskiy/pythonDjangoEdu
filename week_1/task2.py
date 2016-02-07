original_string = "123456 7 890 abc"  #We define the string
change_string= ''                     #We define new string
for i in range(len(original_string)): #In loop we go through all the elements of the string
	change_string+=original_string[i] #Transform original string in changed string

print change_string[2::3] #We output every third symbol of the string into the console