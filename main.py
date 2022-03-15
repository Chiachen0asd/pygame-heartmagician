#################
#By 30903江冠締  #
#################

#### 導入插件
import sys       # 系統
import pygame       # 遊戲插件
import random       # 隨機取數

pygame.init()#pygame預設

#### 變數
P=[] # 存取21張牌
S=[] # 打亂排序用
CARDS=[] # 存取印出文件格式
clicked = 0  # 可以發牌
keyed = 0 #點擊鍵盤
Times = 0 #次數

#### 視窗尺寸
windowsize = [1080,720]    #(width 1080 * height 720)
#### 設定視窗以變數Screen存取
screen = pygame.display.set_mode(windowsize)
#### pagetitle
pygame.display.set_caption('心靈魔術師') 
#### 顏色設定
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')
red = pygame.color.Color('#FF0000')
green = pygame.color.Color('#00FF00')
blue = pygame.color.Color('#0000FF')
aqua = pygame.color.Color('#03b4ff')
purple = pygame.color.Color('#b153e1')
yellow = pygame.color.Color('#fff700')
pink = pygame.color.Color('#ffd4fc')
gray = pygame.color.Color('#d5d5d5')
darkgray = pygame.color.Color('#616161')
gold = pygame.color.Color('#F0E68C')

#### 文字物件
    # 設定文字格式 (font style name ,font size)
font1 = pygame.font.Font('font1.ttf',48)
font2 = pygame.font.Font('font2.TTC',20)
    # 建立文字物件(text,font smooth ,font color ,background)
titletext = font1.render('心靈魔術師',True,white,black)
subtitle = font2.render('由我來解鎖你心中的秘密',True,aqua,white)
hittext = font2.render('點擊左鍵發牌',True,black,white)
col1= font2.render('第一排',True,purple)
col2= font2.render('第二排',True,purple)
col3= font2.render('第三排',True,purple)
#### 導入圖片物件
imgback = pygame.image.load("54/back2.jpg") # 讀取圖片檔案
bgimg =  pygame.image.load("54/back3.jpg")
#### 函數區

#### 隨機取21張撲克牌
def pickcards():
    # 在陣列中放入1~54
    for i  in range(1,55,1):
        P.append(i)

    while ((len(P) - 1) >= 21):     # 迴圈判斷陣列長是否大於a(21)
        # 隨機 0 ~ n 取數(index)
        rc = random.randint(0,(len(P)-1))
        # 刪掉所取之數(index)
        P.remove(P[rc])  
    
#### 隨機洗牌
def randomsortcards():

    # 建立1~20之迴圈
    for i in range(0,21,1):
        # 隨機取數
        rc = random.randint(0,(len(P)-1))
        # 將n陣列之內容導至g陣列
        S.append(P[rc])
        P.remove(P[rc])

#### 導入圖片物件
def printcardimg():
    for i in range(0,21,1):
        # 導入撲克牌位置
        locals()['card'+str(i)] = pygame.image.load('54/'+str(S[i])+'.jpg')
    for i in range(0,21,1):
        # 將物件格式存入CARDS陣列
        CARDS.append(locals()['card'+str(i)])

#### 撲克牌移動 物件
def rectcardimg():
    for i in range(0,21,1):
        
        globals()['cardrect'+str(i)] = CARDS[i].get_rect()   
        globals()['cardrect'+str(i)].left = 900  # 設定 X 軸位置 
        globals()['cardrect'+str(i)].top = 750   # 設定 Y 軸位置
#### 更新視窗
def screenblit():
    #### 視窗背景顏色
    screen.fill(gray)
    #### 印出物件(物件格式,(座標))
    screen.blit(imgback,(900,400))
    screen.blit(titletext,(350,30))
    screen.blit(subtitle,(600,50))
    screen.blit(hittext,(900,370))
    screen.blit(col1,(125,100))
    screen.blit(col2,(325,100))
    screen.blit(col3,(525,100))
def Sort(N,col):    #更改位置
    Control = []    #建立陣列(每次執行時都會清空)
    N_sort = [] 
    for i in range(0,21,1):
        Control.append((i%3)+1)     #在對應的陣列中依順序寫入排數
    
    for i in range(0,21,3):     # 判斷Control陣列中的數值是否與使用者輸入排數相同
        if (Control[i] != col):     #分別使用不同迴圈原因為同一排的要先放
            N_sort.append(N[i])     #所以分別先偵測"不是"所選的排數，並放入N_sort陣列
    for i in range(1,21,3):     
        if (Control[i] != col):
            N_sort.append(N[i])
    for i in range(2,21,3):
        if (Control[i] != col):
            N_sort.append(N[i])


    note = 7    #先設定變數note之值
#array.insert(index,element)
    for i in range(0,21,1):     # 判斷Control陣列中的數值是否與使用者輸入排數相同
        if (Control[i] == col):
            N_sort.insert(note,N[i])    #利用insert函數在 N_sort[note]的地方放入N[i]
            note += 1   #同時note + 1
    #print(N_sort)   #輸出最終的N_sort
    N = N_sort
    global Times    #宣告全域變數
    Times += 1      #Times + 1
    #print('Times=',Times)
    #我討厭
    return N    #返回陣列N值

#### 函數使用區
pickcards()     # 隨機取21張撲克牌
randomsortcards()  # 隨機洗牌
printcardimg()  # 導入圖片物件

rectcardimg()   # 撲克牌移動物件
screenblit()    #更新視窗

#### 遊戲偵測主程式
while True:
    # 更新視窗
    pygame.display.flip()
    # 點擊偵測滑鼠按鍵
    keys = pygame.key.get_pressed()
    click = pygame.mouse.get_pressed()
    # 偵測點擊左鍵 及 是否可以點擊(clicked => 0)
    if (click[0]== 1 and clicked == 0):
        clicked = 1 # 變成不可點擊
        
        screenblit()    #更新視窗
        for i in range(0,21,1):
            globals()['cardrect'+str(i)].left = 900 # 設定 x 軸座標
            globals()['cardrect'+str(i)].top = 750 # 設定 y 軸座標

        for i in range(0,21,1):
            speed=[-5,-2] #控制移動距離
            
            #設定牌的最後位置
         
            x = 100 + (i%3)*200 
            y = (150+60*(i//3))
            
            ####迴圈偵測及移動撲克牌
            while(globals()['cardrect'+str(i)].left > x) or (globals()['cardrect'+str(i)].top > y):
                globals()['cardrect'+str(i)] = globals()['cardrect'+str(i)].move(speed) # 移動位置 (座標)
                screen.blit(CARDS[i],globals()['cardrect'+str(i)]) # 印出撲克牌
                
                pygame.display.flip() # 更新視窗
                
                
                if (globals()['cardrect'+str(i)].left == x): # 若撲克牌 X 軸到達位置 => X 軸移動為0 
                    speed[0] = 0
                if (globals()['cardrect'+str(i)].top == y): # 若撲克牌 Y 軸到達位置 => Y 軸移動為0
                    speed[1] = 0
                if ((speed[0] == 0) and (speed[1] == 0)): # 若撲克牌到達位置 => 跳出迴圈
                    break
                screen.blit(bgimg,globals()['cardrect'+str(i)]) #印出背景圖片
            hittext2 = font2.render('按鍵盤上1、2、3，',True,black,white)   #更改提示文字
            hittext = font2.render('打出你選擇牌的排數',True,black,white)
            screen.blit(hittext2,(850,350))     #印出提示文字
            screen.blit(hittext,(850,370))
            pygame.display.flip()   #更新視窗
    keys = pygame.key.get_pressed() #變數key儲存點擊鍵盤含函式
    if keys[pygame.K_1]:   #判斷按鍵 => 進行迴圈
        col = 1     #第一排
        keyed = 1
    elif keys[pygame.K_KP1]:
        col = 1    #第一排
        keyed = 1
    elif keys[pygame.K_2]: 
        col = 2     #第二排
        keyed = 1
    elif keys[pygame.K_KP2]: 
        col = 2     #第二排
        keyed = 1
    elif keys[pygame.K_3]:
        col = 3     #第三排
        keyed = 1
    elif keys[pygame.K_KP3]:
        col = 3     #第三排
        keyed = 1
    while (clicked == 1 and keyed == 1):    #當點擊滑鼠後同時點擊鍵盤
        CARDS = Sort(CARDS,col)     #執行函式
        hittext = font2.render('點擊左鍵發牌',True,black,white) #更改提示文字
        clicked = 0 #返回可點擊
        screenblit()    #更新視窗
    if (clicked == 0):  #若
        keyed = 0
        col = 0
    if (Times == 3):
        answer = CARDS[10]
        hittext = font1.render('你選的牌是:',True,red)
        screen.blit(hittext,(200,200))
        screen.blit(answer,(200,300))

        clicked = -1
        Times = -1

    #事件與遊戲迴圈
    for event in pygame.event.get():
        #pygame.time.Clock().tick(60)
        
        #偵測關閉事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
