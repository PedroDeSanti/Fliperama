from leaderboard import *
import pygame
from pygame.locals import *
from sys import exit
# O PEDRO É MUITO LEGAL. SÓ O PEDRO.
# O JOÃO É UM CARA MUITO.... MUITOO.... MUITO?



# Inicialização
WIDTH = 900
HEIGH = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH), 0, 32)
pygame.display.set_caption('FPGA: O Melhor Jogo Já Criado!')
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

programIcon = pygame.image.load("assets/arakraken.png")
pygame.display.set_icon(programIcon)

def draw_text (text, font, size, color, surface, x, y):
    text_font = pygame.font.Font(font, size)
    text_surface = text_font.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

def display_img(img, x, y):
    screen.blit(img, (x,y))

# Tela inicial
def main_menu():    
    while True:
        screen.fill((0, 0, 0))
        draw_text('F        ', 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2, 75)
        draw_text('P        ', 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2, 125)
        draw_text('G        ', 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2, 175)
        draw_text('A        ', 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2, 225)
        draw_text(' liperama', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 75)
        draw_text(' erfeito ', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 125)
        draw_text(' amer    ', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 175)
        draw_text(' mador   ', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 225)

        mx, my = pygame.mouse.get_pos()


        button_1 = pygame.Rect((WIDTH-200)/2-25, 300, 250, 80)
        # botaoIniciar = pygame.image.load("assets/botao.png")
        # display_img(botaoIniciar, 100, 200)
        button_2 = pygame.Rect((WIDTH-200)/2-25, 400, 250, 80)

        # se o jogador clica nos botões, vai para as tela correspondente (jogo ou ranking)
        if (button_1.collidepoint((mx, my))):
            if (click):
                # leaderboards()
                game()
        if (button_2.collidepoint((mx, my))):
            if (click):
                leaderboards()

        # Desenha os dois botões para jogo e ranking
        pygame.draw.rect(screen, 'Silver', button_1)
        pygame.draw.rect(screen, 'Gold', button_2)
        draw_text("Start Game", 'assets/PressStart2P.ttf', 20, 'Black', screen, (WIDTH-200)/2+100, 340)
        draw_text("Leaderboard", 'assets/PressStart2P.ttf', 20, 'Black', screen, (WIDTH-200)/2+100, 440)
        
        click = False
        
        # Analisa os comandos do teclado para a tela MainMenu
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

# Tela de ranking (acessado via tela inicial)
def leaderboards():

    # obtém o ranking para o caso da dificuldade 1                                              MUDAR AQUI DEPOIS
    leader_board = LeaderBoard()
    scores = leader_board.get(1)
    running = True

    # Enquanto o jogador não aperta ESC
    while running:
        
        screen.fill((0, 0, 0))
        draw_text('LeaderBoard', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 50)

        # Desenha na tela as 11 melhores pontuações
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
            y = y + 52

        # Escreve o nome e pontuação de cada jogador
        y = 150
        for player in scores:
            x = (WIDTH/3)+50
            for item in player:
                # print("player: ", player, " item: ", item)
                draw_text(str(item), 'assets/PressStart2P.ttf', 20, 'Green', screen, x, y)

                x = x + 100
            y = y + 52
                
        # Analisa as entradas do teclado para esta tela
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False

        pygame.display.update()
        clock.tick(60)

# global difficulty
# click = False

# Tela de seleção de dificuldade (acessado via tela inicial)
def select_difficulty():
    difficulty = 0
    click = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Select Difficulty', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 100)

        mx, my = pygame.mouse.get_pos()

        # escreve a dificuldade selecionada (assim que alguma for selecionada)
        if (difficulty > 0):
            draw_text('Difficulty '+ str(difficulty), 'assets/PressStart2P.ttf', 20, 'Green', screen, WIDTH/2, 200)

        # desenha os botões correspondentes às dificuldades 
        dif_1 = pygame.Rect((WIDTH-200)*1/6, 400, 200, 100)
        dif_2 = pygame.Rect((WIDTH-200)*3/6, 400, 200, 100)
        dif_3 = pygame.Rect((WIDTH-200)*5/6, 400, 200, 100)
        pygame.draw.rect(screen, 'Green', dif_1)
        pygame.draw.rect(screen, 'Yellow', dif_2)
        pygame.draw.rect(screen, 'Red', dif_3)
        draw_text("Gugu Dadá", 'assets/PressStart2P.ttf', 20, 'Black', screen, (WIDTH-200)*1/6+100, 450)
        draw_text("Normal", 'assets/PressStart2P.ttf', 20, 'Black', screen, (WIDTH-200)*3/6+100, 450)
        draw_text("Doom", 'assets/PressStart2P.ttf', 20, 'Black', screen, (WIDTH-200)*5/6+100, 450)

        guguDada = pygame.image.load("assets/pacifier.png")
        display_img(guguDada, (WIDTH-200)*1/6, 200)
        pikachu = pygame.image.load("assets/pikachu.png")
        display_img(pikachu, (WIDTH-200)*3/6+25, 190)
        doomGuy = pygame.image.load("assets/doomGuy3.png")
        display_img(doomGuy, (WIDTH-200)*5/6+25, 190)

        # verifica qual dificuldade foi selecionada
        if (dif_1.collidepoint((mx, my))):
            if (click):
                difficulty = 1
                return difficulty
        if (dif_2.collidepoint((mx, my))):
            if (click):
                difficulty = 2
                return difficulty
        if (dif_3.collidepoint((mx, my))):
            if (click):
                difficulty = 3
                return difficulty

        click = False

        # Analisa as entradas do teclado para esta tela
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

    return difficulty

# Tela de criação de nickname (acessado via tela de jogo)
def insert_name():
    # difficulty = 0
    char_list = "AabCcdEFGHIJkLMnOoPqrStUuVWXyZ012345689 "
    select = 0
    click = False
    char_index = [0, 0, 0]
    running = True
    # enquanto o jogador não aperta ESC ou return
    while running:
        screen.fill((0, 0, 0))
        draw_text('Insert Name', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 100)

        mx, my = pygame.mouse.get_pos()

        # desenha os botões para as setas de criação de nickname
        button_1 = pygame.Rect((WIDTH-150)*1/8, 400, 150, 100)
        button_2 = pygame.Rect((WIDTH-150)*3/8, 400, 150, 100)
        button_3 = pygame.Rect((WIDTH-150)*5/8, 400, 150, 100)
        button_4 = pygame.Rect((WIDTH-150)*7/8, 400, 150, 100)
        pygame.draw.rect(screen, 'Green', button_1)
        pygame.draw.rect(screen, 'Yellow', button_2)
        pygame.draw.rect(screen, 'Red', button_3)
        pygame.draw.rect(screen, 'Blue', button_4)

        # Define a cor dos caracteres mostrados a depender de qual está atualmente selecionado
        if (select == 0):
            draw_text(char_list[char_index[0]], 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2 -50, 200)
            draw_text(char_list[char_index[1]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 , 200)
            draw_text(char_list[char_index[2]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 + 50, 200)    
        elif (select == 1):
            draw_text(char_list[char_index[0]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 - 50, 200)
            draw_text(char_list[char_index[1]], 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2 , 200)
            draw_text(char_list[char_index[2]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 + 50, 200)
        else:
            draw_text(char_list[char_index[0]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 - 50, 200)
            draw_text(char_list[char_index[1]], 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2 , 200)
            draw_text(char_list[char_index[2]], 'assets/PressStart2P.ttf', 50, 'Red', screen, WIDTH/2 + 50, 200)

        # vai para a esquerda
        if (button_1.collidepoint((mx, my))):
            if (click):
                if (select != 0):
                    select -= 1
        # incrementa o caractere
        if (button_2.collidepoint((mx, my))):
            if (click):
                if (char_index[select] < len(char_list) - 1):
                    char_index[select] += 1
                else:
                    char_index[select] = 0
        # decrementa o caractere
        if (button_3.collidepoint((mx, my))):
            if (click):
                if (char_index[select] > 0):
                    char_index[select] -= 1
                else:
                    char_index[select] = len(char_list) - 1
        # vai para a direita
        if (button_4.collidepoint((mx, my))):
            if (click):
                if (select != 2):
                    select += 1


        click = False

        nickname = char_list[char_index[0]] + char_list[char_index[1]] + char_list[char_index[2]]

        # Analisa as entradas do teclado para esta tela
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

# Tela de jogo (acessado via tela de seleção de dificuldade)
def game():
    diff = select_difficulty()
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
        draw_text('Difficulty '+ str(diff) +' selected', 'assets/PressStart2P.ttf', 20, 'Green', screen, WIDTH/2, 50)

        mx, my = pygame.mouse.get_pos()

        # test_surface = pygame.image.load('assets/botao.png').convert_alpha()
        # test_rect = test_surface.get_rect()
        # screen.blit(test_surface, (x, y))


        # Desenha os quadrados correspondentes aos leds
        led_1 = pygame.Rect((WIDTH-150)*1/8, 200, 150, 100)
        led_2 = pygame.Rect((WIDTH-150)*3/8, 200, 150, 100)
        led_3 = pygame.Rect((WIDTH-150)*5/8, 200, 150, 100)
        led_4 = pygame.Rect((WIDTH-150)*7/8, 200, 150, 100)
        pygame.draw.rect(screen, 'Grey25', led_1)
        pygame.draw.rect(screen, 'Grey25', led_2)
        pygame.draw.rect(screen, 'Grey25', led_3)
        pygame.draw.rect(screen, 'Grey25', led_4)

        # Desenha os botões que correspondem aos... wait for it... botões
        button_1 = pygame.Rect((WIDTH-150)*1/8, 400, 150, 100)
        button_2 = pygame.Rect((WIDTH-150)*3/8, 400, 150, 100)
        button_3 = pygame.Rect((WIDTH-150)*5/8, 400, 150, 100)
        button_4 = pygame.Rect((WIDTH-150)*7/8, 400, 150, 100)
        pygame.draw.rect(screen, 'Green', button_1)
        pygame.draw.rect(screen, 'Yellow', button_2)
        pygame.draw.rect(screen, 'Red', button_3)
        pygame.draw.rect(screen, 'Blue', button_4)


        # Caso os botões sejam clicados, acendem o led correspondente
        if ((click and button_1.collidepoint((mx, my))) or button1_state):
                pygame.draw.rect(screen, 'Green', led_1)
        if ((click and button_2.collidepoint((mx, my))) or button2_state):
                pygame.draw.rect(screen, 'Yellow', led_2)
        if ((click and button_3.collidepoint((mx, my))) or button3_state):
                pygame.draw.rect(screen, 'Red', led_3)
        if ((click and button_4.collidepoint((mx, my))) or button4_state):
                pygame.draw.rect(screen, 'Blue', led_4)

        # if (click and changed):
        #     print ("clicando")
        # if (release and changed):
        #     print ("soltando")

        # click = False
        # release = False
        changed = False

        # Analisa as entradas do teclado para esta tela
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            # verifica qual tecla foi pressionada
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False
                if (event.key == K_a):
                    button1_state = True
                if (event.key == K_s):
                    button2_state = True
                if (event.key == K_d):
                    button3_state = True
                if (event.key == K_f):
                    button4_state = True
            # verifica qual tecla foi solta
            if (event.type == KEYUP):
                if (event.key == K_a):
                    button1_state = False
                if (event.key == K_s):
                    button2_state = False
                if (event.key == K_d):
                    button3_state = False
                if (event.key == K_f):
                    button4_state = False
            # verifica o mouse
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