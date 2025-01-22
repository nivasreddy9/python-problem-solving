# 1st one
bill=int(input("enter the bill: "))
while(bill>0):
    if(bill<100):
        print(bill*5+50)
        break
    elif (bill <200 and bill >100):
        print(bill*7+50)
        break
    else:
        print(bill*10+5)
        break
    
# 2nd 
num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
num3=int(input("enter the number: "))

if(num1>num2 and num3):
    print(num2)
elif(num2>num1 and num3):
    print(num2)
else:
    print(num3)
 
# 3rd
num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
num3=input("press 1 for add,press 2 for sub , press 3 for mul,press 4 for div and press enter")
num4=int(input("enter num for requird operation: "))
if(num4==1):
    print(num1+num2)
elif(num4==2):
    print(num1-num2)
elif(num4==3):
    print(num1*num2)
else:
    print(num1/num2)
    

# factorial 4th
def factorial_iterative(n):
    if n < 0:
        return "Factorial not for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  

# 5th
n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 6th

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "fizzbuzz")
    elif i % 3 == 0:
        print(i, "fizz")
    elif i % 5 == 0:
        print(i, "buzz")
        
# 7th
num1=int(input("enter the number: "))
for i in range(1,num1+1):
    if(num1 % i == 0):
        print("the divisors are ", i)

#8th
num1 = int(input("Enter the number: "))

res = 0 
while num1 > 0:
    rev = num1 % 10  
    count=+rev
    res = res * 10 + rev  
   
    num1 = num1 // 10  

print("Reversed Number:", res)
print(count)

    

































    
