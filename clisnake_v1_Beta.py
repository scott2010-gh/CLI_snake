import os, random, time
global length,ix,iy,dx,dy,size,t,lx,ly,game
try:
    import keyboard #keyboard 모듈 불러오기를 시도
except:
    print('Installing keyboard library on computer...')
    os.system('pip install keyboard')
    try:
        import keyboard
        print('Successfully installed! Please restart the program.')
    except:
        print("Can't install keyboard module... please check python pip.") 
ui = "=                                                     ="

gameover = ['Game Over']
game = []
player = ['0/0']
before = []
length=1
dx=1
dy=0
t = 0
lx=1
ly=0
gamev = True

def print_messagebox(l):
    os.system('cls')
    print("=======================================================")
    print(ui)
    for i in range(len(l)):
        f = int((len(ui)-len(l[i]))/2)
        b = int(f+len(l[i]))
        print(ui[:f]+l[i]+ui[b:])
    print(ui)
    print("=======================================================")
def check_key():
    global dx,dy
    if keyboard.is_pressed("Right"):
        dx=1
        dy=0
    elif keyboard.is_pressed("Left"):
        dx=-1
        dy=0
    elif keyboard.is_pressed("UP"):
        dx=0
        dy=-1
    elif keyboard.is_pressed("Down"):
        dx=0
        dy=1
def refresh():
    global length,ix,iy,dx,dy,size,t,lx,ly,gamev
    t +=1
    if t%2000 == 0:
        os.system('cls')
        game = []
        for i in range(int(size.split('x')[1])):
            game.append('□'*int(size.split('x')[0]))
        for a in range(len(game)):
            if a==iy:
                game[a] = game[a][:ix]+"◈"+game[a][ix+1:]
            for b in range(len(player)):
                px = int(player[b].split('/')[0])
                py = int(player[b].split('/')[1])
                if a==py:
                    game[a] = game[a][:px]+"■"+game[a][px+1:]
            print(game[a])
        before = player.copy()
        check_key()
        px = int(player[0].split('/')[0])+dx
        py = int(player[0].split('/')[1])+dy
        player[0] = str(px)+'/'+str(py)

        if not len(player)==1:
            for c in range(1,len(player)):
                bx = int(before[c-1].split('/')[0])
                by = int(before[c-1].split('/')[1])
                player[c] = str(bx)+'/'+str(by)
            
        if int(player[b].split('/')[0])==ix and int(player[b].split('/')[1])==iy:
            while int(player[b].split('/')[0])==ix and int(player[b].split('/')[1])==iy:
                ix = random.randrange(0,int(size.split('x')[0])-1)
                iy = random.randrange(0,int(size.split('x')[1])-1)
            length +=1
            px = int(player[b].split('/')[0])-lx
            py = int(player[b].split('/')[1])-ly
            player.append(str(px)+'/'+str(py))
            lx = dx
            ly = dy
        print("[ score | "+str(length)+" ]")
        if int(player[0].split('/')[0])<0 or int(player[0].split('/')[0])>int(size.split('x')[0]) or int(player[0].split('/')[1])<0 or int(player[0].split('/')[1])>int(size.split('x')[1]):
            gamev=False
            gameover.append("Your Score : "+str(length))
            print_messagebox(gameover)
size = input("Enter game board size >> ")
ix = random.randrange(0,int(size.split('x')[0])-1)
iy = random.randrange(0,int(size.split('x')[1])-1)
while gamev:
    check_key()
    refresh()
    check_key()
