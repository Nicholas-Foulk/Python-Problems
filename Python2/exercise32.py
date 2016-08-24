the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#number just starts at '0'
for number in the_count:
    print "This is count %d" % number
#fruit just starts at '0'
for fruit in fruits:
    print "A fruit of type: %s" % fruit
  
for i in change:
    print "I got %r" % i
    
elements = []
# so this range has  = 0,1,2,3,4,5
for i in range(0,6):
    print "Adding %d to the list." % i
    elements.append(i)
    
for i in elements:
    print "Element was: %d" % i
    
