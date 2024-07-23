import pygame
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("블럭 깨기 게임")

# 패들 설정
PADDLE_WIDTH = 300
PADDLE_HEIGHT = 10
PADDLE_SPEED = 6

# 공 설정
BALL_SIZE = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# 벽돌 설정
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_COLOR = GREEN

# FPS 설정
FPS = 60
clock = pygame.time.Clock()

# 패들 클래스
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)

# 공 클래스
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

# 벽돌 클래스
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, BRICK_COLOR, self.rect)

# 벽돌 생성 함수
def create_bricks():
    bricks = []
    for row in range(5):
        for col in range(SCREEN_WIDTH // (BRICK_WIDTH + 10)):
            brick_x = col * (BRICK_WIDTH + 10) + 35
            brick_y = row * (BRICK_HEIGHT + 10) + 50
            bricks.append(Brick(brick_x, brick_y))
    return bricks

# 게임 루프
def main():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-PADDLE_SPEED)
        if keys[pygame.K_RIGHT]:
            paddle.move(PADDLE_SPEED)

        ball.move()

        if ball.rect.colliderect(paddle.rect) and ball.speed_y > 0:
            ball.speed_y = -ball.speed_y

        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.speed_y = -ball.speed_y
                bricks.remove(brick)

        if ball.rect.bottom >= SCREEN_HEIGHT:
            running = False  # 공이 바닥에 닿으면 게임 오버

        SCREEN.fill(BLACK)
        paddle.draw(SCREEN)
        ball.draw(SCREEN)
        for brick in bricks:
            brick.draw(SCREEN)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
