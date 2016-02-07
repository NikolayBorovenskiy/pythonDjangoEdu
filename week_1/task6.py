var_string = '1486371' #We define the string
change_string ='' #We define the string twith which we will work
listNumbers = []  #Determine a list of numbers
a = []            #A list of odd numbers
b = []            #A list of even numbers
for i in var_string: #Using a loop pass by string's elements
	listNumbers.append(int(i)) #Add to the end of the list integers
	if int(i) % 2 != 0:        #Condition: if the number is odd
		a.append(int(i))       #Add it to the list a
		
	else:
		b.append(int(i))       #Otherwise to the list b(if the number is even)

a.sort()                       #Sort all list's elements in increasing
b.sort(reverse = True)         #Sort elements descending

q = ''                         #We create two strings to make strings from lists and then we will gather the data in one string
w = ''

for i in range(len(a)):        #In the loop we change integer's data into string type
	a[i] = str(a[i])
for i in range(len(b)):
	b[i] = str(b[i])

change_string = q.join(a) + w.join(b)  #Merge sorted strings into one string

print ("Changed string = %s \n " % (change_string)) #Print the result(sorted string)

