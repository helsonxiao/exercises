import pygame
import random
import sys

# 创建滑雪者图像列表，文件的排序根据“转向”来决定
skier_images = ["skier_down.png", "skier_right1.png", "skier_right2.png",
                "skier_left2.png", "skier_left1.png"]


class SkierClass(pygame.sprite.Sprite):
    # 人物初始化
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 继承 - 动画精灵
        self.image = pygame.image.load("skier_down.png")  # 加载向下运动的图片，赋给滑雪者的图像属性
        self.rect = self.image.get_rect()  # 把“获取图像位置”这个方法赋给滑雪者的位置属性
        self.rect.center = [320, 100]  # 固定滑雪者的中心位置
        self.angle = 0  # 初始角度为0

    # 定义转向方法
    def turn(self, direction):
        self.angle = self.angle + direction  # 改变滑雪者的角度
        if self.angle < -2:  # 限制角度区间[-2, 2]
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        center = self.rect.center  # 缓存位置中心，因为下面的操作会清空数据。
        self.image = pygame.image.load(skier_images[self.angle])  # 根据角度加载滑雪者图片。图片列表的排序由这个决定。
        self.rect = self.image.get_rect()  # 同上
        self.rect.center = center  # 恢复位置中心
        speed = [self.angle, 6 - abs(self.angle) * 2]  # 更改速度
        return speed

    # 定义移动方法
    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]  # 改变滑雪者的横向位置
        if self.rect.centerx < 20:  # 限制位置范围
            self.rect.centerx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620


class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        # self.image_file = image_file  感觉多余，去掉后测试也没有问题
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location  # 初始化障碍物的中心位置
        self.type = type  # 设置障碍物的类型，树 或 旗
        self.passed = False  # 不能通过障碍物

    def update(self):
        global speed
        self.rect.centery -= speed[1]  # 障碍物的纵向位置不断地减去纵向速度
        if self.rect.centery < -32:  # 障碍物移出屏幕后释放内存
            self.kill()

# 生成地图
def create_map():
    global obstacles
    locations = []  # 障碍物位置列表
    for i in range(10):  # 循环10次，但不一定生成10个
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20 + 640]  # 从屏幕下方开始生成，所以y轴要加640
        if not (location in locations):  # 确保障碍物不重叠
            locations.append(location)
            type = random.choice(["tree", "flag"])  # 随机选择树 或 旗
            if type == "tree":
                img = "skier_tree.png"
            elif type == "flag":
                img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, type)  # 生成障碍物实例
            obstacles.add(obstacle)

# 画很多东西
def animate():
    screen.fill([255, 255, 255])  # 用白色填充屏幕
    obstacles.draw(screen)  # 画障碍物
    screen.blit(skier.image, skier.rect)  # 画滑雪者
    screen.blit(score_text, [10, 10])  # 画分数
    pygame.display.flip()  # 把缓冲层的内容翻转显示


pygame.init()  # 初始化pygame模块
screen = pygame.display.set_mode([640, 640])  # 设置窗口大小
clock = pygame.time.Clock()  # 生成时钟对象
skier = SkierClass()
speed = [0, 6]  # 初始速度
obstacles = pygame.sprite.Group()  # 生成对象集合，用于碰撞检测。
map_position = 0  # 初始地图位置
points = 0  # 得分
create_map()
font = pygame.font.Font(None, 50)  # 设置字体大小

running = True
while running:
    clock.tick(30)  # 30 帧，可参考书本前面的知识
    for event in pygame.event.get():  # 判断游戏事件
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)  # 传入速度，横向移动滑雪者（实际上是障碍物们在向上移动）
    map_position += speed[1]  # 将纵向速度传入地图位置
    if map_position >= 640:  # 若滑雪者已移动640，重新绘制障碍物，同时清空地图位置
        create_map()
        map_position = 0

    # 碰撞检测
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load("skier_crash.png")
            animate()  # 更新界面
            pygame.time.delay(1000)  # 延迟 1000ms
            skier.image = pygame.image.load("skier_down.png")
            skier.angel = 0
            speed = [0, 6]
            hit[0].passed = True  # 撞完之后可以通过障碍物
        elif hit[0].type == "flag" and not hit[0].passed:
            points += 10  # 得分
            hit[0].kill()  # 消去旗帜
    obstacles.update()  # 更新障碍物们的位置，营造人物向下运动的假象
    score_text = font.render("Score: " + str(points), 1, (0, 0, 0))  # 渲染分数
    animate()  # 更新界面
pygame.quit()