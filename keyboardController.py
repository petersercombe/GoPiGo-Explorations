import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((300, 150))
    # Place some text on the display here
    pygame.display.update()

def keyPress(keyName):
    for event in pygame.event.get(): pass # Update latest events
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        return True
    else:
        return False

def main():
    if keyPress('w') and keyPress('s'):
        throttle = 0
    elif keyPress('w'):
        throttle = 1
    elif keyPress('s'):
        throttle = -1
    else: throttle = 0

    if keyPress('j'):
        steering = 0.5
    elif keyPress('k'):
        steering = 1
    elif keyPress('h'):
        steering = -0.5
    elif keyPress('g'):
        steering = -1
    else: steering = 0

    return throttle, steering

