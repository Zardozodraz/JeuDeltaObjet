import pygame
pygame.init()

def lock16_9(event):
    largeur = 1600
    hauteur = 900
    screen_height = pygame.display.Info().current_h

    ratio_16_9 = 16 / 9
    nouvelle_largeur = largeur
    nouvelle_hauteur = hauteur

    # Si la largeur a changé, on ajuste la hauteur
    if event.w != largeur:
        nouvelle_largeur = event.w
        nouvelle_hauteur = int(nouvelle_largeur / ratio_16_9)
        
    # sinon on ajuste la largeur
    elif event.h != hauteur:
        nouvelle_hauteur = event.h
        nouvelle_largeur = int(nouvelle_hauteur * ratio_16_9)
        
    # Si la hauteur doit être supérieure à la hauteur de l'écran, on passe en full screen
    if int(event.w / ratio_16_9) >= screen_height:
        nouvelle_largeur, nouvelle_hauteur = event.size
    return nouvelle_largeur, nouvelle_hauteur