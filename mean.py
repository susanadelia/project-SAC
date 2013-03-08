import sys

sum=0
n=0

#Sum input values in the data.txt file
file_name='data.txt'
for num in open(file_name):
	sum += float(num)
	n += 1

print sum/n
