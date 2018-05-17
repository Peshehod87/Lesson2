n= 0
n1=0
n2 = 0
sum_scores = 0
school_score = [{'school_class':'4a', 'scores':[4,3,2,5,5,2]}, {'school_class':'3a', 'scores':[4,3,2,2,3,5]}]
print (school_score)
for class_room in school_score:
	for scores in class_room['scores']:
		sum_scores +=scores
		n +=1
print ('Средний балл по всей школе: ', float(sum_scores/n), '\n'+'Количество оценок: ', n)

for class_count in school_score:
#	print (class_count)
	for  class_score in class_count['scores']:
		n1 +=class_score
		n2 +=1
	print ('\n', class_count['school_class'], 'Средний балл по классу: ', float(n1/n2))

	#print (class_room.keys())
	#for score in school_score['scores']:
	#	print(score)