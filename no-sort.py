"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~NO-SORT ALGORITHM~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm is for nearly sorting arrays.
Its potential usage is for speeding-up insertion sort.
I experimented, sorting a list that has been no-sorted first, made insertion
sort 2 times faster.

"""

import sys, random, time
import matplotlib.pyplot as plt

def nearlysort(shuffled):
	size = len(shuffled)
	finish = False
	i = 0
	while (finish == False):
		if (shuffled[i] > shuffled[-(i+1)]):
			swap(shuffled, i, -(i+1))
		i = i+1
		if (i >= size/2):
			finish = True
	if (size <= 2):
		return (shuffled)
	nearlysort(shuffled[0:int(size/2)])
	nearlysort(shuffled[int(size/2):])

def swap (liste, i, j):
	temp = liste[i]
	liste[i] = liste[j]
	liste[j] = temp

size = int(sys.argv[1])

randomList = [random.randint(1,size*3) for _ in range(size)]
plt.plot(randomList)
plt.show()

nearlysort(randomList)
plt.plot(randomList)
plt.show()
