#-*-coding: UTF-8 -*-
import pygame #导入各类库
import sys
import random
import time
def errorcheck(): #错误输入捕捉
    pygame.init()
    font=pygame.font.SysFont('m s 明朝',24) #导入字体
    text00=font.render('输入错误，请重新输入', True, (0, 0, 0)) #创建文本
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        screen.fill((255,255,255)) #清空显示屏
        screen.blit(text00,(400,800)) #显示文本
def main(text000): #显示输入框，并接收键盘输入
    pygame.init()
    textbox_rect=pygame.Rect(430, 300, 200, 30)
    font=pygame.font.SysFont('m s 明朝', 24) #导入字体
    global text #引入各类全局变量
    text=''
    global flag
    global flagflag
    global jl
    while True:
        for event in pygame.event.get(): #检测玩家输入
            if event.type==pygame.QUIT:
                pygame.quit()
                return
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    text=text[:-1] # 删除最后一个字符
                elif flag==11 and event.key==pygame.K_RETURN: #更改指针数值，返回主程序
                    flag=2 #更改指针数值
                    flagflag=1
                    return text
                elif event.key==pygame.K_RETURN and flagflag==3: #更改指针数值，返回主程序
                    flagflag=2 #更改指针数值
                    return text
                elif event.key==pygame.K_x and flagflag==3: #更改指针数值，返回主程序
                    flagflag=2 #更改指针数值
                    return text
                elif event.key==pygame.K_RETURN and flagflag!=3: #更改指针数值，返回主程序
                    flagflag=1 #更改指针数值
                    return text
                elif event.key==pygame.K_x and flagflag!=3: #更改指针数值，返回主程序
                    flagflag=1 #更改指针数值
                    return text
                else:
                    text+=event.unicode #增加文本内容
        screen.fill((255, 255, 255)) #清空屏幕内容
        screen.blit(text000,(350,200)) #显示文本
        pygame.draw.rect(screen, (0, 0, 0), textbox_rect, 2) # 绘制矩形框
        text_surface=font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (textbox_rect.x + 5, textbox_rect.y + 5))
        pygame.display.flip()
money=random.randint(600,1000) #生成各随机数
health=random.randint(45,100)
study=[0,0,0,0,0,0,0,0] #创建各类变量
xf=0 #学分
total=0 #总学分
zstudy=0 #总绩点
zxx=0 #总学习点
zsj=0 #总休息点
zyx=0 #总娱乐点
zdl=0 #总锻炼点
jl=100 #精力点
i=1 #用于在while循环中模拟实现for循环的功能
xx=qs=yx=dl=0
flag1=1 #模拟学期
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("背景音乐.mp3") #加载MP3文件
pygame.mixer.music.play() #播放mp3文件
clock=pygame.time.Clock()
img=pygame.image.load("人物.jpg") #导入角色图片
img=pygame.transform.scale(img,(100,100))  #可以将角色缩放
img1=pygame.image.load("图书馆.jpg") #导入图书馆图片
img1=pygame.transform.scale(img1,(250,250))  #缩小图片
img2=pygame.image.load("寝室.jpg") #导入图书馆图片
img2=pygame.transform.scale(img2,(250,250))  #缩小图片
img3=pygame.image.load("操场.jpg") #导入图书馆图片
img3=pygame.transform.scale(img3,(250,250))  #缩小图片
pos=img.get_rect() #记录图片位置
screen=pygame.display.set_mode((1200, 800)) #设置窗口大小
speedx=5 #设置移动速度
speedy=5
font=pygame.font.SysFont('华文仿宋', 30) #导入系统字体
screen.fill((255,255,255)) #用纯色清空屏幕
c=1
zstudy=0
total=0
#创建各类文本
text01=font.render('图书馆', True, (0, 0, 0))
text02=font.render('寝室', True, (0, 0, 0))
text03=font.render('操场', True, (0, 0, 0))
text04=font.render('睡觉', True, (0, 0, 0))
text05=font.render('打游戏', True, (0, 0, 0))
text1=font.render('欢迎来到模拟校生游戏', True, (0, 0, 0))
text2=font.render('按z键开始游戏', True, (0, 0, 0))
text3=font.render('这是您来到大学的第'+str(c)+'年', True, (0, 0, 0))
text4=font.render('毕业要求总学分为200，总均绩24', True, (0, 0, 0))
text5=font.render('您现在的状态是'+'金钱'+str(money)+' 健康'+str(health)+' 上学期的均绩'+str(round(study[i-2],2)), True, (0, 0, 0))
text6=font.render('按空格键继续', True, (0, 0, 0))
text11=font.render('请输入本学期您所修的学分', True, (0, 0, 0))
text7=font.render('您现有'+str(jl)+'点行动点,请输入您要分配的行动点,按x键返回', True, (0, 0, 0))
text8=font.render("您已获得的总学分为"+str(total)+"\n您已获得的总均绩"+str(zstudy), True, (0, 0, 0))
text9=font.render('很抱歉，因不可抗力，您未能毕业', True, (0, 0, 0))
text10=font.render('恭喜您，成功毕业', True, (0, 0, 0))
flag=0  #创建指针1
flagflag=0   #创建指针2
pygame.display.set_caption("模拟校生") #更改游戏标题
textbox_rect = pygame.Rect(100, 100, 200, 30)
text=""
tt1=""
tt2=""
tt3=""
tt4=""
pygame.mouse.set_visible(False)  # 隐藏鼠标
while True:
    clock.tick(60) #每秒不超过60帧的速度运行
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()  # 获取键盘状态
    zxx=zsj=zyx=zdl=0 #重置各点数
    font = pygame.font.SysFont('华文仿宋',30) #重新导入字体，防止乱码
    if flag1==1: #秋冬学期
        text3=font.render('这是您来到大学的第'+str(c)+'年秋冬学期', True, (0, 0, 0))
        text5=font.render('您现在的状态是'+'金钱'+str(money)+' 健康'+str(health)+' 上学期的均绩'+str(round(study[i-2],2)), True, (0, 0, 0))
    elif flag1==-1: #春夏学期
        text3=font.render('这是您来到大学的第'+str(c)+'年春夏学期', True, (0, 0, 0))
        text5=font.render('您现在的状态是'+'金钱'+str(money)+' 健康'+str(health)+' 上学期的均绩'+str(round(study[i-2],2)), True, (0, 0, 0))
    if flag==0:
        screen.blit(text1, (400, 300)) #显示对应文本
        screen.blit(text2, (400, 400)) #显示对应文本
    if flag==0 and key[K_z]: #利用指针与键盘输入推进游戏进程
        screen.fill((255,255,255)) #清空屏幕
        screen.blit(text3, (400, 300)) #显示对应文本
        screen.blit(text4, (400, 350)) #显示对应文本
        screen.blit(text5, (400, 400)) #显示对应文本
        screen.blit(text6, (400, 450))
        flag=10 #更改指针数值
    if flag==7:
        screen.fill((255,255,255))
        screen.blit(text3, (400, 300))
        screen.blit(text4, (400, 350))
        screen.blit(text5, (400, 400))
        screen.blit(text6, (400, 450))
        flag=10
    # 用键盘控制角色上下移动
    if key[K_UP] and pos.top > 0:  # 如果方向键上按下，并且没有超过上边界
        pos.y -= speedy  # 向上移动一个速度的值
    if key[K_DOWN] and pos.bottom < 800:  # 如果方向键下按下，并且没有超过下边界
        pos.y += speedy  # 向下移动一个速度的值
    if key[K_LEFT] and pos.left > 0:  # 如果方向键左按下，并且没有超过左边界
        pos.x -= speedx  # 向左移动一个速度的值
    if key[K_RIGHT] and pos.right < 1200:  # 如果方向键右按下，并且没有超过右边界
        pos.x += speedx  # 向右移动一个速度的值
    if flagflag==1:
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(img, pos)  # 绘制图像
        screen.blit(text01,(0,0))
        screen.blit(img1,(0,50))
        screen.blit(img2,(400,50))
        screen.blit(img3,(900,50))
        screen.blit(text02,(500,0))
        screen.blit(text03,(1000,0))
    if flagflag==1 and pos.top<=100 and pos.right<=200 and key[K_z]: #检测玩家位置以及是否推进游戏进度
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(img, pos)  # 绘制图像
        screen.blit(text04,(0,0))
        screen.blit(text05,(300,0))
        flagflag=5
    if flagflag==1 and pos.top<=200 and 400<=pos.right<=600 and key[K_z]: #检测玩家位置以及是否推进游戏进度
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(img, pos)  # 绘制图像
        screen.blit(text04,(0,0)) #显示对应文本
        screen.blit(img2,(400,100))
        screen.blit(text05,(300,0)) #显示对应文本
        flagflag=2
    if flagflag==1 and pos.top<=200 and 800<=pos.right<=1200 and key[K_z]: #检测玩家位置以及是否推进游戏进度
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(img, pos)  # 绘制图像
        screen.blit(text04,(0,0)) #显示对应文本
        screen.blit(text05,(300,0)) #显示对应文本
        flagflag=6
    if flagflag==2:
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(img, pos)  # 绘制图像
        screen.blit(text04,(200,400)) #显示对应文本
        screen.blit(text05,(800,400)) #显示对应文本
    if flagflag==2 and pos.top<=200 and pos.right<=200 and key[K_z]: #检测玩家位置以及是否推进游戏进度
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(img, pos)  # 绘制图像
        screen.blit(text04,(200,400)) #显示对应文本
        screen.blit(text05,(800,400)) #显示对应文本
    if flagflag==2 and 200<=pos.top<=400 and 250<=pos.right<=450 and key[K_z]: #检测输入方位
        flagflag=3
    if flagflag==2 and 200<=pos.top<=400 and 750<=pos.right<=950 and key[K_z]: #检测输入方位
        flagflag=4
    if flag==10 and key[K_SPACE]: #利用指针与键盘输入推进游戏进程
        flag=11
    if flag==11:
        if __name__=="__main__":
            text11=font.render('请输入本学期您所修的学分', True, (0, 0, 0))
            main(text11) #调用显示矩形框的函数
            try: #错误捕捉，防止报错
                xf=int(text) 
                zxf=zxf+xf
            except:
                errorcheck()
    if flagflag==3:
        if __name__=="__main__":
            text7=font.render('您现有'+str(jl)+'点行动点,请输入您要分配的行动点,按x键返回', True, (0, 0, 0))
            main(text7) #调用显示矩形框的函数
            try:
                jl=jl-int(text)
                sj=int(text) #给目的变量sj赋值
                zsj=zsj+sj #将sj累加入zsj，记录多次输入
            except:
                errorcheck()
    if flagflag==4:
        if __name__=="__main__":
            text7=font.render('您现有'+str(jl)+'点行动点,请输入您要分配的行动点,按x键返回', True, (0, 0, 0))
            main(text7) #调用显示矩形框的函数
            try:
                jl=jl-int(text)
                yx=int(text) #给目的变量yx赋值
                zyx=zyx+yx #将yx累加入zyx，记录多次输入
            except:
                errorcheck()
    if flagflag==5:
        if __name__=="__main__":
            text7=font.render('您现有'+str(jl)+'点行动点,请输入您要分配的行动点,按x键返回', True, (0, 0, 0))
            main(text7) #调用显示矩形框的函数
            try:
                jl=jl-int(text)
                xx=int(text) #给目的变量xx赋值
                zxx=zxx+xx #将xx累加入zxx，记录多次输入
            except:
                errorcheck()
    if flagflag==6:
        if __name__=="__main__":
            text7=font.render('您现有'+str(jl)+'点行动点,请输入您要分配的行动点,按x键返回', True, (0, 0, 0))
            main(text7)
            try:
                jl=jl-int(text)
                dl=int(text) #给目的变量dl赋值
                zdl=zdl+dl #将dl累加入zdl，记录多次输入
            except:
                errorcheck()
    if flagflag==2 and key[K_x]: #检测玩家是否想回到上一界面
        flagflag=1
    if jl==0: #检测精力点是否消耗完毕，消耗完毕则进入下一学期
        jl=100 #重置精力点
        flag=7 #更改指针1数值
        flagflag=0 #更改指针2数值
        if zsj<30:
            health=health-random.randint(0,20)
        if 30<=zsj<=70:
            health=health+random.randint(-10,20)
        if 70<zsj<=100:
            health=health+random.randint(10,30)
        if health<50:
            b=random.randint(-20,0)
        else:
            b=random.randint(0,20)
        #考虑身体欠恙未能顺利毕业
        if health<40:
            flag=100
        #根据算法给本学期均绩、健康赋值
        if zxx<30:
            study[i-1]=random.randint(2,3)-random.randint(0,xf)/60+b/60
        if 30<=zxx<60:
            study[i-1]=random.uniform(3,4.2)-random.randint(0,xf)/60+b/60
        if 60<=zxx<80:
            study[i-1]=random.uniform(4,4.8)-random.randint(0,xf)/60+b/60
        if 80<=zxx<=100:
            study[i-1]=random.uniform(4.3,5)-random.randint(0,xf)/60+b/60
        if study[i-1]>5:
            study[i-1]=5
        total=total+xf
        zstudy=round(study[i-1],2)+zstudy
        zstudy=round(zstudy,2)
        i+=1
        flag1=-flag1 #模拟秋冬学期、春夏学期
        c=c+i%2
    if flag==100:
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(text9,(400,400)) #显示文本
    if i==9 and total>=200 and zstudy>=24:
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(text10,(800,400)) #显示文本
    elif i==9:
        screen.fill((255,255,255))  # 用纯色填充窗口
        screen.blit(text9,(800,400)) #显示文本
    pygame.display.flip()