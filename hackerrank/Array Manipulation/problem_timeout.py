def arrayManipulation(n, queries):
	'''	
	Timeout error
	'''
	m = 0
	l = [0 for i in range(n)]
	for q in range(len(queries)):
		for i in range(queries[q][0] -1, queries[q][1]):
			l[i] += queries[q][2]
			m = max(m, l[i])
	return m

print(arrayManipulation(10, [[1, 5, 3],
 					   		[4, 8, 7],
    				   		[6, 9, 1]]))