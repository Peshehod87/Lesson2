n=0
n1=0
names = ["Вася", "Маша", "Петя", 'Коля', 'Гельмут', 'Ганс', "Валера", "Саша", "Даша"]
while names[n] != 'Валера':
	#if n == 'Валера':
	#	n.pop()
	#	print ('Валера нашелся!')
	#else:
	n +=1
	print (names[n], 'Это не Валера!')
print (names[n], " - Валера нашелся!", '| Номер в списке: ', n)