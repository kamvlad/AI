from LogicalAgents.wampusworld import Locator

class AgentWrapper:
    def __init__(self, world, agent):
        self.location = Locator(world)
        self.agent = agent
        self.arrow = True

    def nextAction(self, percept):
        return self.agent.nextAction(percept)

    def turnRight(self):
        self.location.turnRight()

    def turnLeft(self):
        self.location.turnLeft()

    def goForward(self):
        return self.location.goForward()

    def position(self):
        return self.location.position

    def hasArrow(self):
        return self.arrow

    def shoot(self):
        self.arrow = False
        return self.location.clone()

    def canClimb(self):
        return self.location.position == (1, 1)

class Action:
    FORWARD = 0
    TURNLEFT = 1
    TURNRIGHT = 2
    SHOOT = 3
    CLIMB = 4
    GRAB = 5

    def __init__(self, action):
        self.action = action
    def isForward(self):
        return self.action == self.FORWARD
    def isTurnLeft(self):
        return self.action == self.TURNLEFT
    def isTurnRight(self):
        return self.action == self.TURNRIGHT
    def isShot(self):
        return self.action == self.SHOOT
    def isClimb(self):
        return self.action == self.CLIMB
    def isGrab(self):
        return self.action == self.GRAB

class Forward(Action):
    def __init__(self):
        super(Forward, self).__init__(self.FORWARD)

class TurnLeft(Action):
    def __init__(self):
        super(TurnLeft, self).__init__(self.TURNLEFT)

class TurnRight(Action):
    def __init__(self):
        super(TurnRight, self).__init__(self.TURNRIGHT)

class Shoot(Action):
    def __init__(self):
        super(Shoot, self).__init__(self.SHOOT)

class Climb(Action):
    def __init__(self):
        super(Climb, self).__init__(self.CLIMB)

class Grab(Action):
    def __init__(self):
        super(Grab, self).__init__(self.GRAB)
