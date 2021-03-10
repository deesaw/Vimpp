def countdown(n):
    while n:
        yield(n)
        n-=1

j=countdown(10)
print(type(j))
for x in countdown(5):
    print(x)
for xx in j:
    print(xx)