from LogicalAgents.wampusworld import generateWorld, createWorld, standartWorld
from LogicalAgents.wampusworld.AgentWrapper import *
from LogicalAgents.wampusworld.game import gameloop

class HumanAgent:
    def __init__(self, world):
        self.world = world

    def nextAction(self, percept):
        print('Percept : ', percept)
        while True:
            ch = input('Choose action : F - forward, L - Turn left, R - Turn right, S - Shoot, G - Grab, C - Climb, M - Map\n')
            if ch.upper() == 'F':
                return Forward()
            elif ch.upper() == 'L':
                return TurnLeft()
            elif ch.upper() == 'R':
                return TurnRight()
            elif ch.upper() == 'S':
                return Shoot()
            elif ch.upper() == 'G':
                return Grab()
            elif ch.upper() == 'C':
                return Climb()
            elif ch.upper() == 'M':
                self.world.print()
            else:
                print('Unknown action :', ch)

def main():
    world = generateWorld((4, 4))

    world = standartWorld()
    agent = HumanAgent(world)
    print('Game Result :', gameloop(world, agent))

if __name__ == '__main__':
    main()
