import pygame
import sys
import random
import sqlite3

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (47, 54, 153)
RED = (255, 0, 0)
GREEN = (0,128,0)
YELLOW = (255,255,0)
PASTEL_BLUE = (199, 222, 255)
PASTEL_RED = (245, 154, 142)
couleurs = [BLACK,YELLOW,BLUE,GREEN,WHITE,RED] #Liste pour stocker chaque couleurs cite
couleur_actuel=couleurs[0] #permet de garder la couleur actuel de base ici noir

# Initialisation de la connexion à la base de données SQLite
conn = sqlite3.connect('scores.db')
cursor = conn.cursor()

# Création de la table des scores si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (id INTEGER PRIMARY KEY, score INTEGER)''')

# Fonction pour ajouter un score à la base de données
def ajouter_score(valeur):
    cursor.execute("INSERT INTO scores (score) VALUES (?)", (valeur,))
    conn.commit()

# Fonction pour récupérer les 5 meilleurs scores
def recuperer_meilleurs_scores():
    cursor.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 5")
    meilleurs_scores = cursor.fetchall()
    return [score[0] for score in meilleurs_scores]


#initialisaation de pygame
pygame.init()

# Paramètres de l'écran et affichage
largeur_fenetre = 570
hauteur_fenetre = 770
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("SUIKA GAME")
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Paramètres des balles
rayon_cercle = 20
position_x_cercle = largeur_fenetre // 2
position_y_cercle = 50
vitesse_x = 5 #vitesse de chute en pos_x
gravite = 4  # gravite
choix_position_fait = False
cercles_fixes = []

# Paramètres de la palteforme du sol
base = hauteur_fenetre - 15

# Paramètres du score
score = 0 #Réinitialisation du score à zéro
print(f"INIT SCORE :{score}" )
font = pygame.font.Font(None, 36)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Ajouter le score actuel à la base de données lorsque le joueur quitte la partie
            print(score)
            print("+_++)+_+_+")
            ajouter_score(score)
            conn.close()
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if not choix_position_fait:
        if keys[pygame.K_q] or keys[pygame.K_LEFT] and position_x_cercle - rayon_cercle > 0:
            position_x_cercle -= vitesse_x
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and position_x_cercle + rayon_cercle < largeur_fenetre:
            position_x_cercle += vitesse_x

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            choix_position_fait = True
    else:
        if position_y_cercle + rayon_cercle < base:
            position_y_cercle += gravite
        else:
             # Ajouter la position actuelle du cercle à la liste des cercles fixes
            cercles_fixes.append([(position_x_cercle, base - rayon_cercle) ,couleur_actuel])
            # Réinitialiser la position du prochain cercle
            couleur_actuel=random.choice(couleurs) #choisis une couleur au hasard de la list
            position_x_cercle = largeur_fenetre // 2
            position_y_cercle = 50
            choix_position_fait = False
            score += 1

    screen.fill(PASTEL_BLUE)

    # Traçage de la plateforme sol
    pygame.draw.rect(screen, PASTEL_RED, (0, base, largeur_fenetre, hauteur_fenetre - base))

    # Fixer les balles au sol:
    for cercle_fixe in cercles_fixes:
        pygame.draw.circle(screen, cercle_fixe[1], cercle_fixe[0], rayon_cercle)

    #cercle en mouvement
    pygame.draw.circle(screen, couleur_actuel, (position_x_cercle, int(position_y_cercle)), rayon_cercle)

    # Affichage du score

    score_text = font.render("Score: " + str(score), True, BLACK)
    """print(f"SCORE front :{score}")"""
    screen.blit(score_text, (10, 10))

    # Affichage des 5 meilleurs scores
    meilleurs_scores = recuperer_meilleurs_scores()
    for i, valeur in enumerate(meilleurs_scores):
        score_text = font.render(f"Top {i+1}: {valeur}", True, BLACK)
        screen.blit(score_text, (10, 50 + i * 30))

    
    pygame.display.flip() #mise a jour l'affichage
    clock.tick(60) #Limite le nombre d'images par 60 seconde

pygame.quit()
sys.exit()
