import time

from src import NOD_euclid
from src import NOD_bust

def test():
    # start = time.time()
    # print "result %s"%(NOD_euclid.euclid_nod(5, 7))
    # end = time.time()
    # euclid_time = (end - start)
    # print euclid_time

    print NOD_euclid.euclid_nod_original(60, 24)

    # start2 = time.time()
    # print(NOD_bust.bust_nod(31415, 14142))
    # end2 = time.time()
    # bust_time = (end2 - start2)
    # print bust_time
    #
    # print(bust_time/euclid_time)

test()
