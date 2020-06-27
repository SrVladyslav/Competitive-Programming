

def rotLeft(a, d):
	rot = len(a) % d

	b = a[:d]
	a = a[d:]
	[a.append(i) for i in b]
	return a

print(rotLeft([1,2,3,4,5], 4))