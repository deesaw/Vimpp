a=[1,2,3,4,5,6]
[x*x for x in range(10)]

city=['delhi','Mumbai']
[x.upper() for x in city]

[len(x) for x in city]

[x.capitalize() for x in city[::-1]]

numbers=[1,2,3,0,-1,-2,-4]

from math import sin
[sin(x) for x in numbers]
[x*x for x in numbers if x%2==1]
[x.upper() for x in city if len(x)>4]
[x:x*x for x in numbers]
{ci:len(ci) for ci in city }
{ci:(len(ci),ci.upper(),ci.lower(),ci.capitalize()) for ci in city }