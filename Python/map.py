cities = ['mumbai','delhi','chennai','Cochin','goa','Mangalore']
print(list(map(len,cities)))

print(list(map(lambda x:x.upper(),cities)))
print(list(map(lambda x:x.capitalize(),cities)))
print(list(map(lambda x:x[::-1],cities)))

numbers = [1,6,8,0,4,5,-4,9,-56,3,-98,56,-34]

#double the numbers

print(list(map(lambda x:2*x , numbers)))

print(list(map(lambda x:x*x , numbers)))
print(filter(lambda x:True,cities))

print(filter(lambda x:True,cities))

print(list(filter(lambda x:True,cities)))
print(filter(lambda x:True,cities))