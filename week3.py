'''a=int(input("enter lower limit"))
b=int(input("enter upper limit"))
c=int(input("enter divisor"))
d=0
for i in range(a,b+1,c):
    d=d+i
print("the sum of the numbers that are evenly divided by c from the range a, b= ",d)

#
exp=input("enter expression")
def fun(a):
    i=eval(a)
    if i:
        return True
    else:
        return False
print(fun(exp))

#
k="*"
def repvo(s1,a):
    vowels="aeiouAEIOU"
    for i in vowels:
        s1=s1.replace(i,k)
    return s1
st=input("enter statement")
print("after replacing ",repvo(st,k))

#
num= int(input("enter number"))
fact=1
if num<0:
    print("enter valid number")
elif num=1:
    print("factorial=1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is",fact)
    
#or
num= int(input("enter number"))
def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
print("the factorial of ",num,"is",fact(num))

#
def ham(s1,s2):
    i=0
    count=0
    while(i<len(s1)):
        if s1[i]!=s2[i]:
            count=count+1
        i=i+1
    return count
s1= "some string"
s2= "some other string"
print(ham(s1,s2))

#
x=input("enter string")
z=list(x.split(" "))
def filter(l):
    intl=[]
    while len(l)>0:
        if isinstance(l[0],int):
            if(l[0]>0):
                intl.append(l[0])
                l.remove(l[0])
            else:
                l.remove(l[0])
        if isinstance(l[0],str):
            l.remove(l[0])
    return(intl)
    print(intl)
y=filter(z)
print(y)
#
a=input("enter string")
print(a[::-1])

#
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first)
print(middle)
print(last)

#
def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
print(fact(5))
print(fact(4))

#
l =[1,3,'string1',2, 'string2']
l.append(l.pop(l.index('string1')))
print(l)

def double(str):
    outstr = ''
    for char in str:
        outstr = outstr + char + char
    return outstr
s="hello"
print(double(s))

#
boo1=input("enter boolean")
if boo1 == "True":
    print(not boo1)
elif boo1=="False":
    print(not boo1)
else:
    print("boolean expected")
#
s= 'GitHubForAssignment'
upperalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=[]
for i in range(0,len(s)):
    if s[i] in upperalphabets:
        b.append(i)
print("Uppercase elements indices : " + str(b))

#
l=[]
num=int(input("enter num"))
for i in range(2,num+1,2):
    l.append(i)
print(l)

#
def a(l):  
    output = []
    for i in l:  
        if type(i) != str:  
            output.append(i)  
    return output

print(a([1,2,3,'a','b']))

#
def vol(a,b):
    v=0.33*(22/7)*a*a*b
    print(v)
a=int(input("enter radius"))
b=int(input("enter height"))
'''
#


