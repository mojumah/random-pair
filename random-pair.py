import random
import ast
import MySQLdb

#open database connection
db = MySQLdb.connect("localhost","root","dbpassword","santa" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

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
       print "Who santa knows that he/she likes to have a"
       cursor.execute ("SELECT * FROM gifts WHERE NAME = '%s'" % (A))
       for row in cursor.fetchall():
           print row[1]
       print "AND"
       foo.remove(A);
       B = (random.choice(foo));
       print B
       print "Who santa knows that he/she likes to have a"
       cursor.execute ("SELECT * FROM gifts WHERE NAME = '%s'" % (B))
       for row in cursor.fetchall():
           print row[1]
       foo.remove(B);
       print "Exchange gifts"
       y = y - 1
else:
   print("Number of people must be even")
