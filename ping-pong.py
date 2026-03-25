import pygame

pygame.init()

window_width = 600
window_height = 600
display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong")

ball_color = (255, 165, 0)
ball_radius = 15
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed_x = 5
ball_speed_y = 5

paddle_width = 10
paddle_height = 80
paddle_color = (255, 0, 0)
paddle_speed = 8

paddle1_x = 20
paddle1_y = window_height // 2 - paddle_height // 2

paddle2_x = window_width - 30
paddle2_y = window_height // 2 - paddle_height // 2

score1 = 0
score2 = 0

clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont(None, 40)
background_color = (255, 255, 255)




running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < window_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < window_height - paddle_height:
        paddle2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y - ball_radius < 0 or ball_y + ball_radius > window_height:
        ball_speed_y *= -1

    if (ball_x - ball_radius < paddle1_x + paddle_width and
            ball_y > paddle1_y and ball_y < paddle1_y + paddle_height):
        ball_speed_x *= -1

    if (ball_x + ball_radius > paddle2_x and
            ball_y > paddle2_y and ball_y < paddle2_y + paddle_height):
        ball_speed_x *= -1

    if ball_x < 0:
        score2 += 1
        ball_x = window_width // 2
        ball_y = window_height // 2
        ball_speed_x = 5
        ball_speed_y = 5

    if ball_x > window_width:
        score1 += 1
        ball_x = window_width // 2
        ball_y = window_height // 2
        ball_speed_x = -5
        ball_speed_y = 5

    display.fill(background_color)
    score_text = font.render(f"Score1 = {score1}   Score2 = {score2}", True, (0, 0, 0))
    display.blit(score_text, (window_width // 2 - 120, 20))

    pygame.draw.circle(display, ball_color, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(display, paddle_color, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(display, paddle_color, (paddle2_x, paddle2_y, paddle_width, paddle_height))



    pygame.draw.line(display, (0, 0, 0), (window_width // 2, 0), (window_width // 2, window_height), 2)

    pygame.display.flip()

pygame.quit()