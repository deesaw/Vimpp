cities = ['mumbai','delhi','chennai','Cochin','goa','Mangalore']
numbers = [1,6,8,0,4,5,-4,9,-56,3,-98,56,-34]

print(list(filter(lambda x:True,cities)))
print(list(filter(lambda x:False,cities)))

print(list(filter(lambda x:len(x)>5,cities)))
#filter for positive numbers
print(list(filter(lambda x:x>=0,numbers)))