# 2d game

import pygame

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# check errors

check_error = pygame.init()

if check_error[1] >= 1:
    print(f"Error {check_error[1]}")
else:
    print("No Errors")

# window settings

frame_size_x = 800
frame_size_y = 600

my_title = "Mario Game"

my_screen = pygame.display.set_mode((frame_size_x, frame_size_y))

pygame.display.set_caption(my_title)

# =======================================================================================================================================


def images():
    global move_left, move_right, hero_r, hero_l, start_img, exit_img, bg

    move_left = [pygame.image.load(r"C:\Users\user\Desktop\VSCODE\photos\mario_NoMove_l.png"),
                 pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_move2_l.png"),
        pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_move2_l.png"),
        pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_move1_l.png")]
    move_right = [pygame.image.load(r"C:\Users\user\Desktop\VSCODE\photos\mario_NoMove_r.png"),
                  pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_move2_r.png"),
        pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_move2_r.png"),
        pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_move1_r.png")]

    hero_r = pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_NoMove_r.png")
    hero_l = pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\mario_NoMove_l.png")

    start_img = pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\start_img.png")
    exit_img = pygame.image.load(
        r"C:\Users\user\Desktop\VSCODE\photos\exit_img.png")

    # background
    bg = pygame.image.load(r"C:\Users\user\Desktop\VSCODE\photos\back.jpg")


def texts():
    global start_text, exit_text
    start_font = pygame.font.SysFont(None, 20, True, True)
    exit_font = pygame.font.SysFont(None, 20, True, True)
    start_text = start_font.render(
        "press '1' button to lanch the game", True, WHITE)
    exit_text = exit_font.render(
        "press 'ECS' button to exit the game", True, WHITE)


def object_settings():
    global object_size, object_x, object_y, x_spase, y_spase, moves, speed_jumping, height_jump, frames
    object_size = 40
    object_x = 20
    object_y = 450
    x_spase = 0
    y_spase = 0
    moves = 0
    speed_jumping = 10
    height_jump = 0.30
    frames = 60


def TF():
    global game_over, is_jumping, is_start, stop_left, stop_right, left, right
    game_over = False
    is_jumping = False
    is_start = False
    stop_left = False
    stop_right = False
    left = False
    right = False


images()
texts()
object_settings()
TF()

# =======================================================================================================================================

# game lunching

while not game_over:
    pygame.time.Clock().tick(frames)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    key = pygame.key.get_pressed()

    if key[pygame.K_1]:
        is_start = True
    if key[pygame.K_ESCAPE]:
        game_over = True

    if is_start == True:
        if (key[pygame.K_LEFT] or key[pygame.K_q]) and object_x > 0:
            object_x -= 3
            left = True
            right = False
            stop_left = True
            stop_right = False
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and object_x + object_size < frame_size_x:
            object_x += 3
            right = True
            left = False
            stop_left = False
            stop_right = True
        else:
            right = False
            left = False
            moves = 0

        if not is_jumping:
            if key[pygame.K_SPACE]:
                is_jumping = True
        else:
            if speed_jumping >= -10:
                neg = 1
                if speed_jumping < 0:
                    neg = -1
                object_y -= (speed_jumping ** 2) * height_jump * neg
                speed_jumping -= 1
            else:
                speed_jumping = 10
                is_jumping = False

    my_screen.blit(bg, (0, 0))
    # my_screen.fill(BLACK)
    if not is_start:
        my_screen.blit(start_text, (1, 560))
    if not is_start:
        my_screen.blit(exit_text, (1, 580))
    if not is_start:
        my_screen.blit(start_img, (250, 100))
        my_screen.blit(exit_img, (267, 300))
    else:
        if left:
            my_screen.blit(move_left[moves // 5], (object_x, object_y))
            moves += 1
            if moves == 20:
                moves = 0
        elif right:
            my_screen.blit(move_right[moves // 5], (object_x, object_y))
            moves += 1
            if moves == 20:
                moves = 0
        else:
            if not stop_left:
                my_screen.blit(hero_r, (object_x, object_y))
            elif not stop_right:
                my_screen.blit(hero_l, (object_x, object_y))

    pygame.display.update()
