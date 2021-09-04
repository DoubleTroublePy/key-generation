#regex  test
from random import randint
file = open('test', 'w+')
for i in range(1000):
    a = randint(0, 100)
    b = randint(0, 100)
    file.write(str(a) + ':' + str(b) + '\n')