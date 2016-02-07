def hangman(word, letters):  #Create a function with arguments
	
	
	#word.split(" ")
	#for i in range(len(word)):
	#wordCopy = word
	for i in word:            #In the loop we go through elements of the string
		if i not in letters:  #Condition:if the letter is not included in the list "letters"
			word = word.replace(i, " _ ")   #We replace letters in string "word" on the underscore character
	word = word.replace("  ", " ").strip()  #Remove spaces at the beginning and end of the string and we add one space between 2 underscores
	#word = word.strip()
	return word                             #Function returns changed string



print hangman('python', ['a', 'r', 'y', 'i', 'o']) #We print the result of the function with given values





