import sys

sum=0
n=0

#Sum input values in the data.txt file
for num in open('data.txt'):
	sum += float(num)
	n += 1

print sum/n
