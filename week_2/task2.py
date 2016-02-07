def count_holes(value):  #Create a function with argument "value"-integer or string with integer
	if type(value) != int and type(value) != str:
		return "Error!"  #If it is not a string and not a number we output error message 

	counter = 0          #The variable that counts the number of foles
	for i in str(int(value)): #In the loop we go through elements of the string
		if i in "046":        #Condition:if in our string will be 0, 4 or 6
			counter += 1      #We add to the counter 1 and store the result in variable "counter"
		elif i == "8":        #Second condition: if our string will contain 8
			counter += 2      #We increase the counter to 2, because 8 include two holes
	return counter			  #We return the value stored in variable "counter"

print(count_holes('08824'))   #We print the result of the function with given values
#print(count_holes(123))
#print(count_holes('2016'))
