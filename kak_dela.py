def ask_user():
	while True:
		ask = input ('Как дела: ')
		if ask.lower() == 'хорошо':
			return print ('Наконец-то!')
			break

ask_user()