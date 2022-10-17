# WEEK 2
# SECTION A
#1
def s_um(a,b,c):
 if a==b or b==c or c==a:
   sum=3
 else:
   sum=3
 return sum
print(s_um(2,6,7))
print(s_um(3,5,1))

#2
def D(dict):
    dict = {'Switej':16, 'Aman':67, 'Chetan':25, 'Vishal':45}
    list = [(k, v) for k, v in dict.items()]

    list.sort(key = lambda x: x[0])
    return list

print(D(dict))

#3
def replaceVowels(str, K):
    vowels = 'aeiou'
    for i in vowels:
        str = str.replace(i, K)
    return str

input_str = "why am I even here"
K = "i"

print("Input string =", input_str)
print("Specified vowel =", K)
print("After replacing =", replaceVowels(input_str, K))

#4
#def function3(str):
str1 = "karlo yaar ye bhi"
z = list(str1)
print(z)
go = []
for i in z:
    go.extend(ord(num) for num in i)
print(go)


odd = []
even = []
for i in go:
    if(i % 2 ==0):
        even.append(i)
    else:
        odd.append(i)

#5
def yeah(st):
  res = []
  for index, c in enumerate(st):
    if index % 2 == 0:
      res.append(c.upper())
    else:
      res.append(c.lower())
  return '' .join(res)
print(yeah("insert some quote or dialogue")

# SECTION B
#1
def factorial(n):
     
    
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 

num = 9;
print("Factorial of",num,"is",
factorial(num))

#2
def myfunction():
    print("Escape the ordinary")
myfunction()

#3

def largest_num( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(largest_num([45, 18, 77, 16]))

#4

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(29))

#5
def is_even_num(l):
    evennum = []
    for n in l:
        if n % 2 == 0:
            evennum.append(n)
    return evennum
print(is_even_num([14, 23, 37, 45, 53, 68, 79, 80, 97]))


