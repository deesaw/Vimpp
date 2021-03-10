f=open('input.txt','r')

for x in map(lambda x:x.upper(),f):
    print(x.rstrip())
f.close()
"""way 2"""
f=open('input.txt','r')

for x in map(str.upper,f):
    print(x.rstrip())
f.close()

