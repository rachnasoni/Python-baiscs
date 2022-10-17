#week 1
#Section A Fundamentals of Python
#1)Write a Python program to print “Hello Python”
print("Hello Python")

#2)Write a Python program to do arithmetical operations addition and division..
a=int(input("enter num1"))
b=int(input("enter num2"))
add=a+b
div=a/b
print("addition= ",add,"divisioon= ",div)

#3)Write a Python program to find the area of a triangle.
h=int(input("enter height of triangle"))
b=int(input("enter base lenght "))
area=0.5*h*b
print("area of triangle= ",area)

#4)Write a Python program to swap two variables.
x=input("enter value1")
y=input("enter value2")
z=x
x=y
y=z
print(x,y)

#5)Write a Python program to generate a random number.
import random
r=random.randint(0,5)
print(r)


#SECTION B
#1)Write a Python program to convert kilometers to miles.
k=input("enter km ")
m=k*0.621
print(k,"km is ",m,"miles")

#2)Write a Python program to convert Celsius to Fahrenheit.
c=input("enter temp in c")
f=(c*(9/5))+32
print(c,"C is",f,"F")

#3)Write a Python program to display calendar.
import calendar
yy=2023
mm=5
print(calendar.month(yy,mm))

#4)Write a Python program to solve quadratic equation.
import cmath
a =int(input("enter coeffi of degree 2"))
b =int(input("enter coeffi of degree 1"))
c =int(input("enter constant"))
d = (b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The roots are ',sol1," ",sol2)

#5)Write a Python program to swap two variables without temp variable.
x=3
y=4
x,y=y,x
print(x,y)


#SECTION C
#1)Write a Python Program to Check if a Number is Positive, Negative or Zero.
num=int(input("enter num"))
if num>0:
    print("number is positive")
elif num==0:
    print("number is zero")
else:
    print("number is negative")

#2)Write a Python Program to Check if a Number is Odd or Even.
num=int(input("enter number"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

#3)Write a Python Program to Check Leap Year.
year=int(input("enter year"))
if year%4==0:
    print("it's a leap year")
else:
    print("it's not a lep year")

#4)Write a Python Program to Check Prime Number.
num=int(input("enter num"))
op=False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            op= True
            break
if op:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

#5)Write a Python Program to Print all Prime Numbers in an Interval of 1-10000.
l=[]
for i in range(2,101):
    for j in range(2, i):
        if i % j== 0:
            break
        else:
            l.append(i)
print(l)


#SECTION D
#1)Write a Python Program to Find the Factorial of a Number.
num=int(input("enter num"))
fact=1
for i in range(1,num):
    fact=fact*i
    print(fact)

#2)write a program to display the multiplication table
n=int(input("enter num"))
for i in range(1,11):
    c=num*i
    print(num,"x ",i,"= ",c)

#3)Write a Python Program to Print the Fibonacci sequence.
n=int(input("enter num"))
n1,n2=0,1
count=0
while count,n:
    print(n1,end=", ")
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1

#4)Write a Python Program to Check Armstrong Number.
num=int(input("Enter a number"))
temp=num
sum=0
order=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp=temp//10
if(sum==num):
    print("Above number is armsrong number")
else:
    print("Not a armstrong number")



#5)Write a Python Program to Find Armstrong Number in an Interval.
lowerlim=int(input("Enter lower limit of the range: "))
upperlim=int(input("Enter upper limit of the range: "))
op=[]
nop=[]
for i in range(lowerlim,upperlim+1):
    temp=i
    sum=0
    order=len(str(i))
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp=temp//10
    if(sum==i):
        op.append(i)
    else:
        nop.append(i)
print("Armstrong number in above defined range: ",op)
print("Non armstrong number in above defined range: ",nop)
    

#6)Write a Python Program to Find the Sum of Natural Numbers.
num=int(input("Enter a number "))
sum=0
for i in range(1,num+1):
    sum+=i
print("Sum: ",sum)


#SECTION E
#1)Write a Python Program to find sum of array
arr = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in range (len(arr)):
  sum = sum + arr[i]
print(sum)

#2)Write a Python Program to find largest element in an array
def largest(arr, n):
    arr.sort()
    return arr[n-1]
 
arr = [10, 324, 45, 90, 9808]
n = len(arr)
sol = largest(arr, n)
print("Largest in given array ", sol)

#3)Write a Python Program for array rotation
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

#4)Write a Python Program to Split the array and add the first part to the end
def splitArr(arr, n, k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
          
        arr[n-1] = x

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
  
splitArr(arr, n, position)
  
for i in range(0, n): 
    print(arr[i], end = ' ')


#5)Write a Python Program to check if given array is Monotonic
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
A = [6, 5, 4, 4]
  
print(isMonotonic(A))


#SECTION F
#1)Write a Python program to find sum of elements in list
total = 0

list1 = [11, 5, 17, 18, 23]
 
for ele in range(0, len(list1)):
    total = total + list1[ele]
 
print("Sum of all elements in given list: ", total)

#2)Write a Python program to Multiply all numbers in the list
def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x
    return result
     
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

#3)Write a Python program to find smallest number in a list
list1 = [10, 20, 4, 45, 99]
 
list1.sort()
 
print("Smallest element is:", *list1[:1])

#4)Write a Python program to find largest number in a list
list1 = [10, 20, 4, 45, 99]
 
list1.sort()
 
print("Largest element is:", list1[-1])

#5)Write a Python program to find second largest number in a list
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
# to remove duplicates
list2 = list(set(list1))
 
list2.sort()
 
print("Second largest element is:", list2[-2])

#6)Write a Python program to find N largest elements from a list
l = [1000,298,3579,100,200,-45,900]
n = 4
  
l.sort()
print(l[-n:])

#7)Write a Python program to print even numbers in a list
list1 = [10, 21, 4, 45, 66, 93]
 
for num in list1:
 
    if num % 2 == 0:
        print(num, end=" ")

#8)Write a Python program to print odd numbers in a List
list1 = [10, 21, 4, 45, 66, 93]
 
for num in list1:
     
    if num % 2 != 0:
       print(num, end = " ")

#9)Write a Python program to Remove empty List from List
test_list = [5, 6, [], 3, [], [], 9]
 
print("The original list is : " + str(test_list))
 
while [] in test_list :
    test_list.remove([])
 
print("List after empty list removal : " + str(test_list))

#10)Write a Python program to Cloning or Copying a list
def Cloning(li1):
    li_copy = li1[:]
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#11)Write a Python program to Count occurrences of an element in a list
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))






    


















