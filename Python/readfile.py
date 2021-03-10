f=open("C:/Users/deesaw/Desktop/Python/input.txt","r")
for line in f:
	#print(line.rstrip())
	print(line,end="")
f.close()

f=open('input.txt','r')
print(f.read())
f.close()

f=open('input.txt','r')
lines=f.readlines()
print(lines)
f.close()

f=open('input.txt','r')
print(f.read(1))
print(f.read(1))
f.close()

f=open('input.txt','w')
f.write("this is line one")
f.close()

f=open('input.txt','r')
print(f.readline())
print(f.readline())
f.close()

f=open('input.txt','a')
f.write("this is a new line")
f.close()
