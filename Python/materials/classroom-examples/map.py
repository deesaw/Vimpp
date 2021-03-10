cities = ['mumbai','delhi','chennai','Cochin','goa','Mangalore']
print(list(map(len,cities)))

print(list(map(lambda x:x.upper(),cities)))
print(list(map(lambda x:x.capitalize(),cities)))