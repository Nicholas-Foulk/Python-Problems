i = 0
numbers = [] 

while i<6:
    print "At the top i is %d" % i
    numbers.append(i)
    #this loop will never append 6, because once i is iterated to 6
    #the loop wont meet the condition once it reaches the top again
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
    
