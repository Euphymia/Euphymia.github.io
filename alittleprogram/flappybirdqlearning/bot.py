import json


class Bot(object):
    '''
     将Qlearning逻辑应用于Flappy鸟游戏的Bot类
     在每次迭代（迭代= 1次以鸟死亡结束的游戏）之后更新Q值
     在每次DUMPING_N迭代之后，将Q值转储到本地JSON文件
    '''
    def __init__(self):
        self.gameCNT = 0 # 当前运行的游戏计数，在每次死亡后递增
        self.DUMPING_N = 25 # 之后将Q值转储为JSON的迭代次数
        self.discount = 1.0
        self.r = {0: 1, 1: -1000} # Reward function 奖励机制，正确+1，错误-1000
        self.lr = 0.7 #learning rate
        self.load_qvalues()
        self.last_state = "420_240_0"
        self.last_action = 0
        self.moves = []

    def load_qvalues(self):
        '''
        从JSON文件加载q值
        '''
        self.qvalues = {}
        try:
            fil = open('qvalues.json', 'r')
        except IOError:
            return
        self.qvalues = json.load(fil)
        fil.close()

    def act(self, xdif, ydif, vel):
        '''
        根据当前状态选择最佳动作 - 选择0（不要飞）进行最后一轮
        Chooses the best action with respect to the current state - Chooses 0 (don't flap) to tie-break
        '''
        # xdif,ydif表示小鸟的位置，vel表示小鸟在y方向上的速度
        state = self.map_state(xdif, ydif, vel)

        self.moves.append( [self.last_state, self.last_action, state] ) # Add the experience to the history

        self.last_state = state # 用当前状态更新last_state

        if self.qvalues[state][0] >= self.qvalues[state][1]:
            self.last_action = 0
            return 0
        else:
            self.last_action = 1
            return 1

    def get_last_state(self):
        return self.last_state


    def update_scores(self):
        '''
        通过迭代经验更新qvalues
        '''
        history = list(reversed(self.moves))
        # print(history)
        #如果鸟死于顶管，则打上标记 True
        high_death_flag = True if int(history[0][2].split('_')[1]) > 120 else False

        #Q-learning score updates
        t = 1
        for exp in history:
            state = exp[0]
            act = exp[1]
            res_state = exp[2]
            # 失败后，查看保存的history记录，从后向前，根据奖励机制，更新相应状态下相应动作的值
            if t == 1 or t==2:
                self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[1] + (self.discount)*max(self.qvalues[res_state]) )
            elif high_death_flag and act:
                self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[1] + (self.discount)*max(self.qvalues[res_state]) )
                high_death_flag = False
            else:
                self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[0] + (self.discount)*max(self.qvalues[res_state]) )
            t += 1

        self.gameCNT += 1 #increase game count
        self.dump_qvalues() # Dump q values (if game count % DUMPING_N == 0)
        self.moves = []  #clear history after updating strategies

    def map_state(self, xdif, ydif, vel):
        '''
         将（xdif，ydif，vel）映射到相应的状态，关于网格
         状态是一个字符串，“xdif_ydif_vel”
        这是为了减小q表的大小，加快运算，例如x 411->350,331->280
        经过转换，x和y的取值区间如下
         X - > [-40，-30 ... 120] U [140,210 ... 420]
         Y - > [-300，-290 ... 160] U [180,240 ... 420]

        Map the (xdif, ydif, vel) to the respective state, with regards to the grids
        The state is a string, "xdif_ydif_vel"

        X -> [-40,-30...120] U [140, 210 ... 420]
        Y -> [-300, -290 ... 160] U [180, 240 ... 420]
        '''
        if xdif < 140:
            xdif = int(xdif) - (int(xdif) % 10)
        else:
            xdif = int(xdif) - (int(xdif) % 70)
        if ydif < 180:
            ydif = int(ydif) - (int(ydif) % 10)
        else:
            ydif = int(ydif) - (int(ydif) % 60)

        return str(int(xdif))+'_'+str(int(ydif))+'_'+str(vel)

    def dump_qvalues(self):
        '''
        将qvalues转储到JSON文件
        '''
        if self.gameCNT % self.DUMPING_N == 0:
            fil = open('qvalues.json', 'w')
            json.dump(self.qvalues, fil)
            fil.close()
            print('Q-values updated on local file.')
