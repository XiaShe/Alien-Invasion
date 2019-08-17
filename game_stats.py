class GanmeStats():
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_setttings):
        '''初始化统计信息'''
        self.ai_settings = ai_setttings
        self.reset_stats()
        #游戏刚启动时处于非活动状态
        self.game_active = False
        #在任何情况下都不应重置最高得分,最高分存储于文件中
        #self.high_score = 0
        with open('high_score.txt', 'r') as file_high_score:
            for line in file_high_score:
                self.high_score = int(line)


    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 #初始游戏分数
        self.level = 0 #玩家初始等级