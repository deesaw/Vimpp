import time

start = time.time()
for x in range(1000000):
	y=x*x
end = time.time()
print(end - start)

print(time.time())
time.sleep(1) # sleep for a second

a = 1574148191.871922
print(time.ctime(a))