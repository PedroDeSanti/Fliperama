from leaderboard import *
import pygame
from pygame.locals import *
from sys import exit

#######################################################
# MQTT implement
# Shitty code that needs to be rewritten

import paho.mqtt.client as mqtt
import time

# global button1_state
# global button2_state
# global button3_state
# global button4_state

user = "grupo2-bancadaA4"
passwd = "L@Bdygy2A4"

Broker = "labdigi.wiseful.com.br"           
Port = 80                           
KeepAlive = 60                      

class ButtonState:
    def __init__(self):
        self.button1_state =False
        self.button2_state =False
        self.button3_state =False
        self.button4_state =False
        self.iniciar = False
        self.pronto = False

    def set(self, n, value):
        if n == 1:
            self.button1_state = value
        elif n == 2:
            self.button2_state = value
        elif n == 3:
            self.button3_state = value
        elif n == 4:
            self.button4_state = value
        elif n == "iniciar":
            self.iniciar = value
        else:
            self.pronto = value

    def get(self, n):
        if n == 1:
            return self.button1_state
        elif n == 2:
            return self.button2_state
        elif n == 3:
            return self.button3_state
        elif n == 4:
            return self.button4_state
        elif n == "iniciar":
            return self.iniciar
        else:
            return self.pronto



# Quando conectar na rede (Callback de conexao)
def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo " + str(rc))
    client.subscribe(user+"/E6", qos=0)
    client.subscribe(user+"/E5", qos=0)
    client.subscribe(user+"/E4", qos=0)
    client.subscribe(user+"/E3", qos=0)
    client.subscribe(user+"/E2", qos=0)
    client.subscribe(user+"/S4", qos=0)

# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):
    print(str(msg.topic)+" "+str(msg.payload.decode("utf-8")))

    if(int(str(msg.payload.decode("utf-8"))) == 1):
        is_pressed = True
    else:
        is_pressed = False
    if str(msg.topic) == user+"/E6":
        button_state.set(1, is_pressed)
        print("Recebi uma mensagem de E6")
    elif str(msg.topic) == user+"/E5":
        button_state.set(2, is_pressed)
        print("Recebi uma mensagem de E5")
    elif str(msg.topic) == user+"/E4":
        button_state.set(3, is_pressed)
        print("Recebi uma mensagem de E4")
    elif str(msg.topic) == user+"/E3":
        button_state.set(4, is_pressed)
        print("Recebi uma mensagem de E2")
    elif str(msg.topic) == user+"/E2":
        button_state.set("iniciar", is_pressed)
        print("Recebi uma mensagem de E3")
    elif str(msg.topic) == user+"/S4":
        button_state.set("pronto", is_pressed)
        print("Recebi uma mensagem de S4")
    else:
        print("Erro! Mensagem recebida de tópico estranho")

client = mqtt.Client()              
client.on_connect = on_connect      
client.on_message = on_message  

client.username_pw_set(user, passwd)




print("=================================================")
print("Teste Cliente MQTT")
print("=================================================")

client.connect(Broker, Port, KeepAlive)

client.loop_start() 

# A primeira mensagem costuma ser perdida aqui no notebook
client.publish(user+"/S0", payload="0", qos=0, retain=False)

# while True:
#     client.publish(user+"/S0", payload="1", qos=0, retain=False)
#     time.sleep(2)
#     client.publish(user+"/S0", payload="0", qos=0, retain=False)
#     time.sleep(2)











#######################################################




# Inicialização
WIDTH = 900
HEIGH = 600

button_state = ButtonState()

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
    char_list = "AabCcdEFGHIJkLMnOoPqrStUuVWXyZ012345689"
    button_state.set(1, False)
    button_state.set(2, False)
    button_state.set(3, False)
    button_state.set(4, False)
    button_state.set("iniciar", False)
    button_state.set("pronto", False)
    select = 0
    click = False
    changed = False
    char_index = [0, 0, 0]
    running = True
    # enquanto o jogador não aperta ESC ou return
    while running:
        if (button_state.get("iniciar") == 1):
            running = False
        screen.fill((0, 0, 0))
        draw_text('Insert Name', 'assets/PressStart2P.ttf', 50, 'Green', screen, WIDTH/2, 100)

        ###############################################
        # mx, my = pygame.mouse.get_pos()

        # # desenha os botões para as setas de criação de nickname
        # button_1 = pygame.Rect((WIDTH-150)*1/8, 400, 150, 100)
        # button_2 = pygame.Rect((WIDTH-150)*3/8, 400, 150, 100)
        # button_3 = pygame.Rect((WIDTH-150)*5/8, 400, 150, 100)
        # button_4 = pygame.Rect((WIDTH-150)*7/8, 400, 150, 100)
        # pygame.draw.rect(screen, 'Green', button_1)
        # pygame.draw.rect(screen, 'Yellow', button_2)
        # pygame.draw.rect(screen, 'Red', button_3)
        # pygame.draw.rect(screen, 'Blue', button_4)
        ############################################

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
        

        mx, my = pygame.mouse.get_pos()

        # test_surface = pygame.image.load('assets/botao.png').convert_alpha()
        # test_rect = test_surface.get_rect()
        # screen.blit(test_surface, (x, y))


        # Desenha os botões que correspondem aos... wait for it... botões
        button_1 = pygame.Rect((WIDTH-150)*1/8, 400, 150, 100)
        button_2 = pygame.Rect((WIDTH-150)*3/8, 400, 150, 100)
        button_3 = pygame.Rect((WIDTH-150)*5/8, 400, 150, 100)
        button_4 = pygame.Rect((WIDTH-150)*7/8, 400, 150, 100)
        pygame.draw.rect(screen, 'Grey25', button_1)
        pygame.draw.rect(screen, 'Grey25', button_2)
        pygame.draw.rect(screen, 'Grey25', button_3)
        pygame.draw.rect(screen, 'Grey25', button_4)


        # Caso os botões sejam clicados, acendem o led correspondente
        if ((click and button_1.collidepoint((mx, my))) or button_state.get(1)):
                pygame.draw.rect(screen, 'Green', button_1)
        if ((click and button_2.collidepoint((mx, my))) or button_state.get(2)):
                pygame.draw.rect(screen, 'Yellow', button_2)
        if ((click and button_3.collidepoint((mx, my))) or button_state.get(3)):
                pygame.draw.rect(screen, 'Red', button_3)
        if ((click and button_4.collidepoint((mx, my))) or button_state.get(4)):
                pygame.draw.rect(screen, 'Blue', button_4)

        # if (click and changed):
        #     print ("clicando")
        # if (release and changed):
        #     print ("soltando")

        # vai para a esquerda
        print("button_1", button_state.get(1), " changed: ", changed)
        if ((click and button_1.collidepoint((mx, my))) or (button_state.get(1))):
            if (select != 0):
                select -= 1
        # incrementa o caractere
        if ((click and button_2.collidepoint((mx, my))) or (button_state.get(2))):
            if (char_index[select] < len(char_list) - 1):
                char_index[select] += 1
            else:
                char_index[select] = 0
        # decrementa o caractere
        if ((click and button_3.collidepoint((mx, my))) or (button_state.get(3))):
            if (char_index[select] > 0):
                char_index[select] -= 1
            else:
                char_index[select] = len(char_list) - 1
        # vai para a direita
        if ((click and button_4.collidepoint((mx, my))) or (button_state.get(4))):
            if (select != 2):
                select += 1


        click = False
        button_state.set(1, False)
        button_state.set(2, False)
        button_state.set(3, False)
        button_state.set(4, False)
        button_state.set("iniciar", False)
        button_state.set("pronto", False)
        

        nickname = char_list[char_index[0]] + char_list[char_index[1]] + char_list[char_index[2]]

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
                if (event.key == K_RETURN):
                    running = False
                if (event.key == K_a):
                    button_state.set(1, True)
                if (event.key == K_s):
                    button_state.set(2, True)
                if (event.key == K_d):
                    button_state.set(3, True)
                if (event.key == K_f):
                    button_state.set(4, True)
            # verifica qual tecla foi solta
            if (event.type == KEYUP):
                if (event.key == K_a):
                    button_state.set(1, False)
                if (event.key == K_s):
                    button_state.set(2, False)
                if (event.key == K_d):
                    changed = True
                    button_state.set(3, False)
                if (event.key == K_f):
                    button_state.set(4, False)
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


        # # Analisa as entradas do teclado para esta tela
        # for event in pygame.event.get():
        #     if (event.type == QUIT):
        #         pygame.quit()
        #         exit()
        #     if (event.type == KEYDOWN):
        #         if (event.key == K_ESCAPE):
        #             running = False
        #         if (event.key == K_RETURN):
        #             running = False
        #     if (event.type == MOUSEBUTTONDOWN):
        #         if (event.button == 1):
        #             click = True
        #             clicking = [mx, my]
        #     if (event.type == MOUSEBUTTONUP):
        #         if (event.button == 1):
        #             click = False

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
    button_state.set(1, False)
    button_state.set(2, False)
    button_state.set(3, False)
    button_state.set(4, False)
    button_state.set("iniciar", False)
    button_state.set("pronto", False)
    while running:
        if (button_state.get("pronto") == 1):
            running = False
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
        if ((click and button_1.collidepoint((mx, my))) or button_state.get(1)):
                pygame.draw.rect(screen, 'Green', led_1)
        if ((click and button_2.collidepoint((mx, my))) or button_state.get(2)):
                pygame.draw.rect(screen, 'Yellow', led_2)
        if ((click and button_3.collidepoint((mx, my))) or button_state.get(3)):
                pygame.draw.rect(screen, 'Red', led_3)
        if ((click and button_4.collidepoint((mx, my))) or button_state.get(4)):
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
                    button_state.set(1, True)
                if (event.key == K_s):
                    button_state.set(2, True)
                if (event.key == K_d):
                    button_state.set(3, True)
                if (event.key == K_f):
                    button_state.set(4, True)
            # verifica qual tecla foi solta
            if (event.type == KEYUP):
                if (event.key == K_a):
                    button_state.set(1, False)
                if (event.key == K_s):
                    button_state.set(2, False)
                if (event.key == K_d):
                    button_state.set(3, False)
                if (event.key == K_f):
                    button_state.set(4, False)
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
    # isso aqui ta errado -> ta rodandosó uma vez
    button_state.set("perdeu", False)
    if (button_state.get("iniciar") == 1):
        button_state.set("iniciar", False)
        nick = insert_name()
        leader_board = LeaderBoard()
        leader_board.add(nick, 8888, diff)


main_menu()