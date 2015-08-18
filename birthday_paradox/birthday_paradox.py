#
# In the birthday paradox, we assume that the distribution of birthdays is uniform. 
# However, that might not really be the case. For example, a lot of people are born in September.
# Would the result change if we had istead of the uniform, an accurate distribution of birthdays?
# We use a simulation approach to find out.
#

from random import randint
import numpy as np
k = 23

#Assumes that the birthday data is in the same folder as the script file.
f = open("birthday_data")

day_frequency = []
summ = 0
for i in f:
	day_frequency.append(float(i.split(" ")[1]))
	summ = summ + float(i.split(" ")[1])

for i in range(len(day_frequency)):
	day_frequency[i] = day_frequency[i]/summ

print(len(day_frequency))

pos = 0
for i in range(100000):
	if max(np.random.multinomial(23,day_frequency))>1:
		pos = pos + 1

print(float(pos)/100000)
