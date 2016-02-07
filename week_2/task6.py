
def find_most_frequent(text):             #Create a function with arguments 
	splited_text_without_signs = list()   #Create a list
	splited_text = text.lower().split()   #Splitting lowercase text on words
	temp_variable = ''                    #Create a string
	for i in splited_text:                #Create a loop that will go through the words
		if i[-1] in '!,.?:;-':			  #Condition: if the last letter in the word is '!,.?:;-'
			while i[-1] in '!,.?:;-':     #Condition: while the last word's letter is '!,.?:;-'
				i = i[:-1]				  #We cat the last character off
			splited_text_without_signs.append(i) #We add new word in list
		else:
			splited_text_without_signs.append(i) #We overwrite the word in list "splited_text_without_signs"
	#print splited_text_without_signs
	popular_words = list()						 #Create new list "popular_words "

	for i in splited_text_without_signs:         #In loop we go through the words in list
		if text.lower().count(i) >= 2:			 #Condition: we make text lower case. If the number of repeated words >= 2
			if i not in popular_words:  	     #Condition: if the word is not included in list
				popular_words.append(i)			 #We add the word in list
	popular_words.sort()                         #We sort the list "popular_words" alphabetically
	return popular_words                             #Function returns words which are most often found in the text
print find_most_frequent('Hello, hello, my dear!')   #We print the result of the function with given values
print find_most_frequent('to understand recursion you need first to understand recursion...')