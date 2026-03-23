import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 设置屏幕为窗口模式
width, height = 800, 600  # 设置合适的窗口大小
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("鼠标定位程序")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 小球属性
ball_radius = 75  # 直径翻五倍，原半径30，现在75
balls = []

# 游戏统计
score = 0
clicks = 0

# 生成初始的三个小球
def generate_ball():
    max_attempts = 100  # 最大尝试次数，避免无限循环
    for _ in range(max_attempts):
        x = random.randint(ball_radius, width - ball_radius)
        y = random.randint(ball_radius, height - ball_radius)
        # 检查是否与其他小球重叠
        overlap = False
        for ball in balls:
            distance = ((x - ball['x']) ** 2 + (y - ball['y']) ** 2) ** 0.5
            if distance < 2 * ball_radius:
                overlap = True
                break
        if not overlap:
            color = random.choice([RED, GREEN, BLUE])
            return {'x': x, 'y': y, 'color': color}
    # 如果多次尝试后仍无法找到合适位置，返回一个默认位置
    return {'x': width // 2, 'y': height // 2, 'color': random.choice([RED, GREEN, BLUE])}

# 初始化小球
for _ in range(3):
    balls.append(generate_ball())

# 字体设置
font = pygame.font.Font(None, 72)  # 字体放大

# 游戏主循环
running = True
clock = pygame.time.Clock()

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 检查是否点击到小球
            for i, ball in enumerate(balls):
                distance = ((mouse_x - ball['x']) ** 2 + (mouse_y - ball['y']) ** 2) ** 0.5
                if distance <= ball_radius:
                    score += 1
                    balls[i] = generate_ball()
                    break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 计算命中率
    accuracy = 0 if clicks == 0 else (score / clicks) * 100

    # 绘制背景
    screen.fill(WHITE)

    # 绘制小球
    for ball in balls:
        pygame.draw.circle(screen, ball['color'], (ball['x'], ball['y']), ball_radius)

    # 绘制统计信息
    score_text = font.render(f"击破数: {score}", True, BLACK)
    accuracy_text = font.render(f"命中率: {accuracy:.1f}%", True, BLACK)
    screen.blit(score_text, (width - 200, 20))
    screen.blit(accuracy_text, (width - 200, 60))

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
sys.exit()