def arrayManipulation(n, queries):
	m = -2**32
	# We will use it to calculate
	data = [0] * n

	for a, b, k in queries:
		# Adding the k at the start
		data[a-1] += k

		# Now we must quit k but in the position+ 1, so it can overfit,
		if b < n:
			data[b] -= k

	# Let's find the maximum 
	total = 0
	for i in range(n):
		total += data[i]

		m = max(m, total)
	return m

print(arrayManipulation(10, [[1, 5, 3],
 					   		[4, 8, 7],
    				   		[6, 9, 1]]))

print(arrayManipulation(5, [[1, 2, 100],
 					   		[2, 5, 100],
    				   		[3, 4, 100]]))