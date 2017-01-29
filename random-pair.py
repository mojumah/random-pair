import random
import ast
user_input = raw_input("Enter eight names separated by space:")
foo = user_input.split()
#print foo
A = (random.choice(foo));
print A
print "AND"
foo.remove(A);
#print foo
B = (random.choice(foo));
print B
print "Exchange gifts"
print "_________________________"
foo.remove(B);
#print foo
C = (random.choice(foo));
print C
print "AND"
foo.remove(C);
#print foo
D = (random.choice(foo));
print D
print "Exchange gifts"
print "_________________________"
foo.remove(D);
E = (random.choice(foo));
print E
print "AND"
foo.remove(E);
#print foo
F = (random.choice(foo));
print F
print "Exchange gifts"
foo.remove(F);
print "__________________________"
G = (random.choice(foo));
print G
print "AND"
foo.remove(G);
#print foo
H = (random.choice(foo));
print H
print "Exchange gifts"
foo.remove(H);
