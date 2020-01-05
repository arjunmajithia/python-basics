import sys

def printData():
    print(sys.argv)
# first argument of argv is filename

def printSum():
    print(int(sys.argv[1]) + int(sys.argv[2]))

printData()
printSum()

print(sys.version)         # specifies which version of python we are working on
print(sys.path)

print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)