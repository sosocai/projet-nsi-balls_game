from tkinter import image_names
import pygame

BLUE = (47, 54, 153)

clock = pygame.time.Clock()
running = True
dt = 0
pygame.init()
screen = pygame.display.set_mode((570, 770))
pos =   pygame.Vector2(570/2, 50)
pos2 =   pygame.Vector2(100, 50)

pos_img=pygame.Vector2(0, 0)

def update_pos(pos):
    if(pos.y < 700):
        pos.update(pos.x, pos.y+1)
    print(f"nouvelle valeur x={pos[0]} y={pos[1]}")

apple = pygame.image.load('apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (100, 100))

x = 0
y= 150


def image_mov(y) :
    print(y)
    if y <700 :
        y=y+1
    return y


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       # print(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        running = False
    if keys[pygame.K_r]:
        pos = pygame.Vector2(570/2, 50)
        pos2 =   pygame.Vector2(100, 50)
        pos_img=pygame.Vector2(0, 0)

    if keys[pygame.K_g]:
       screen.blit(apple, pos_img)


    screen.fill(BLUE)
    pygame.draw.circle(screen, "red", pos, 20)
    pygame.draw.circle(screen, "green", pos2, 20)
    update_pos(pos)
    #update_img_pos(apple)
    screen.blit(apple, pos_img)
    update_pos(pos_img)
    clock.tick(500)

                
    #screen.blit(apple, apple.get_rect(left = screen.get_rect().left))
    #screen.blit(apple, apple.get_rect(bottom = screen.get_rect().bottom))
    #screen.blit(apple, apple.get_rect(right = screen.get_rect().right))
    #screen.blit(apple, apple.get_rect(bottom = screen.get_rect().right))
    pygame.display.update()

pygame.quit()


