var_string = "hApPyHalLOweEn" #We define the string
counting_vowels = 0           #The variable that counts the vowels
#consonants = 0
for i in var_string:          #Create a loop that iterates over all the elements in a row 
	letter = i.lower()        #We make our string insensitive to the register making all letters small
	if letter == "a" or letter == "e" or\
		letter == "i" or letter == "o" or\
		letter == "u":           # Write a condition if the letter is a vowel
			counting_vowels += 1 # Count the number of vowels increasing the value of the counter
	#else:
			#consonants +=1
print("Counting vowels: %i \n " % (counting_vowels)) # Print the result of counting vowels