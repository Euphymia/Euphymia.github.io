from itertools import cycle
from bot import Bot

import random
import sys

import pygame
from pygame.locals import *

# 初始化机器人
bot = Bot()
# 每秒传输帧数(Frames Per Second
FPS = 60
# 设置游戏的宽度和高度
SCREENWIDTH  = 288
SCREENHEIGHT = 512
# 基数最多可以左移的量
# amount by which base can maximum shift to left
PIPEGAPSIZE  = 100 # 管子上下部分之间的缝隙
# base地面那个条条所在的高度 注意以左上角为坐标起始点  所以这个高度是往下为正  
BASEY        = SCREENHEIGHT * 0.79
# 图像，声音和hitmask字典
IMAGES, SOUNDS, HITMASKS = {}, {}, {}

# list of all possible players (tuple of 3 positions of flap)三种小鸟造型  
PLAYERS_LIST = (
    # red bird
    (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png',
    ),
    # blue bird
    (
        # amount by which base can maximum shift to left
        'assets/sprites/bluebird-upflap.png',
        'assets/sprites/bluebird-midflap.png',
        'assets/sprites/bluebird-downflap.png',
    ),
    # yellow bird
    (
        'assets/sprites/yellowbird-upflap.png',
        'assets/sprites/yellowbird-midflap.png',
        'assets/sprites/yellowbird-downflap.png',
    ),
)

# list of backgrounds  两种背景，一种白天，一种黑夜  
BACKGROUNDS_LIST = (
    'assets/sprites/background-day.png',
    'assets/sprites/background-night.png',
)

# list of pipes 管道的两种颜色，一种绿色，一种红色  
PIPES_LIST = (
    'assets/sprites/pipe-green.png',
    'assets/sprites/pipe-red.png',
)


def main():
    global SCREEN, FPSCLOCK, bot
    # 初始化pygame,为使用硬件做准备
    pygame.init()
    # 管理时间和帧信息
    # 使用Pygame时钟之前，必须先创建Clock对象的一个实例， 
    # 控制每个循环多长时间运行一次。这就像一个定时器在控制时间进程，指出“现在开始下一个循环”！现在开始下一个循环！……  
    FPSCLOCK = pygame.time.Clock()
    # 创建了一个窗口
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    # 设置窗口标题
    pygame.display.set_caption('Flappy Bird')

    # 设置比分显示的图片
    # 在pygame中可以使用pygame.image.load（）函数来加载位图。（支持jpg,png,gif,bmp,pcx,tif,tga等多种图片格式）。
    # convert_alpha()方法会使用透明的方法绘制前景对象，因此在加载一个有alpha通道的素材时（比如PNG TGA），
    # 需要使用convert_alpha()方法，当然普通的图片也是可以使用这个方法的，用了也不会有什么副作用。
    IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    # game over 的图片
    IMAGES['gameover'] = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
    # welcome screen 的图片
    IMAGES['message'] = pygame.image.load('assets/sprites/message.png').convert_alpha()
    # base (ground) 地面的图片
    IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()

    # 声音
    # WAV版 OGG版是指游戏的音频格式  
    # WAV版是属于游戏原版  
    # OGG是大大们通过转换器把音频格式的WAV改成OGG，这样游戏的配置提高要求使游戏本身的体积而缩小节省了空间。  
    # 可以看一下同一个音频 ogg版的是比wav版的文件小很多  
    # 如果是windows系统，使用.wav的音频格式
    if 'win' in sys.platform:
        soundExt = '.wav'
    # 如果不是
    else:
        soundExt = '.ogg'
    # 音效:pygame.mixer  
    # sound = pygame.mixer.Sound('/home/liumin/love.wav')使用指定文件名载入一个音频文件，并创建一个Sound对象。 
    # 音频文件可以是wav,ogg等格式。  
    # 音频文件的内容会被全部载入到内存中。  
    SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt)
    SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)
    SOUNDS['point']  = pygame.mixer.Sound('assets/audio/point' + soundExt)
    SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt)
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    while True:
        # 选择随机的背景图片
        randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1)
        IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert()

        # 选择随机玩家图片
        randPlayer = random.randint(0, len(PLAYERS_LIST) - 1)
        # 小鸟的三种形态
        IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[randPlayer][0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[randPlayer][1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[randPlayer][2]).convert_alpha(),
        )

        # 选择随机管道图片，红色和绿色
        pipeindex = random.randint(0, len(PIPES_LIST) - 1)
        # 两个管道，一个倒着一个正着
        IMAGES['pipe'] = (
            # 旋转，将管道旋转180度
            pygame.transform.rotate(pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha(), 180),
            pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha(),
        )
        # hismask for pipes
        # 得到管道的边界mask  
        HITMASKS['pipe'] = (
            getHitmask(IMAGES['pipe'][0]),
            getHitmask(IMAGES['pipe'][1]),
        )

        # hitmask for player
        # 得到player的边界mask  
        HITMASKS['player'] = (
            getHitmask(IMAGES['player'][0]),
            getHitmask(IMAGES['player'][1]),
            getHitmask(IMAGES['player'][2]),
        )
        # 返回'playery'（player所在位置）,'basex'（base图像所在位置） 'playerIndexGen'（飞行姿势index）  
        movementInfo = showWelcomeAnimation()
        # 游戏失败，产生返回值
        # 其中包括
        #  'y': playery,
        # 'groundCrash': crashTest[1],
        # 'basex': basex,
        # 'upperPipes': upperPipes,
        # 'lowerPipes': lowerPipes,
        # 'score': score,
        # 'playerVelY': playerVelY,
        crashInfo = mainGame(movementInfo)
        showGameOverScreen(crashInfo)


def showWelcomeAnimation():
    """Shows welcome screen animation of flappy bird"""
    # index of player to blit on screen
    playerIndex = 0
    # [0,1,2,1]的一个循环
    playerIndexGen = cycle([0, 1, 2, 1])
    # 迭代器在每次迭代之后用于更改playerIndex
    # iterator used to change playerIndex after every 5th iteration
    loopIter = 0

    playerx = int(SCREENWIDTH * 0.2)
    playery = int((SCREENHEIGHT - IMAGES['player'][0].get_height()) / 2)

    messagex = int((SCREENWIDTH - IMAGES['message'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.12)
    # 初始时basex的值为0，表示地面从最左端显示
    # 之后它的值会变成-4，-8，-12...每达到-48(地面与背景的最大偏移量)，basex重新设为0
    # -4表示地面向左移动了4个像素，连续起来地面就像移动一样
    basex = 0
    # amount by which base can maximum shift to left
    # 算出'base'和 'backgroung'两张图的最大偏移量
    # 为循环展示地面base做准备，这里算出来是48
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()
    #  角色在欢迎屏幕上进行上下移动
    playerShmVals = {'val': 0, 'dir': 1}


    while True:
        ''' De-activated the press key functionality

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # make first flap sound and return values for mainGame
                SOUNDS['wing'].play()
                return {
                    'playery': playery + playerShmVals['val'],
                    'basex': basex,
                    'playerIndexGen': playerIndexGen,
                }
        '''
        SOUNDS['wing'].play()#播放飞的特效声音  
        return {#返回初始位置  进入maingame 
            'playery': playery + playerShmVals['val'],
            'basex': basex,
            'playerIndexGen': playerIndexGen,
        }


        # draw sprites
        # screen.blit(space, (0,0))可以绘制位图 第一个参数是加载完成的位图，第二个参数是绘制的起始坐标。 
        SCREEN.blit(IMAGES['background'], (0,0))
        SCREEN.blit(IMAGES['player'][playerIndex],
                    (playerx, playery + playerShmVals['val']))
        SCREEN.blit(IMAGES['message'], (messagex, messagey))
        SCREEN.blit(IMAGES['base'], (basex, BASEY)) 
        #更新窗口
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def mainGame(movementInfo):
    # 初始得分以及初始player的姿态以及迭代次数都为0  
    score = playerIndex = loopIter = 0
    # 得到飞行姿势
    playerIndexGen = movementInfo['playerIndexGen']
    # player所在位置 
    playerx, playery = int(SCREENWIDTH * 0.2), movementInfo['playery']

    basex = movementInfo['basex']
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()
    # 获取2个新的管道添加到upperPipes lowerPipes列表
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    # list of upper pipes
    # 两个上方管道的位置，x坐标变了，y没变
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]
    # list of lowerpipe
    # 对应上方管道的位置
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4
    # 角色速度，最大速度，向下加速度，襟翼加速度  
    # player velocity, max velocity, downward accleration, accleration on flap
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerMaxVelY =  10   # max vel along Y, max descend speed 最大下降速度
    playerMinVelY =  -8   # min vel along Y, max ascend speed 最大上升速度
    playerAccY    =   1   # players downward accleration 玩家向下加速
    playerFlapAcc =  -9   # players speed on flapping 玩家快速扑动
    playerFlapped = False # True when player flaps 当玩家扑动时是真的


    while True:
        # 后面lowerPipes[0]['x']在不停的更新(不断减4)，表示慢慢向左移动
        # 判断小鸟与第一个管道x的距离。如果大于-30，表示已经飞过去了，则换第二的管道
        if -playerx + lowerPipes[0]['x'] > -30: myPipe = lowerPipes[0]
        else: myPipe = lowerPipes[1]
        # 虽然在这里使用robot实现小鸟的飞行，这里的代码每什么用但是不能删去
        # 有这块点击事件，可以与robot一起玩(虽然你可能会捣乱)
        # 删去之后没了点击事件，关闭程序时会出错
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)):
                # playery是小鸟的位置在y方向的参数
                if playery > -2 * IMAGES['player'][0].get_height():#如果点击  
                    playerVelY = playerFlapAcc#上升  
                    playerFlapped = True
                    SOUNDS['wing'].play()#并播放飞行音效  
        # bot.act()返回true 表示小鸟扇动翅膀，false表示没动
        if  bot.act(-playerx + myPipe['x'], - playery + myPipe['y'], playerVelY ):
            playerVelY = playerFlapAcc #速度变为playerFlapAcc
            playerFlapped = True #表示小鸟扇动翅膀
            SOUNDS['wing'].play()
       
        # 检查撞击
        crashTest = checkCrash({'x': playerx, 'y': playery, 'index': playerIndex},
                               upperPipes, lowerPipes)
        if crashTest[0]:#如果掉在地上或者撞击到了管道，就返回结束游戏  
            # 更新q值
            bot.update_scores()
            return {
                'y': playery,
                'groundCrash': crashTest[1],
                'basex': basex,
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'score': score,
                'playerVelY': playerVelY,
            }

        # check for score
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            # 当角色达到管道缝隙的中间+4时，score+1，并且在此时播放得分音效  
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                SOUNDS['point'].play()
        # 改变小鸟和地面形态
        # playerIndex basex change
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerIndexGen)
        # 避免loopIter太大，每到三十重新循环
        loopIter = (loopIter + 1) % 30
        # 这里参数100是为了让basex的值刷新时地面看起来跟管道左移速度一致
        basex = -((-basex + 100) % baseShift)

        # 小鸟的动作
        # 如果小鸟当前的速度小于最大下降速度 切 小鸟并没有扇动翅膀
        if playerVelY < playerMaxVelY and not playerFlapped:
            # 小鸟下降速度变快，向下的加速度为1
            playerVelY += playerAccY
        # 如果扇动翅膀    
        if playerFlapped:
            # 扇动翅膀的flag回复为false
            playerFlapped = False
        # 获取当前形态的小鸟的高度
        playerHeight = IMAGES['player'][playerIndex].get_height()
        # 非常巧妙
        # 首先BASEY - playery - playerHeight表示小鸟底部聚地面的距离>0，等于零时触地
        # 如果小鸟的速度即playerVely为负，min()一定是playerVely，即小鸟向上飞
        # 如果小鸟的速度即playerVely为正，切min()是playerVely，表示小鸟还有下降的余地，结果为下降
        # 如果小鸟的速度即playerVely为正，切min()是BASEY - playery - playerHeight，表示小鸟落到地面上，避免沉入地下
        playery += min(playerVelY, BASEY - playery - playerHeight)

        # move pipes to left 将管道左移
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX

        # 当第一条管道即将触摸屏幕左侧时添加新的管道
        if 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        # 如果第一根管道离开了屏幕，则将其移除
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # 画图
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))



        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        # print score so player overlaps the score
        showScore(score)
        SCREEN.blit(IMAGES['player'][playerIndex], (playerx, playery))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def showGameOverScreen(crashInfo):
    """crashes the player down and shows gameover image"""
    score = crashInfo['score']
    playerx = SCREENWIDTH * 0.2
    playery = crashInfo['y']
    playerHeight = IMAGES['player'][0].get_height()
    playerVelY = crashInfo['playerVelY']
    playerAccY = 2

    basex = crashInfo['basex']

    upperPipes, lowerPipes = crashInfo['upperPipes'], crashInfo['lowerPipes']

    # play hit and die sounds
    SOUNDS['hit'].play()
    if not crashInfo['groundCrash']:
        SOUNDS['die'].play()

    while True:
        ''' De-activated press key functionality
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery + playerHeight >= BASEY - 1:
                    return
        '''
        return ### 必须删除才能激活按键功能

        # player y shift
        if playery + playerHeight < BASEY - 1:
            playery += min(playerVelY, BASEY - playery - playerHeight)

        # player velocity change
        if playerVelY < 15:
            playerVelY += playerAccY

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        showScore(score)
        SCREEN.blit(IMAGES['player'][1], (playerx,playery))

        FPSCLOCK.tick(FPS)
        pygame.display.update()


def playerShm(playerShm):
    """
    在8和-8之间振荡playerShm['val']的值
    oscillates the value of playerShm['val'] between 8 and -8"""
    if abs(playerShm['val']) == 8:
        playerShm['dir'] *= -1

    if playerShm['dir'] == 1:
         playerShm['val'] += 1
    else:
        playerShm['val'] -= 1


def getRandomPipe():#随机生成随机高度的管道 
    """returns a randomly generated pipe"""
    # y of gap between upper and lower pipe
    gapY = random.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
    gapY += int(BASEY * 0.2)
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return [
        # 返回两个点，一个是上方管道绘图的起始点，一个是下方管道绘图的起始点
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]


def showScore(score):
    """在屏幕中心显示分数"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][digit].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) / 2

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][digit].get_width()


def checkCrash(player, upperPipes, lowerPipes):
    """如果玩家与基地或管道相撞，则返回True"""
    #player包括 飞行的位置和姿势
    pi = player['index']#飞行姿势 
    # 获取小鸟的宽度和高度
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()
 
    # if player crashes into ground 掉在地上  
    # 如果小鸟的底部触底，或者全部飞出窗口视为失败
    if (player['y'] + player['h'] >= BASEY - 1 ) or (player['y'] + player['h'] <= 0):
        return [True, True]
    else:
        # 创建一个小鸟的矩形框
        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])
        # 获取管道的长度和高度 这里管道的宽度是52，高度是320
        pipeW = IMAGES['pipe'][0].get_width()
        pipeH = IMAGES['pipe'][0].get_height()
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # 产生上下两个管道的矩形框
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            # player and upper/lower pipe hitmasks
            pHitMask = HITMASKS['player'][pi]
            uHitmask = HITMASKS['pipe'][0]
            lHitmask = HITMASKS['pipe'][1]
            # 如果鸟与管道或管道相撞
            # if bird collided with upipe or lpipe 
            uCollide = pixelCollision(playerRect, uPipeRect, pHitMask, uHitmask)
            lCollide = pixelCollision(playerRect, lPipeRect, pHitMask, lHitmask)

            if uCollide or lCollide:#如果撞击到了上管道或者下管道 返回  
                return [True, False]

    return [False, False]

def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    """检查两个对象是否碰撞，而不仅仅是它们的矩形框"""
    rect = rect1.clip(rect2) #角色和管道之间重合的情况  
    # 先检测重合矩形框是否存在，若矩形框都没有重合，则一定没发生碰撞
    if rect.width == 0 or rect.height == 0:
        return False
    # 下面检测矩形框内的图像是否发生碰撞
    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y
    # 若两个图像矩形框内的hitmask(像素所在的位置)发生重合，则判断为碰撞
    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False

def getHitmask(image):
    """
    使用图像的alpha返回一个hitmask。
    获取像素所在的位置，有为true。没有则为false
    returns a hitmask using an image's alpha.
    """
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask

if __name__ == '__main__':
    main()
