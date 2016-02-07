text = "Swedish pop group ABBA, single SOS unique occo both palindromes." #We define the string
count = 0    #The variable that counts the number of word's palindromes
text.lower() #Convert string to lower case
for word in text.split():	   #In loop we break a string into words by spaces
	if not word[-1].isalpha(): #Condition: if the last character is not a letter
		word = word [:-1]      #We cut it off

	if word == word[::-1]:     #If a word is read equally in both directions
		count += 1             #Count the number of palindromes
print ("Palindromes = %i \n " % (count))  #Print number of palindromes
	
print(word, type(word))		   #Print palindrome's type 


