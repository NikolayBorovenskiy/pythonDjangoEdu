text = "Swedish pop group ABBA, single SOS unique occo both palindromes."
count = 0
text.lower()
for word in text.split():	
	if not word[-1].isalpha():
		word = word [:-1]

	if word == word[::-1]: 
		count += 1
print ("Palindromes = %i \n " % (count))
	
print(word, type(word))


