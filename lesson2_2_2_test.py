names = ["Вася", "Маша", "Петя", 'Коля', 'Гельмут', 'Ганс', "Валера", "Саша", "Даша"]
n1 = 0
def search_names (name1):
	n1=0
	while n1<len(names):
		if name1.lower() not in names[n1].lower():
			pass
			#print (names[n1], ' - Это не: ', name1)
		if names[n1].lower() == name1.lower():
				print (names[n1], ' НАЙДЕН!', '\n', 'Его номер: ', n1+1)
				break
		n1 +=1
		#print ('Такого имени нет в списке!')
name2 = input('Введите имя для поиска: ')
search_names(name2)