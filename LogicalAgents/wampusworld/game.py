import sys
from LogicalAgents.wampusworld import AgentWrapper
from LogicalAgents.wampusworld.AgentWrapper import AgentWrapper


class Percept:
    def __init__(self, world, position, scream = False, bump = False):
        self.percept = [False] * 5
        self.percept[3] = bump
        self.percept[4] = scream
        if (world.isAdjWampus(position)):
            self.percept[0] = True
        if (world.isAdjPit(position)):
            self.percept[1] = True
        if (world.isGold(position)):
            self.percept[2] = True

    def isStench(self):
        return self.percept[0]

    def isBreeze(self):
        return self.percept[1]

    def isGlitter(self):
        return self.percept[2]

    def isBump(self):
        return self.percept[3]

    def isScream(self):
        return self.percept[4]

    def _compose(self, name, value):
        if value:
            return name
        else:
            return 'None'

    def __str__(self):
        return '[ %s, %s, %s, %s, %s ]'%(self._compose('Stench', self.isStench()), self._compose('Breeze', self.isBreeze()),
                                                self._compose('Glitter', self.isGlitter()), self._compose('Bump', self.isBump()),
                                                self._compose('Scream', self.isScream()))


def shoot(agent, world):
    arrowLocation = agent.shoot()
    while arrowLocation.goForward():
        if world.killWampus(arrowLocation.position):
            return Percept(world, agent.position(), scream=True)
    return Percept(world, agent.position())

def gameloop(world, agent):
    agent = AgentWrapper(world, agent)
    score = 0
    steps = 0

    percept = Percept(world, agent.position())

    while (steps < 2 ** 32):
        action = agent.nextAction(percept)
        score -= 1
        steps += 1

        if action.isClimb() and agent.canClimb():
            return (score, True)
        elif action.isTurnLeft():
            agent.turnLeft()
            percept = Percept(world, agent.position())
        elif action.isTurnRight():
            agent.turnRight()
            percept = Percept(world, agent.position())
        elif action.isGrab() and world.isGold(agent.position()):
            world.setEmpty(agent.position())
            score += 1000
            percept = Percept(world, agent.position())
        elif action.isShot() and agent.hasArrow():
            score -= 10
            percept = shoot(agent, world)
        elif action.isForward():
            if agent.goForward():
                position = agent.position()
                if world.isPit(position):
                    score -= 1000
                    return (score, False)
                elif world.isWampus(position):
                    score -= 1000
                    return (score, False)
                percept = Percept(world, agent.position())
            else:
                percept = Percept(world, agent.position(), bump=True)
        else:
            print('Unknown action :', action)
        steps += 1

    return (score, True)