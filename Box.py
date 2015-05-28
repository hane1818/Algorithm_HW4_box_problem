import sys
from operator import attrgetter


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.plist = list()
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
        other.be_linked += 1


def topo_sort(box):

    # Record every box can be included in which box
    for x in box:
        for y in box:
            if x < y:
                x.link_to(y)

    box = sorted(box, key=attrgetter('be_linked'))

    while True:
        for x in box:
            if x.be_linked == 0:
                x.be_linked = -1
                for y in x.plist:
                    y.max_route = max(y.max_route, x.max_route+1)
                    y.be_linked = y.be_linked - 1

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
    sys.exit()
