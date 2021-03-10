lambda a,d:a + d

lambda strs:strs.upper()

cities =['mumbai','delhi','CHennai','Goa']
print(sorted(cities))

#sort by length
print(sorted(cities,key=len))
print(sorted(cities,key=len,reverse=True))

#sort by ending letter
print(sorted(cities,key=lambda x:x.lower()))
print(sorted(cities,key=lambda x:x[-1]))