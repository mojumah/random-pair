import random
import ast
user_input = raw_input("Enter names:")
foo = user_input.split()
x = 0
for name in foo:
   x = x+1
print x  
if (x % 2) == 0:
   print("Good this is an even nunber")
   y = x/2
   while y > 0:
       A = (random.choice(foo));
       print A
       print "AND"
       foo.remove(A);
       B = (random.choice(foo));
       print B
       foo.remove(B);
       print "Exchange gifts"
       y = y - 1
else:
   print("Number of people must be even")
