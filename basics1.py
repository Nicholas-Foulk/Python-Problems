#!/usr/bin/env python
import math
import os
x=3
y=8
sum=x+y
print(sum)



#a=int(raw_input("Enter a:"))
#b=int(raw_input("Enter b:"))
#sum=a+b
#print(sum)

s="Sup world"
print(s)
print(len(s))

s="The new string"
print(s)
print("The indicy is 0 on the previous string is")
print(s[0])
print("The indiciy is 1 on the string before the previous one")
print(s[1])


d = "Onto modifying strings now"
print(d)

print(d + ' ' + d)
print(d.replace("ARRRR","MATEY"))

d=d.upper()
print(d)
d=d.lower()
print(d)

sent1="The cat is brown"
sent2="The cat is brown"

if sent1==sent2:
	print("strings equal")

if sent1 in sent2:
	print(sent2 + " found in " + sent1)

str1=" OH \n newline amirite? \n another one!"
print(str1)

str5="tabbing\tlabbed\tstabbed\trabbed\n"
print(str5)


l=["one","two","three","four"]
print(l)
print(l[0])
print(l[1])
print(l[2])
print("Sorting the new list")
l.sort()
print(l)

print("Reversing the list")
l.reverse()
print(l)

info=(3,4,3.141579,"Hi everyone")
print(info[0])
print(info[1])
print(info[2])
print(info[3])
print(info)

info=info+(6,7,8,9)
print("added to the tuple")
print(info)

listNumber = [6,3,7,4]
x=tuple(listNumber)
print(x)

x=(4,5)
lister=list(x)
print(lister)

people=("Me","I","Are","Help")
print(people)
print("After Sort of tuple")
people=tuple(sorted(people))
print(people)

words={}
words["Hello"]="Bonjour"
words["Bye"]="Asta La Vista"
print(words["Hello"])
print(words["Bye"])

p=3.412341
u=4.2345435

print("we have p and u defined here")
print("x = "+str(p))
print("y = "+str(u))
print("two more defined variables to add and print, floating point numbers")

k="1234.324231"
o="23.1123"

c=float(k)+float(o)
print(c)
c=45
o=23
if c > o:
	print("c is larger than o")
else:
	print("c isn't larger than o")

def function(e):
	return e*e
print(function(5))

items = [ "Abby","Brenda","Cindy","Diddy" ]
 
for item in items:
    print(item)

for i in range(1,10):
	print(i)
for x in range(1,5):
	for y in range(1,7):
		print("(" + str(x) + "," + str(y) + ")")


