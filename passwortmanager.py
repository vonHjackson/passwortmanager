import pygame
import os
print("Aktuelles Arbeitsverzeichnis:", os.getcwd())
FPS = 60

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(220,60,60)
DARK_RED = (60, 10, 10)
BLUE=(60,60,220)
GREEN=(60,220,60)
YELLOW=(220,220,60)
GRAY=(100,100,100)
DARK_GREEN=(20,120,20)#farben

def read_txt_to_list(filepath):
    lines = []  # Liste aller Zeilen

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()  
                if clean_line:
                    lines.append(clean_line)
    except FileNotFoundError:
        print(f"Datei '{filepath}' nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Lesen: {e}")

    return lines
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
font = pygame.font.Font(None, 72)
text_surface = font.render("Pygame", True, RED)
text_rect = text_surface.get_rect(center=(width // 2, height // 2))# textfeld erstellen
screen.fill(BLACK)
clock = pygame.time.Clock()
running = True
while running:
    
    txt = "Wie heißt deine Datei?"
    xy = 0
    asking = True
    while asking:								#für spieler 1 der Name neu
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and xy == 1:
                    datei = txt
                    asking = False
                elif event.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                else:
                    if xy == 0:
                        txt = event.unicode
                        xy = 1
                    else:
                        txt += event.unicode

        text_surface = font.render(txt, True, WHITE)
        screen.blit(text_surface, (width//4, height//2))
        pygame.display.flip()
        clock.tick(FPS)
    datei = txt
    passwörter = read_txt_to_list(datei)
    keyasking = True
    txt = "Wie ist dein erster Schlüssel?"
    xy = 0
    while keyasking:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and xy == 1:
                    keyasking = False
                elif event.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                else:
                    if xy == 0:
                        txt = event.unicode
                        xy = 1
                    else:
                        txt += event.unicode
		try:
        	 txt = int(txt)
        except ValueError:
        	txt= "dies ist keine Zahl"
        text_surface = font.render(txt, True, WHITE)
        screen.blit(text_surface, (width//4, height//2))
        pygame.display.flip()
        clock.tick(FPS)
    key1 = txt % 89
    txt = "Wie ist dein zweiter Schlüssel?"
    xy = 0
    keyasking = True
    while keyasking:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and xy == 1:
                    keyasking = False
                elif event.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                else:
                    if xy == 0:
                        txt = event.unicode
                        xy = 1
                    else:
                        txt += event.unicode
        try:
            txt = int(txt)
        except ValueError:
        	txt= "dies ist keine Zahl"

        text_surface = font.render(txt, True, WHITE)
        screen.blit(text_surface, (width//4, height//2))
        pygame.display.flip()
        clock.tick(FPS)
    key2 = txt % 89
    zugänge = []
    for i in range(0, (len{passwörter}-1), 2):
        
    txt = f"Welches der 1 - {len(passwörter)} Passwörter möchtest du sehen?"ttt
    xy = 0
    working = True
    while working:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and xy == 1:
                    work = txt
                    working = False
                elif event.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                else:
                    if xy == 0:
                        txt = event.unicode
                        xy = 1
                    else:
                        txt += event.unicode

        text_surface = font.render(txt, True, WHITE)
        screen.blit(text_surface, (width//4, height//2))
        pygame.display.flip()
        clock.tick(FPS)
    running = False
pygame.quit()


