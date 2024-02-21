import pygame
import sys

#couleur
BLUE = (47, 54, 153)
PASTEL_BLUE = (199, 222, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PASTEL_RED = (245, 154, 142)



"""parrametres de l'ecran et affichage"""
#Paramètres
largeur_fenetre = 570
hauteur_fenetre = 770


#Initialisation
clock = pygame.time.Clock()
running = True
pygame.init()
pygame.display.set_caption("SUIKA GAME")
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

"""les parametres ball"""
#Initialisation
rayon_cercle = 20
position_x_cercle = largeur_fenetre // 2
position_y_cercle = 50
#mouvement ball
vitesse_x = 5
gravite = 4  # gravite
choix_position_fait = False
cercles_fixes = []#Liste pour stocker les positions des balles

"""parrametres du sol"""
base = hauteur_fenetre - 15 #Position base



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if not choix_position_fait:
        if keys[pygame.K_q] or keys[pygame.K_LEFT] and position_x_cercle - rayon_cercle > 0:
            position_x_cercle -= vitesse_x
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and position_x_cercle + rayon_cercle < largeur_fenetre:
            position_x_cercle += vitesse_x

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            choix_position_fait = True
    else:
        #Si la position est choisie, faire tomber la balle
        if position_y_cercle + rayon_cercle < base:
            position_y_cercle += gravite
        else:
            # Ajouter la position actuelle du cercle à la liste des cercles fixes
            cercles_fixes.append((position_x_cercle, base - rayon_cercle))
            # Réinitialiser la position du prochain cercle
            position_x_cercle = largeur_fenetre // 2
            position_y_cercle = 50
            choix_position_fait = False

    

    screen.fill(PASTEL_BLUE)

    #sol
    pygame.draw.rect(screen, PASTEL_RED, (0, base, largeur_fenetre, hauteur_fenetre - base))

    # Fixer les balles au sol:
    for cercle_fixe in cercles_fixes:
        pygame.draw.circle(screen, BLACK, cercle_fixe, rayon_cercle)

    # cercle en mouvement
    pygame.draw.circle(screen, BLACK, (position_x_cercle, int(position_y_cercle)), rayon_cercle)

    pygame.display.flip() #mise a jour l'affichage

    clock.tick(60) #Limite le nombre d'images par seconde

pygame.quit()
