from collections import deque

def jumpingOnClouds(c):
	jumps = deque() 							# O(1)
	d = list(c) 								# O(n)

	i = 0										# O(1)
	while True: 								# O(n-2)
		if i < len(c) - 2 and c[i +2] != 1:		# O(3)
			jumps.append(i +2)					# O(1)
			i += 2								# O(1)
		elif i < len(c) - 1 and c[i +1] != 1:	# O(3)
			jumps.append(i +1)					# O(1)
			i += 1								# O(1)
		else:
			break
	return len(jumps) 							# O(1) 

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])) # 4
print(jumpingOnClouds([0, 0, 0, 0, 1, 0])) # 3
print(jumpingOnClouds([0, 0, 0, 1, 0, 0])) # 3

