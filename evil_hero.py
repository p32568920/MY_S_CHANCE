class Evil_Hero():

    def __init__(self):

        self.name='Darkness'

        self.maxhp = 100
        self.maxmp = 100
        self.hp = self.maxhp
        self.mp = self.maxmp

        self.maxsp = 10
        self.sp = 0
        self.level = 1
        self.exp = 0

    def recovery(self):

        self.hp = self.maxhp
        self.mp = self.maxmp

    def check_exp(self):
        pass

    def level_up(self):
        pass
        
