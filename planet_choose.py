import ephem as ep
from datetime import datetime as dt

dt1 = dt.today()
print(dt1)
planet_choose = input('Выберите планету: ')
try:
	if planet_choose.lower() == 'mercury':
		print (ep.constellation(ep.Mercury(dt1)))
	elif planet_choose.lower() =='venus':
		print (ep.constellation(ep.Venus(dt1)))
	elif planet_choose.lower() =='earth':
		print (ep.constellation(ep.Earth(dt1)))
	elif planet_choose.lower() =='mars':
		print (ep.constellation(ep.Mars(dt1)))
	elif planet_choose.lower() =='jupiter':
		print (ep.constellation(ep.Jupiter(dt1)))
	elif planet_choose.lower() =='saturn':
		print (ep.constellation(ep.Saturn(dt1)))
	elif planet_choose.lower() =='uranus':
		print (ep.constellation(ep.Uranus(dt1)))
	elif planet_choose.lower() =='neptune':
		print (ep.constellation(ep.Neptune(dt1)))
	elif planet_choose.lower() =='pluto':
		print (ep.constellation(ep.Pluto(dt1)))
	else:
		print ('Нет таких планет')
except:
	print ('Нет таких планет')