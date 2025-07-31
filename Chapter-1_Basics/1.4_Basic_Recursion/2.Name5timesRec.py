"""
How did this worked?

Name_rec(1) -> Name_rec(2) -> Name_rec(3) -> Name_rec(4) -> Name_rec(5)

Till 5 it went on increasing but as soons as i became 6
it stopped due to our base case i.e. i == 6.
"""


def Name_rec(i=1):
    if i == 6:
        return
    print(f"Name {i} times. ")
    i += 1
    Name_rec()


Name_rec()
