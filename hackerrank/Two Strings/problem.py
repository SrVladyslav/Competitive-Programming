
def twoStrings(s1, s2):
	d = {
		1:{},
		2:{}
	}

	for l in s1:
		d[1][l] = True

	for l in s2:
		d[2][l] = True


	if len(d[1]) > len(d[2]):
		keys = d[2].keys()
		s = 1
	else:
		keys = d[1].keys()
		s = 2

	for k in keys:
		if d[s].get(k):
			return 'YES'
	return 'NO'

print(twoStrings('hello', 'world')) # YES

print(twoStrings('hi', 'world')) #NO