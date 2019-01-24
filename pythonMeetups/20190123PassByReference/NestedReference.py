## Check the visualized memory location of a and b
## https://github.com/YuqingLethe/Python-Algs-Meetups/wiki/Python-Meetups-Presentations 

a=[1, 2, [3]]
b=list(a)
b[2] += [42]









print ("a is: ")
print (a)
print()

print ("b is : ")
print (b)
print()

print ("Does id(a) == id(b) ?")
print (id(a) == id(b))
