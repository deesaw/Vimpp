f=open("input.txt","r")
def get_word_count(fp):
	return len(fp.read().split())
print(get_word_count(f))
f.close()