import pygame
import sys

# Pygame starten
pygame.init()

# Fenstergröße
width, height = 800, 590
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kasten bewegen")

# Farben
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Kasten-Eigenschaften
x, y = 100, 100
kasten_breite, kasten_hoehe = 50, 50
geschwindigkeit = 30

# Hauptschleife
running = True
while running:
    pygame.time.delay(30)  # 30 ms Pause = ca. 33 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tasten abfragen
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= geschwindigkeit
    if keys[pygame.K_RIGHT]:
        x += geschwindigkeit
    if keys[pygame.K_UP]:
        y -= geschwindigkeit
    if keys[pygame.K_DOWN]:
        y += geschwindigkeit

    # Bildschirm neu zeichnen
    win.fill(WHITE)
    pygame.draw.rect(win, RED, (x, y, kasten_breite, kasten_hoehe))
    pygame.display.update()

# Beenden
pygame.quit()
sys.exit()