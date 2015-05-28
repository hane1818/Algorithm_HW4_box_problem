import sys
from operator import attrgetter


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.plist = list()
        self.plength = 0
        self.be_linked = 0
        self.max_route = 1

    def __lt__(self, other):
        return (self.length < other.length
                and self.width < other.width
                and self.height < other.height)

    def __gt__(self, other):
        return (self.length > other.length
                and self.width > other.width
                and self.height > other.height)

    def link_to(self, other):
        self.plist.append(other)
        self.plength += 1
        other.be_linked += 1

"""
    Test for input:
    def print_content(self):
        print(self.length, self.width, self.height)
"""


def topo_sort(box):

    for i, x in enumerate(box):
        for j, y in enumerate(box):
            if x < y:
                x.link_to(y)

    while True:
        for i, x in enumerate(box):
            if x.be_linked == 0:
                for j, y in enumerate(x.plist):
                    if y.max_route < x.max_route + 1:
                        y.max_route = x.max_route + 1
                    y.be_linked -= 1
                x.be_linked = -1
                print(i, x.max_route)

        if all(b.be_linked == -1 for b in box):
            break

    return max(box, key=attrgetter('max_route')).max_route


def main():
    N = int(input())
    box = list()
    for i in range(N):
        x = input()
        x = x.split(' ')
        x = Box(x[0], x[1], x[2])
        box.append(x)

    MAX_ROUTE = topo_sort(box)
    print(MAX_ROUTE)

if __name__ == "__main__":
    main()
