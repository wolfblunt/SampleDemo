import sys
from Addition import Addition
from Multiply import Multiply
from Division import Division
from Subtract import Subtract

print("Enter the operation to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

try:
    inp = str(sys.argv[1])
    a = int(sys.argv[2])
    b = int(sys.argv[3])
except:
    inp = input()
    a = int(input())
    b = int(input())

if(inp=="1"):
    op = Addition()
elif(inp=="2"):
    op = Subtraction()
elif(inp=="3"):
    op = Division()
elif(inp=="4"):
    op = Multiply()
else:
    print("Wrong input given")
    sys.exit(0)


print(op.operation(a,b))