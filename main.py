import pygame
from constants import*


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while pygame.get_init():
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    

if __name__ == "__main__":
    main()

