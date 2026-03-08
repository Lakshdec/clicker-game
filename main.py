import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
score = 0
my_rect = pygame.Rect(100, 100, 50, 50)
font = pygame.font.SysFont("Arial", 32)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if my_rect.collidepoint(event.pos):
                score += 1

    screen.fill((255, 255, 255))
    
    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))
    
    pygame.draw.rect(screen, (255, 0, 0), my_rect)
    pygame.display.flip()

pygame.quit()
