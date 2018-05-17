def line_compr(line1,line2):
	if line1==line2:
		print ('1')
	elif len(line1)>len(line2) and line1 != line2 and line2 != 'learn':
		print ('2')
	elif line1 != line2 and line2=='learn':
		print ('3')
	else:
		print('Не было такого условия')

line1 = input('Введите 1 строку: ')
line2 = input('Введите 2 строку: ')

line_compr(line1, line2)