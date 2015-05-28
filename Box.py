class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.plist = list()
        self.plength = 0
        self.be_linked = 0

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


def main():
    N = int(input())
    box = list()
    for i in range(N):
        x = input()
        x = x.split(' ')
        x = Box(x[0], x[1], x[2])
        box.append(x)
#    Test:
#    for i, x in enumerate(box):
#        x.print_content()

if __name__ == "__main__":
    main()
