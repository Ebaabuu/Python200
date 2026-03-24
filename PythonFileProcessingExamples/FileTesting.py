'''
inFile = open("Cities.txt", "r")
for line in inFile:
    print(line.rstrip())
inFile.close()
'''
#########
'''
filename = input("Which file to display? ")
inFile = open(filename, "r")
data = inFile.read()
inFile.close
print(data)
'''
##########
'''
filename = input("Which file to display? ")
inFile = open(filename, "r")
data = inFile.readlines()
inFile.close

print(data)
print()
for city in data:
    print(city.rstrip())
    # or print(city, end = "")
'''
#########
'''
inFile = open("Numbers.txt", "r")
sum = 0
for line in inFile:
    sum += int(line)
print(f"Sum: {sum}")
inFile.close()
'''
