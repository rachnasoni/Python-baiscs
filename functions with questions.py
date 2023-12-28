#Create a function that returns True if a given inequality expression is correct and False otherwise.
def check(p):
    abc=eval(p)
    if abc:
        return True
    else:
      return False


print(check("2 < 7 < 15"))

#Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
def sumDivisibles(X, Y, Z):
    sum = 0

    for i in range(X, Y + 1):
 
        if (i % Z == 0):
            sum += i
 
    return sum

     
X = int(input("Enter value of X ="))
Y = int(input("Enter value of Y ="))
Z = int(input("Enter value of Z ="))
 
print(sumDivisibles(X, Y, Z))

#Create a function that replaces all the vowels in a string with a specified character.
def replaceVowels(str, K):
    vowels = 'AEIOUaeiou'
    for i in vowels:
      str = str.replace(i, K)
    return str

input = "Escape the ordinary"
K = "*"
print("Given String:", input)
print("Given Specified Character:", K)
print("After replacing vowels with the specified character:", replaceVowels(input, K

#Write a function that calculates the factorial of a number recursively.
def factorial(n): 
    if (n==1 or n==0): 
        return 1
    else:     
        return (n * factorial(n - 1)) 
  
num = 6
print("number : ",num)
print("Factorial : ",factorial(num))

#Create a function that computes the hamming distance between two strings.
def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
 
str1 = "drink"
str2 = "drunk"

print(hammingDist(str1, str2))

#Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
def filter_list(l):  
    output = []
    for i in l:  
        if type(i) != str:  
            output.append(i)  
    return output

print(filter_list([44,2199,'a','s',7,68,'j']))

#The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
def reverse(str):
    str = str[::-1]
    return str.swapcase()
reverse('Go for it')

#with middle being everything in between the first and last element.
lst = [1, 2, 3, 4, 5, 6]
lst = first, middle, last

print(first)
print(middle)
print(last)

#Write a function that moves all elements of one type to the end of the list.
def move_end(array, toMove):
    i = 0
    s = len(array) - 1
    while (i < s):
        while (i < s and array[s] == toMove):
            s-=1
  
        if (array[i] == toMove):
            array[i], array[s] = array[s] , array[i]
        i += 1
    return array

arr = ['a', 'a', 'a', 'b']
k = 'a'
ans = move_end(arr, k)
for i in range(len(arr)):
    print(ans[i] ,end= " ")

#Create a function that takes a string and returns a string in which each character is repeated once.
def double(str):
    return ''.join([c+c for c in str])

print(double('String'))

#Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
def reverse(arg=None):
    return not arg if type(arg) == bool else "boolean expected"

print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))

#Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
def layers(n):
    thickness = 0.6
    for _ in range(n):
        thickness *= 2
    return str(thickness / 1000)+'m' # for meters

print(layers(3))
print(layers(4))

#Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string
def index_of_cap(word):
    indices = []
    for i in range(len(word)):
        if word[i].isupper():
             indices.append(i)
    return indices

print(index_of_cap('Pratik'))
print(index_of_cap('eDaBiT'))
print(index_of_cap('eQuINoX'))

#Using list comprehensions, create a function that finds all even numbers from 1 to given num
def find_even_no(n):
    even =[x for x in range(2,n+1) if x % 2 == 0]
    return even

n = int(input('Enter a number : '))
find_even_no(n)

#Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only
def filter_list(lst):
    intlst = []
    for i in lst:
        if type(i) == int:
            intlst.append(i)
    return intlst 

filter_list([1, 2, 'p', 3, 'y', 'b', 4, 7, 9])

#Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself.
def add_index(lst):
    ind = 0
    index = []
    for i in lst:
        index.append(lst.index(i,ind) + i)
        ind+=1
    return index

add_index([1, 2, 3, 4, 5, 6, 7])

#Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth
import math
pi = math.pi
def cone_volume(r, h):
    return round((1 / 3) * pi * r * r * h)

radius = float(input("Enter value of radius= "))
height = float(input("Enter value of height= "))

print( "Volume Of Cone : ", cone_volume(radius, height) )

#Write a function that gives the number of dots with its corresponding triangle number of the sequence.
def triangle(n):
    return n*(n+1)*0.5

n = int(input('Enter the trinalge number :'))
print("The {}th triangle has {} dots ".format(n,int(triangle(n))))

triangle(1)

#Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
def missing_num(lst):
    total = sum([x for x in range(11)])
    sum_of_list = sum(lst)
    return total - sum_of_list

print(missing_num([1, 2, 3, 5, 6, 7, 8, 9, 10]))

