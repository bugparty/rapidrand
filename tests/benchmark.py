from random import randint
from hashlib import sha1
import datetime
import rapidrand
def entropy(length):
    hex = "".join(chr(randint(0, 255)) for _ in xrange(length))
    return hex


def random_id():
    h = sha1()
    h.update(entropy(20))
    return h.digest()

def random_id2():
    h = sha1()
    h.update(rapidrand.entropy(20))
    return h.digest()

def random_id3():
    h = sha1()
    h.update(rapidrand.entropy2(20))
    return h.digest()

def random_id4():
    h = sha1()
    h.update(rapidrand.genstr(20))
    return h.digest()
def bench(func, iterations):
    begin = datetime.datetime.now()
    for i in range(iterations):
        hex = func()

    end = datetime.datetime.now()
    print('total runing time:', str(end-begin))

ITERATIONS = 200000


if __name__ == '__main__':
    bench(random_id, ITERATIONS)
    bench(random_id2, ITERATIONS)
    bench(random_id3, ITERATIONS)
    bench(random_id4, ITERATIONS)

