def foobar():
    for i in range(100, 100001):
        printing = all(i%x for x in xrange(2,i))
        root = i**.5
        if root == int(root):
            root=int(root)
        if isinstance(root, int):
            print i,"Bar"
        elif printing == True:
            print i,"Foo"
        else:
            print i,"Foobar"

foobar()