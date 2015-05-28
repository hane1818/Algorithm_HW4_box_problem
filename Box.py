class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.plist = list()


def main():
    N = input()
    box = list()
    for i in range(N):
        x = input()
        x = x.split('')
        b = Box(x[0], x[1], x[2])
        box.append(b)

if __name__ == "__main__":
    main()
