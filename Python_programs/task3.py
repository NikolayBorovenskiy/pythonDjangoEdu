var_string = "hApPyHalLOweEn"
counting_vowels = 0
#consonants = 0
for i in var_string:
	letter = i.lower()
	if letter == "a" or letter == "e" or\
		letter == "i" or letter == "o" or\
		letter == "u":
			counting_vowels += 1
	#else:
			#consonants +=1
print("Counting vowels: %i \n " % (counting_vowels))