"""x = int(input("ENTER A NUMBER: "))
y = int(input("ENTER NEXT NUMBER: "))
z = x+y
print(z)
"""
"""
a = input("ENTER A NUMER: ")
b = input("ENTER NEXt NUMBER: ")
c = a+b
print(c)
"""
"""
char = input("ENTER A CHARACTER : ")[2]
print(char)
"""
"""
result = eval(input("ENTER AN EXPRESSION: "))
print(result)
"""
"""
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print("result : " + z)
"""
# if statement
"""
x = 8
if x==8:
    print("THE NUMBER IS EVEN.")
    if(x<5):
        print("THE NUMBER IS SMALL.")
    else:
        print("THE NUMBER IS GREAT.")
else:
    print("THE NUMBER IS ODD.")
"""
# nested if
"""
x = int(input("ENTER A NUMBER: "))
if (x<=100):
    print("THE IS UNDER 100.")
elif(x<=50):
    print("THE IS UNDER 50.")
elif(x<=25):
    print("THE IS UNDER 25.")
else:
    print("THE NUMBER IS OUT OF 100.))")
"""
# while loop
"""
i =1
while i<=10:
    print("AJMAL NK")
    i+=1
"""
"""
i=8
while i>=1:
    print("I AM PYTHON DEVELOPER.")
    i-=1
"""
"""
i=1
j=1
while i<=5:
    print("PYTHON DEVELOPER")
    i+=1
    while j<=5:
        print("AJMAL NK")
        j+=1
"""
# for loop
"""
x = 'ajmal nk'
for i in x:
    print(i)
"""
"""
for i in range(10):
    print(i)

for i in range(2,26,2):
    print(i)

for i in range(26,2,-2):
    print(i)

for i in range(1,11):
    if(i%5!=0):
        print(i)
"""
# break
"""
available = 10
x = int(input("YOU CAN TYPE HOW MANY CANDIES ?: "))
i=1
while i<=x:
    if(i>available):
        print("OUT OF STOCK.")
        break
    print("CANDY")
    i+=1
"""
# continue
"""
for i in range(1,11):
    if i%3==0 or i%5==0:
        continue
    print(i)
"""
# pass
"""
def display():
    pass

print("hello world")
"""
# pattern printing
"""
print("# ",end="")
print("# ",end="")
print("# ",end="")
print("# ",end="")
"""
# next
"""
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()
"""
# for else
"""
num=[12,36,39,38,37,17,28,45,68,95]

for i in num:
    if i%5==0:
        print(i)
        break
else:
    print("NUMBERS NOT FOUND")
"""
# prime or not
"""
n = int(input("ENTER A NUMBER: "))

for i in range(2,n):
    if n%i==0:
        print("NOT PRIME.")
        break
else:
    print("PRIME NUMBER.")
"""












