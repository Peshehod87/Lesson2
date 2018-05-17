def ask_user():
	while True:
		ask = input ('Как дела: ')
		if ask.lower() == 'хорошо':
			return print ('Наконец-то!')
			break

def get_answer():
	while True:
		ask_user()
		if ask.lower() == 'хорошо':
			return print ('Наконец-то!')
			break

ask_user()