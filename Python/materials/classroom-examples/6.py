def get_indices(word,char):
	newlist=[]
	for index,val in enumerate(word):
		if val==char:
			newlist.append(index)
	return newlist

print(get_indices("banana","a") == [1,3,5])