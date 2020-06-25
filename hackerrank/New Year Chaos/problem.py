

def minimumBribes(q):
	steps = 0
	actual = len(q)-1
	en = True
	
	while actual > 0:
		#print(q)
		if q[actual] != actual +1:
			if actual >= 0 and actual +1 == q[actual -1]:
				a = q[actual]
				q[actual] = q[actual -1]
				q[actual -1] = a

				steps += 1
				actual -= 1

			elif actual -2 >= 0 and actual +1 == q[actual -2]:
				a = q[actual -2]
				q[actual -2] = q[actual -1]
				q[actual -1]= q[actual]
				q[actual] = a

				steps += 2
				actual -= 1
			else:
				print('Too chaotic')
				en = False
				break
		else:
			actual -= 1
	if en:
		print(steps)

minimumBribes([2, 1, 5, 3, 4]) # 3
minimumBribes([2, 5, 1, 3, 4]) # Too Chaotic
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]) # Too chaotic
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) # 7
minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]) # 4