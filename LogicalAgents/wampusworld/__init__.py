import random

class Locator:
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, world, position = (1, 1)):
        self.direction = 0
        self.position = position
        self.world = world
    def forwardLocation(self):
        return (self.position[0] + self.DIRECTIONS[self.direction][0],
                self.position[1] + self.DIRECTIONS[self.direction][1])
    def goForward(self):
        newPosition = self.forwardLocation()

        if self.world.isAcceptible(newPosition):
            self.position = newPosition
            return True
        return False
    def turnRight(self):
        self.direction = (self.direction - 1) % len(self.DIRECTIONS)
    def turnLeft(self):
        self.direction = (self.direction + 1) % len(self.DIRECTIONS)
    def clone(self):
        r = Locator(self.world, position=self.position)
        r.direction = self.direction
        return r



class _WampusWorld:
    def __init__(self, size):
        self.size = size;
        self.world = ['-'] * (size[0] * size[1])

    def print(self):
        for rowIdx in range(self.size[0] - 1, -1, -1):
            print (self.world[rowIdx * self.size[0] : rowIdx * self.size[0] + self.size[1]])

    def at(self, pos):
        pos = (pos[0] - 1, pos[1] - 1)

        if pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]:
            return None

        return self.world[pos[0] * self.size[0] + pos[1]]

    def set(self, pos, value):
        pos = (pos[0] - 1, pos[1] - 1)
        self.world[pos[0] * self.size[0] + pos[1]] = value

    def setEmpty(self, pos):
        self.set(pos, '-')

    def setPit(self, pos):
        self.set(pos, 'P')

    def setWampus(self, pos):
        self.set(pos, 'W')

    def setGold(self, pos):
        self.set(pos, 'G')

    def isPit(self, pos):
        return self.at(pos) == 'P'

    def isWampus(self, pos):
        return self.at(pos) == 'W'

    def isGold(self, pos):
        return self.at(pos) == 'G'

    def isAdjPit(self, pos):
        return self.isAdjacent(pos, 'P')

    def isAdjWampus(self, pos):
        return self.isAdjacent(pos, 'W')

    def isAdjGold(self, pos):
        return self.isAdjacent(pos, 'G')

    def grabGold(self, pos):
        if (self.isGold(pos)):
            self.setEmpty(pos)
            return True
        return False

    def killWampus(self, pos):
        if (self.isWampus(pos)):
            self.setEmpty(pos)
            return True
        return False

    def isAcceptible(self, pos):
        return (pos[0] > 0 and pos[0] <= self.size[0] and
                pos[1] > 0 and pos[1] <= self.size[1])

    def isAdjacent(self, pos, symbol):
        if (self.at((pos[0] - 1, pos[1])) == symbol or
            self.at((pos[0],     pos[1] - 1)) == symbol or
            self.at((pos[0],     pos[1] + 1)) == symbol or
            self.at((pos[0] + 1, pos[1])) == symbol):
            return True
        return False

def generateWorld(size):
    w = _WampusWorld(size)
    rooms = size[0] * size[1]
    random.seed()

    wampusPos = 0
    goldPos = 0
    while wampusPos == goldPos:
        wampusPos = random.randint(1, rooms - 1)
        goldPos = random.randint(1, rooms - 1)

    w.setWampus((int(wampusPos / size[0]) + 1, wampusPos % size[1] + 1))
    w.setGold((int(goldPos / size[0]) + 1, goldPos % size[1] + 1))

    for pos in range(1, rooms):
        worldPos = (int(pos / size[0]) + 1, pos % size[1] + 1)
        if not w.isWampus(worldPos) and not w.isGold(worldPos):
            if random.random() <= 0.2:
                w.setPit(worldPos)
    return w

def standartWorld():
    return createWorld((4, 4),  '---P'
                                'WGP-'
                                '----'
                                '--P-')
def createWorld(size, str):
    w = _WampusWorld(size)
    pos = (size[0], 1)

    while len(str) > 0:
        head = str[0].upper()
        str = str[1:]
        if (head == '#'):
            while head != '\n':
                head = str[0]
                str = str[1:]
        elif (head == 'P' or head == 'W' or head == 'G' or head == '-'):
            w.set(pos, head)
            if (pos[1] == size[1]):
                pos = (pos[0] - 1, 1)
            else:
                pos = (pos[0], pos[1] + 1)
            if (pos == (1, size[1])):
                return w