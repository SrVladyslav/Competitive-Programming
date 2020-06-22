def countingValleys(n, s):
	t = {'D':-1, 'U': 1, 'v': False}
	valleys = 0
	gary = 0
	for i in s:
		gary += t[i]
		if gary < 0:
			t['v'] = True
		elif t['v'] == True:
			t['v'] = False
			valleys += 1
	return valleys


print(countingValleys(8, 'UDDDUDUUUDDDUDUU'))