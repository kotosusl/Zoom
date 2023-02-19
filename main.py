import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 501, 501
    pygame.display.set_caption('zoom')
    running = True
    screen = pygame.display.set_mode(size)
    coeff = 20
    points = [(float(p.split(';')[0][1:].replace(',', '.')), float(p.split(';')[1][:-1].replace(',', '.'))) for p in
              open('points.txt', 'r').read().split(', ')]
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if coeff + event.y > 0:
                    coeff += event.y
        pygame.draw.polygon(screen, 'white',
                            tuple([(p[0] * coeff + width * 0.5, p[1] * -coeff + width * 0.5) for p in points]), width=1)
        pygame.display.flip()
    pygame.quit()