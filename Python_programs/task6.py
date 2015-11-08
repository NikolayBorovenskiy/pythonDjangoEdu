var_string = '1486371'
change_string =''
listNumbers = []
a = []
b = []
for i in var_string:
	listNumbers.append(int(i))
	if int(i) % 2 != 0:
		a.append(int(i))
		
	else:
		b.append(int(i))

a.sort()
b.sort(reverse = True)

q = ''
w = ''

for i in range(len(a)):
	a[i] = str(a[i])
for i in range(len(b)):
	b[i] = str(b[i])

change_string = q.join(a) + w.join(b)

print ("Changed string = %s \n " % (change_string))

