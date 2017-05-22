# coding:utf-8

def count():
    times = [0]
    def wrapper():
        times[0] += 1
        print "+1s..."
        print "He got %ds.\n" % times[0]
    return wrapper

test = count()
test()
test()
test()