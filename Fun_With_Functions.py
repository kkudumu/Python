def odd_even():
    for i in range(2001):
        if i % 2 == 0:
            print "Number is {}. This is an even number".format(i)
        else:
             print "Number is {}. This is an odd number".format(i)
odd_even()

a = [2,4,10,16]

def multiply(a):
    for i in xrange(len(a)):
       
        print a[i]*5

print multiply(a)

