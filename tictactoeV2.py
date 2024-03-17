import pygame
from pygame.locals import *
import random

pygame.init()

screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Le meilleur jeu')

background_img = pygame.image.load("TicTacToe/images/background_image.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

#definir les variables
line_width = 3
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

# Charger les images des joueurs
x_imgs = [pygame.image.load(f"TicTacToe/images/player1/coco{i}.png") for i in range(1, 11)]
o_imgs = [pygame.image.load(f"TicTacToe/images/player2/mango{i}.png") for i in range(1, 11)]
img_size = (100, 100) 

#couleurs
rougePale = (243, 186, 186)
red = (255, 0, 0)
noir = (0, 0, 0)
#font
font = pygame.font.SysFont(None, 40)

rejouer_rectangle = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

def grille():
    screen.blit(background_img, (0, 0))
    grid = (50, 50, 50)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)

for x in range(3):
    row = [0] * 3
    markers.append(row)


selected_images = [[None for _ in range(3)] for _ in range(3)]


selected_images = [[None for _ in range(3)] for _ in range(3)]

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
              
                if selected_images[x_pos][y_pos] is None:
                    selected_images[x_pos][y_pos] = random.choice(x_imgs)
                x_img = selected_images[x_pos][y_pos]
                x_img = pygame.transform.scale(x_img, img_size)

                img_x = x_pos * 100 + (100 - img_size[0]) // 2
                img_y = y_pos * 100 + (100 - img_size[1]) // 2
                screen.blit(x_img, (img_x, img_y))
            elif y == -1:
                
                if selected_images[x_pos][y_pos] is None:
                    selected_images[x_pos][y_pos] = random.choice(o_imgs)
                o_img = selected_images[x_pos][y_pos]
                o_img = pygame.transform.scale(o_img, img_size)

                # Centrer l'image au centre des cases
                img_x = x_pos * 100 + (100 - img_size[0]) // 2
                img_y = y_pos * 100 + (100 - img_size[1]) // 2
                screen.blit(o_img, (img_x, img_y))
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner
    global game_over
    y_pos = 0
    for x in markers:
        #Verifier les colonnes
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #Verifier les rangees
        if markers[0][y_pos] + markers[1][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
        #verifier en diagonale
        if markers [0] [0] + markers [1] [1] + markers [2][2] == 3 or markers [2][0] + markers [1][1] + markers[0][2] == 3:
            winner = 1
            game_over = True
        if markers [0] [0] + markers [1] [1] + markers [2][2] == -3 or markers [2][0] + markers [1][1] + markers[0][2] == -3:
            winner = 2
            game_over = True

def draw_rounded_rect(surface, rect, color, corner_radius):
    pygame.draw.rect(surface, color, rect.inflate(-corner_radius*2, 0))
    pygame.draw.rect(surface, color, rect.inflate(0, -corner_radius*2))
    pygame.draw.circle(surface, color, (rect.left+corner_radius, rect.top+corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.right-corner_radius-1, rect.top+corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.left+corner_radius, rect.bottom-corner_radius-1), corner_radius)
    pygame.draw.circle(surface, color, (rect.right-corner_radius-1, rect.bottom-corner_radius-1), corner_radius)

def draw_winner(winner):
    win_text = 'Joueur ' + str(winner) + " a gagné!"
    win_img = font.render(win_text, True, noir)
    rect = pygame.Rect(screen_width // 2 - 120, screen_height // 2 - 60, 240, 50)
    draw_rounded_rect(screen, rect, rougePale, 10,)
    screen.blit(win_img, (screen_width // 2 - 120, screen_height // 2 - 50))

def draw_rejouer():
    rejouer_text = 'Rejouer?'
    rejouer_img = font.render(rejouer_text, True, noir)
    rect = rejouer_rectangle
    draw_rounded_rect(screen, rect, rougePale, 10)
    screen.blit(rejouer_img, (screen_width // 2 - 60, screen_height // 2 + 10))

def check_tie():
    for row in markers:
        for cell in row:
            if cell == 0:
                return False 
    return True  



#main loop 
run = True
while run:

    grille()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_X = pos[0]
                cell_Y = pos[1]
                if markers[cell_X // 100][cell_Y//100] == 0:
                    markers[cell_X // 100][cell_Y//100] = player
                    player *= -1
                    check_winner()
                    if check_tie():
                        game_over = True

    if game_over == True:

        if winner != 0:
            draw_winner(winner)
            draw_rejouer()
        else:
            draw_rejouer()
            
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
        if rejouer_rectangle.collidepoint(pos):
                    markers = []
                    pos = []
                    player = 1
                    winner = 0
                    game_over = False
                    for x in range(3):
                        row = [0] * 3
                        markers.append(row)
                    selected_images = [[None for _ in range(3)] for _ in range(3)]
    pygame.display.update()

pygame.quit()