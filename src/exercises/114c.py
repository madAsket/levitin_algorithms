import time

from src import NOD_euclid
from src import NOD_bust

def test():
    start = time.time()
    print(NOD_euclid.euclid_nod(31415, 14142))
    end = time.time()
    euclid_time = (end - start)
    print euclid_time

    start2 = time.time()
    print(NOD_bust.bust_nod(31415, 14142))
    end2 = time.time()
    bust_time = (end2 - start2)
    print bust_time

    print(bust_time/euclid_time)

test()
