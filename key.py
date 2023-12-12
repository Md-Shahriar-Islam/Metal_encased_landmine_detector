import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))



def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans



def main():
    if getKey('LEFT'):
        print('a is pressed')
    if getKey('RIGHT'):
        print('b is pressed')
    if getKey('UP'):
        print('c is pressed')
    if getKey('DOWN'):
        print('d is pressed')
    if getKey('d'):
        print('d')
    


if __name__ == '__main__':
    init()
    while True:
        main()
