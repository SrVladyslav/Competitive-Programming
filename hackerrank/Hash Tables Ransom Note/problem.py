
def checkMagazine(magazine, note):
	m = {}
	n = {}
	veredict = 'Yes'
	
	for m1 in magazine.split(' '):
		m[m1] = 1 if m.get(m1) == None else m[m1] + 1

	for n1 in note.split(' '):
		n[n1] = 1 if n.get(n1) == None else n[n1] + 1

	# Equals
	for k in n.keys():
		if n[k] > m.get(k, -1):
			veredict = 'No'
			break
	print(veredict)



checkMagazine('ive got a lovely bunch of coconuts', 'ive got some coconuts') # NO
	
checkMagazine('two times three is not four', 'two times two is four') # NO

checkMagazine('give me one grand today night','give one grand today') # YES