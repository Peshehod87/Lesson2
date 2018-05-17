user_age = input('Введите Ваш возраст: ')
if int(user_age)>21:
	print ('Иди работай!')
elif 17<int(user_age)<=21:
	print ('Учись, студент!')
elif 7<=int(user_age)<=17:
	print ('Иди в школу, школота!')
else:
	print ('Иди отсюда, мальчик')