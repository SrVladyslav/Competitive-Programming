

def hourglassSum(arr):
	end = len(arr) - 2
	m = -1e100
	for h in range(end):
		for v in range(end): 
			s = arr[v][h] + arr[v][h+1] + arr[v][h+2] + arr[v+1][h+1] + arr[v+2][h] +arr[v+2][h+1] + arr[v+2][h+2]
			if s > m:
				m = s
	return m


print(hourglassSum([[1, 1, 1, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[1, 1, 1, 0, 0, 0],
			[0, 0, 2, 4, 4, 0],
			[0, 0, 0, 2, 0, 0],
			[0, 0, 1, 2, 4, 0]])) # 19
