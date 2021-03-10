cities = ['mumbai','delhi','chennai','Cochin','goa','Mangalore']
print(sorted(cities))

#sort by length
print(sorted(cities,key = len ))
print(sorted(cities,key = len,reverse=True ))

#sort case insensitive
print(sorted(cities,key = lambda x:x.lower() ))

#sort by ending letter
print(sorted(cities,key = lambda x:x[-1] ))
