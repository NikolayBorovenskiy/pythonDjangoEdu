def trimmed_text(text, limit):         			#Create a function with arguments 
	#cutText = text
	if len(text) > limit:              			#Condition:If the text doesn't fit in limit
		
		if " " in text[:limit-3]:      			#Condition:if text contains space between words
			originalText = text[:limit-3]       #In variable "originalText" we write text that is included in the limit, but without "..."
			reverseText = originalText[::-1]    #We make the string reversed and store the result in variable "reverseText" 
			if reverseText[0] in ",.!:;?": 		#Condition:if in string "reverseText" the first character includes one of this characters ",.!:;?"
				reverseText = reverseText[1:]   #Check the first character and if it is a sign ",.!:;?", we cut it off 
			findedSpaceNumber = reverseText.find(" ")           #We find the gap in reversed text
			toReverseAgain = reverseText[findedSpaceNumber+1:]  #In variable stores text where we found the gap and to the end of string
			cutText = toReverseAgain[::-1]+ "..."               #Turn the string back and add "..." 
		else:
			cutText = text[:limit-3] + "..."                    #Otherwise in variable "cutText" we write text that is included in the limit and "..."
	else:
		cutText = text                                          #Otherwise we print text
	

	return cutText #Function returns changed cut text

print trimmed_text("Proin eget tortor risus.", 24) #We print the result of the function with given values
print trimmed_text("Proin eget tortor risus.", 23)
print trimmed_text("Proin eget tortor risus.", 6)