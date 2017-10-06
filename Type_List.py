leet = [1,'Coding',1,'is',3,'fun.',7]
x = []
y = ""


for i in xrange(len(leet)):
    if isinstance(leet[i], int):
         x.append(leet[i])

    elif isinstance(leet[i], str):
         y+=(leet[i])


print y

if x and y:
    print "mixed"


x = sum(x)

print x


     

