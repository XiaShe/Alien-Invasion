import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GanmeStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GanmeStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    #开始游戏主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:#玩家飞船命数为0前执行循环
            #玩家飞船移动
            ship.update()
            #每次循环都会重绘屏幕,让最近绘制的屏幕可见
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)#刷新子弹
            gf.update_aliens(ai_settings, screen, stats, sb,  ship, aliens, bullets)#刷新外星人飞船
        gf.update_screen(ai_settings, screen,stats, sb, ship, aliens, bullets, play_button)#刷新屏幕
        sb.save_high_score()#储存最高分

run_game()
