with open('results.txt') as data:
    contents = data.readlines()
contents = [x.strip() for x in contents]
geosum = 1.0
currint = 0.0
for item in contents:
    if (item == ''):
        avg = geosum**(1/30.0)
        print(str(avg))
        geosum = 1.0
        print('\n')
    elif (item[0].isdigit()):
        geosum *= float(item)
    else:
        print(item)


