with open('results.txt') as data:
    contents = data.readlines()
contents = [x.strip() for x in contents]
sum = 0.0
currint = 0.0
for item in contents:
    if (item == ''):
        avg = sum / 30.0
        print(str(avg))
        sum = 0.0
        print('\n')
    elif (item[0].isdigit()):
        sum += float(item)
    else:
        print(item)


