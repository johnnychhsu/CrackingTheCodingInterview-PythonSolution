import time
w = ''
start = time.time()
for i in range(10000):
    w += 'a'
print("Time 1 is " + str(time.time() - start))

w = []
start = time.time()
for i in range(10000):
    w.append('a')
w = ''.join(w)
print("Time 2 is " + str(time.time() - start))
