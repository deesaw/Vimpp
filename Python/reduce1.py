from functools import reduce
numbers = [1,6,8,3,4,5,-4,9,-56,3,-98,56,-34]
print(reduce(lambda x,y:x+y,numbers))

print(reduce(lambda x,y:x*y,numbers))

a='\\t'
cities = ['mumbai','delhi','chennai','Cochin','goa','Mangalore']

print(reduce(lambda x,y:x+y,map(len,cities)))