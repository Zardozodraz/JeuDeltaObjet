import pygame
pygame.init()
import time
from Utilitaire import lock16_9

largeur = 1600
hauteur = 900

def ecranCharge(fenetreJeu):  # fenetreJeu est la fenetre en cours pour ne pas en ouvrir une nouvelle
    """
    Cette fonction permet d'afficher l'écran de charge à chaque fois qu'elle est apellée.
    Elle calcule les images de l'écran de charge et leurs positions.
    Elle les affiche après.
    """
    
    global largeur, hauteur
       
    # Import de l'image de fond d'origine (car elle est tournée par la suite)
    fondOrigine = pygame.image.load("../images/fonds/Fond.png")
    
    # Création d'une surface de rendu
    surface_rendu = pygame.Surface((largeur, hauteur))
    
    # Charger l'image à faire tourner (en bas à droite)
    LogoChargeOrigine = pygame.image.load("../images/logo/LogoCharge2.png")
    
    # Angle de rotation initial
    rotation_angle = 0
    
    # Calculer la taille de l'image
    LogoCharge = pygame.transform.scale(LogoChargeOrigine, (200, 200))
    
    # Calculer le CENTRE de l'image (position fixe)
    centre_x = largeur - 100 - 50  # largeur - (taille_image/2) - marge
    centre_y = hauteur - 100 - 50  # hauteur - (taille_image/2) - marge
    
    # Redimensionner l'image de fond initialement
    fondRedimensionne = pygame.transform.scale(fondOrigine, (largeur, hauteur))
    
    duree = 5  # Durée en secondes de l'écran de charge
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
                
                # Recréer la surface de rendu avec les nouvelles dimensions
                surface_rendu = pygame.Surface((largeur, hauteur))
                
                # Recalculer le centre après redimensionnement
                centre_x = largeur - 100 - 50
                centre_y = hauteur - 100 - 50
                
                # Redimensionner l'image de fond pour la nouvelle taille
                fondRedimensionne = pygame.transform.scale(fondOrigine, (largeur, hauteur))
        
        # Calculer le temps écoulé
        temps_ecoule = time.time() - temps_debut
        if temps_ecoule > duree:
            done = True
        
        # Calculer la rotation de l'image
        rotation_angle += 3
        if rotation_angle >= 360:
            rotation_angle = 0
        
        # Appliquer la rotation à l'image
        LogoChargeRotate = pygame.transform.rotate(LogoCharge, rotation_angle)
        
        # IMPORTANT : Calculer la nouvelle position pour centrer l'image tournée
        # L'image tournée a une taille différente, donc on doit ajuster sa position
        rect_rotate = LogoChargeRotate.get_rect()
        rect_rotate.center = (centre_x, centre_y)  # Centrer sur le point fixe
        
        # Remplir la surface de rendu avec une couleur (noir)
        surface_rendu.fill((0, 0, 0)) 
        
        # Afficher l'image de fond redimensionnée
        surface_rendu.blit(fondRedimensionne, (0, 0))
        
        # Afficher l'image de l'écran de charge avec la position corrigée
        surface_rendu.blit(LogoChargeRotate, rect_rotate.topleft)
        
        # Afficher la surface de rendu dans la fenêtre
        fenetreJeu.blit(surface_rendu, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)

fenetreJeu = pygame.display.set_mode((largeur, hauteur), flags=pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Jeu Delta")
ecranCharge(fenetreJeu)