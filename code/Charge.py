import pygame
pygame.init()
import time
from Utilitaire import lock16_9

largeur = 1600
hauteur = 900

def ecranCharge(fenetreJeu): # fenetreJeu est la fenetre en cours pour ne pas en ouvrir une nouvelle
    """
    Cette fonction permet d'afficher l'écran de charge à chaque fois qu'elle est apellée.
    Elle calcule les images de l'écran de charge et leurs positions.
    Elle les affiche après.
    """
    
    global largeur, hauteur
       
    # Import de l'image de fond d'origine (car elle est tournée par la suite)
    fondOrigine = pygame.image.load("../Images/Fond.png")

    # Création d'une surface de rendu
    surface_rendu = pygame.Surface((largeur, hauteur))

    # Charger l'image à faire tourner (en bas à droite)
    LogoChargeOrigine = pygame.image.load("../Images/LogoCharge2.png")

    # Angle de rotation initial
    rotation_angle = 0

    duree = 2  # Durée en secondes de l'écran de charge
    temps_debut = time.time()  # Temps de début de la boucle
    clock = pygame.time.Clock()
    
    # Cette boucle dure jusqu'a ce que "duree" soit dépassé
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            elif event.type == pygame.VIDEORESIZE: # Événement de redimensionnement de la fenêtre                
                # Calculer la fenêtre avec les nouvelles dimensions
                largeur, hauteur = lock16_9(event)
                # Mettre à jour la fenêtre avec les nouvelles dimensions
                fenetreJeu = pygame.display.set_mode((largeur, hauteur), flags=pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        
        
        
fenetreJeu = pygame.display.set_mode((largeur, hauteur), flags=pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Jeu Delta")
ecranCharge(fenetreJeu)