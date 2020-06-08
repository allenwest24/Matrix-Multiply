import math
with open('results.txt') as data:
    contents = data.readlines()
contents = [x.strip() for x in contents]
# You have to enter the arithmetic you found using arithmeticMeanFinder.py previously.
amean = 0.0
sum = 0.0
for item in contents:
    if (item == ''):
        sum /= 30.0
        stddev = math.sqrt(sum)
        print(str(stddev))
        sum = 0.0
        print('\n')
    elif (item[0].isdigit()):
        sum += ((float(item) - amean)**2)
    else:
        print(item)


