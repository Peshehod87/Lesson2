def ask_user():
	try: 
		while True:
			ask = input ('Как дела: ')
			if ask.lower() == 'хорошо':
				return print ('Наконец-то!')
				break
	except TypeError:
		print ('Ошибка ввода!')
	except KeyboardInterrupt:
		print ('\n' + 'Кто тут Ctrl+C балуется?!')

ask_user()