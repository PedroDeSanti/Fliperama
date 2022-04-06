from leaderboard import *
import pygame
from pygame.locals import *
from sys import exit

WIDTH = 900
HEIGH = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH), 0, 32)
pygame.display.set_caption('Fliperama Perfeito Gamer Amador')
clock = pygame.time.Clock()

# test_surface = pygame.Surface((200, 100))
# test_surface.fill('Red')

# test_surface = pygame.image.load('assets/botao.png').convert_alpha()
# test_rect = test_surface.get_rect()

title = pygame.font.Font('assets/PressStart2P.ttf', 50)

title_surface = title.render('Fliperama', False, 'Green')
# x = 0
# y = 0
click = False

def draw_text (text, font, size, color, surface, x, y):
    text_font = pygame.font.Font(font, size)
    text_surface = text_font.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

def main_menu():    
    while True:
        screen.fill((0, 0, 0))
        draw_text('Fliperama', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 100)

        mx, my = pygame.mouse.get_pos()


        button_1 = pygame.Rect((WIDTH-200)/2, 200, 200, 50)
        button_2 = pygame.Rect((WIDTH-200)/2, 300, 200, 50)

        if (button_1.collidepoint((mx, my))):
            if (click):
                # leaderboards()
                game()
        if (button_2.collidepoint((mx, my))):
            if (click):
                leaderboards()


        pygame.draw.rect(screen, 'Red', button_1)
        pygame.draw.rect(screen, 'Red', button_2)

        click = False
        
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            if (event.type == MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True
                    clicking = [mx, my]
            if (event.type == MOUSEBUTTONUP):
                if (event.button == 1):
                    click = False

        
        # screen.blit(test_surface, ((WIDTH-test_surface.get_width())/2, 300))
        # screen.blit(title_surface, ((WIDTH-title_surface.get_width())/2, 100))
        # screen.blit(test_surface, (x, y))
        # x = x+1
        # y = y+1
        
        pygame.display.update()
        clock.tick(60)

def leaderboards():
    leader_board = LeaderBoard()
    scores = leader_board.get(1)
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('LeaderBoard', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 50)

        y = 150
        x = (WIDTH/3)-50
        for i in range(1, 12):
            if (i == 1):
                position = "1ST"
            elif (i == 2):
                position = "2ND"
            elif (i == 3):
                position = "3RD"
            else:
                position = str(i) + "TH"
            draw_text(position, 'assets/PressStart2P.ttf', 20, 'Green', screen, x, y)
            y = y + 50

        y = 150
        for player in scores:
            x = (WIDTH/3)+50
            for item in player:
                # print("player: ", player, " item: ", item)
                draw_text(str(item), 'assets/PressStart2P.ttf', 20, 'Green', screen, x, y)

                x = x + 100
            y = y + 50
                

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False

        pygame.display.update()
        clock.tick(60)

# global difficult
# click = False


def select_difficult():
    difficult = 0
    click = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Select Difficult', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 100)

        mx, my = pygame.mouse.get_pos()

        if (difficult > 0):
            draw_text('Difficult '+ str(difficult), 'assets/PressStart2P.ttf', 20, 'Green', screen, WIDTH/2, 200)

        dif_1 = pygame.Rect((WIDTH-200)*1/6, 300, 200, 100)
        dif_2 = pygame.Rect((WIDTH-200)*3/6, 300, 200, 100)
        dif_3 = pygame.Rect((WIDTH-200)*5/6, 300, 200, 100)

        if (dif_1.collidepoint((mx, my))):
            if (click):
                difficult = 1
                return difficult
        if (dif_2.collidepoint((mx, my))):
            if (click):
                difficult = 2
                return difficult
        if (dif_3.collidepoint((mx, my))):
            if (click):
                difficult = 3
                return difficult


        pygame.draw.rect(screen, 'Green', dif_1)
        pygame.draw.rect(screen, 'Yellow', dif_2)
        pygame.draw.rect(screen, 'Red', dif_3)

        click = False

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False
            if (event.type == MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True
                    clicking = [mx, my]
            if (event.type == MOUSEBUTTONUP):
                if (event.button == 1):
                    click = False

        pygame.display.update()
        clock.tick(60)

    return difficult

def insert_name():
    # difficult = 0
    char_list = "AabCcdEFGHIJkLMnOoPqrStUuVWXyZ012345689 "
    select = 0
    click = False
    char_index = [0, 0, 0]
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Insert Name', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect((WIDTH-150)*1/8, 400, 150, 100)
        button_2 = pygame.Rect((WIDTH-150)*3/8, 400, 150, 100)
        button_3 = pygame.Rect((WIDTH-150)*5/8, 400, 150, 100)
        button_4 = pygame.Rect((WIDTH-150)*7/8, 400, 150, 100)


        if (select == 0):
            draw_text(char_list[char_index[0]], 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2, 200)
            draw_text(char_list[char_index[1]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 + 50, 200)
            draw_text(char_list[char_index[2]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 + 100, 200)
        
        elif (select == 1):
            draw_text(char_list[char_index[0]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 200)
            draw_text(char_list[char_index[1]], 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2 + 50, 200)
            draw_text(char_list[char_index[2]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 + 100, 200)

        else:
            draw_text(char_list[char_index[0]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 200)
            draw_text(char_list[char_index[1]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 + 50, 200)
            draw_text(char_list[char_index[2]], 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2 + 100, 200)


        if (button_1.collidepoint((mx, my))):
            if (click):
                if (select != 0):
                    select -= 1

        if (button_2.collidepoint((mx, my))):
            if (click):
                if (char_index[select] < len(char_list) - 1):
                    char_index[select] += 1
                else:
                    char_index[select] = 0

        if (button_3.collidepoint((mx, my))):
            if (click):
                if (char_index[select] > 0):
                    char_index[select] -= 1
                else:
                    char_index[select] = len(char_list) - 1

        if (button_4.collidepoint((mx, my))):
            if (click):
                if (select != 2):
                    select += 1

        pygame.draw.rect(screen, 'Green', button_1)
        pygame.draw.rect(screen, 'Yellow', button_2)
        pygame.draw.rect(screen, 'Red', button_3)
        pygame.draw.rect(screen, 'Blue', button_4)

        click = False

        nickname = char_list[char_index[0]] + char_list[char_index[1]] + char_list[char_index[2]]

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False
                if (event.key == K_RETURN):
                    running = False
            if (event.type == MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True
                    clicking = [mx, my]
            if (event.type == MOUSEBUTTONUP):
                if (event.button == 1):
                    click = False

        pygame.display.update()
        clock.tick(60)

    return nickname

def game():
    diff = select_difficult()
    click = False
    release = False
    running = True
    changed = False
    button1_state = False
    button2_state = False
    button3_state = False
    button4_state = False
    while running:

        screen.fill((0, 0, 0))
        draw_text('Difficult '+ str(diff) +' selected', 'assets/PressStart2P.ttf', 20, 'Green', screen, WIDTH/2, 50)

        mx, my = pygame.mouse.get_pos()

        # test_surface = pygame.image.load('assets/botao.png').convert_alpha()
        # test_rect = test_surface.get_rect()
        # screen.blit(test_surface, (x, y))

        led_1 = pygame.Rect((WIDTH-150)*1/8, 200, 150, 100)
        led_2 = pygame.Rect((WIDTH-150)*3/8, 200, 150, 100)
        led_3 = pygame.Rect((WIDTH-150)*5/8, 200, 150, 100)
        led_4 = pygame.Rect((WIDTH-150)*7/8, 200, 150, 100)

        button_1 = pygame.Rect((WIDTH-150)*1/8, 400, 150, 100)
        button_2 = pygame.Rect((WIDTH-150)*3/8, 400, 150, 100)
        button_3 = pygame.Rect((WIDTH-150)*5/8, 400, 150, 100)
        button_4 = pygame.Rect((WIDTH-150)*7/8, 400, 150, 100)

        pygame.draw.rect(screen, 'Grey25', led_1)
        pygame.draw.rect(screen, 'Grey25', led_2)
        pygame.draw.rect(screen, 'Grey25', led_3)
        pygame.draw.rect(screen, 'Grey25', led_4)

        pygame.draw.rect(screen, 'Green', button_1)
        pygame.draw.rect(screen, 'Yellow', button_2)
        pygame.draw.rect(screen, 'Red', button_3)
        pygame.draw.rect(screen, 'Blue', button_4)

        if (button_1.collidepoint((mx, my))):
            if (click or button1_state):
                pygame.draw.rect(screen, 'Green', led_1)

        if (button_2.collidepoint((mx, my))):
            if (click):
                pygame.draw.rect(screen, 'Yellow', led_2)

        if (button_3.collidepoint((mx, my))):
            if (click):
                pygame.draw.rect(screen, 'Red', led_3)

        if (button_4.collidepoint((mx, my))):
            if (click):
                pygame.draw.rect(screen, 'Blue', led_4)

        # if (click and changed):
        #     print ("clicando")
        # if (release and changed):
        #     print ("soltando")

        # click = False
        # release = False
        changed = False
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False
                if (event.key == K_f):
                    button1_state = True
                if (event.key == K_g):
                    button2_state = True
                if (event.key == K_h):
                    button3_state = True
                if (event.key == K_j):
                    button4_state = True
            if (event.type == KEYUP):
                if (event.key == K_f):
                    button1_state = False
                if (event.key == K_g):
                    button2_state = False
                if (event.key == K_h):
                    button3_state = False
                if (event.key == K_j):
                    button4_state = False
            if (event.type == MOUSEBUTTONDOWN):
                if (event.button == 1):
                    changed = True
                    click = True
                    release = False
                    clicking = [mx, my]
            if (event.type == MOUSEBUTTONUP):
                if (event.button == 1):
                    changed = True
                    click = False
                    release = True

        pygame.display.update()
        clock.tick(60)

    nick = insert_name()
    leader_board = LeaderBoard()
    leader_board.add(nick, 8888, diff)


main_menu()