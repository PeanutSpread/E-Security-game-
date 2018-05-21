import pygame
import random
pygame.mixer.init()
pygame.init()

# A class for allowing images to be animated with ease from sprite sheets.
class anim(object):

    # Getting the information required for the entire class.
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name)

    # Making part of the original sprite sheet its own message.
    def get_image(self, x, y, width, height, truth):
        image = pygame.Surface([width, height]) 
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        if truth == True:
            image.set_colorkey((0,0,0))
        # Returning the image.
        return image

# Used for the vertical movement of the enemies
def enemyy (player_positiony,y,mode,amount):
    if player_positiony - 15 > y:
        y += amount
        if mode == True:
            y += 2
    if player_positiony - 15 < y:
        y -= amount
        if mode == True:
            y -= 2
    return y

# Used for the horizontal movement of the enemies
def enemyx(player_positionx,x,mode,amount):
    if player_positionx - 20 > x:
        x += amount
        if mode == True:
            x += 2
    if player_positionx + 40 < x:
        x -= amount
        if mode == True:
            x -= 2
    return x
        
# Used for the horizontal movement of the player
def movementx(xc,left,right,jumping):  
    
    if left == True and xc > -34:
        if jumping == True:
            xc -= 8
        else:
            xc -= 5

    if right == True and xc < 720:
        if jumping == True:
            xc += 8
        else:        
            xc += 5
        
    return xc
    
# used for the vertical movement of the player
def movementy(yc,up,down,jumping):
    
    if up == True and yc < 480:
        if jumping == True:
            yc += 8
        else:        
            yc += 5
    
    if down == True and yc > 194:
        if jumping == True:
            yc -= 8
        else:        
            yc -= 5  
        
    return yc
        
# Setting up the game window.
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
myClock = pygame.time.Clock()
pygame.mouse.set_visible(False)
# Loading Screen
load = pygame.image.load('Hominid.png')
screen.blit(load,(0,0))
pygame.display.flip()
pygame.display.set_caption('E-Security')

# Defining the constants of colours.
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BACKER = (0,0,100)
RAND = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# Loading the individual frames of each image.
#Computer Chip Image
Background = anim('comp_chip.png')
Back_me_up = Background.get_image(0,0,1600,1200, True)
# Game Over Animation
Game_Over = anim('Game_Over.png')
Over = [Game_Over.get_image(0,0,672,280,True),Game_Over.get_image(672,0,672,280,True),Game_Over.get_image(1344,0,672,280,True),Game_Over.get_image(2016,0,672,280,True),Game_Over.get_image(2688,0,672,280,True),Game_Over.get_image(3360,0,672,280,True),Game_Over.get_image(4032,0,672,280,True),Game_Over.get_image(4032,0,672,280,True)]
# Menu buttons and other assets
Menu = anim('Menu_assets.png')
Menu_buttons = [Menu.get_image(0,0,50,50, False),Menu.get_image(50,0,50,50, False),Menu.get_image(0,50,50,50, False),Menu.get_image(50,50,50,50, False),Menu.get_image(0,100,50,50, False),Menu.get_image(50,100,50,50, False),Menu.get_image(0,150,50,50, False),Menu.get_image(50,150,50,50, False),Menu.get_image(0,200,50,50, False),Menu.get_image(50,200,50,50, False),Menu.get_image(0,250,50,50, False),Menu.get_image(50,250,50,50, False),Menu.get_image(100,0,700,100, False),Menu.get_image(100,100,700,100, False),Menu.get_image(100,200,100,100, False),Menu.get_image(200,200,100,100, False),Menu.get_image(300,200,100,100, False),Menu.get_image(400,200,100,100, False),Menu.get_image(500,200,250,100, False),Menu.get_image(750,200,50,50, False),Menu.get_image(750,250,50,50, False)]
# Player Images
#45 frames, 1 - 12 punch and run, 13 - 16 jump, 17 - 20 crouch, 21 - 32 run, 33 - 45, punch
character = anim('Player.png')
Hacker = [character.get_image(0,0,120,120,True), character.get_image(120,0,120,120,True), character.get_image(240,0,120,120,True), character.get_image(360,0,120,120,True),character.get_image(480,0,120,120,True), character.get_image(600,0,120,120,True),character.get_image(720,0,120,120,True),character.get_image(840,0,120,120,True), character.get_image(960,0,120,120,True),character.get_image(1080,0,120,120,True),character.get_image(1200,0,120,120,True), character.get_image(1320,0,120,120,True),character.get_image(1440,0,120,120,True),character.get_image(1560,0,120,120,True), character.get_image(1680,0,120,120,True),character.get_image(1800,0,120,120,True),character.get_image(1920,0,120,120,True), character.get_image(2040,0,120,120,True),character.get_image(2160,0,120,120,True),character.get_image(2280,0,120,120,True), character.get_image(2400,0,120,120,True),character.get_image(2520,0,120,120,True),character.get_image(2640,0,120,120,True), character.get_image(2760,0,120,120,True), character.get_image(2880,0,120,120,True),character.get_image(3000,0,120,120,True), character.get_image(3120,0,120,120,True),character.get_image(3240,0,120,120,True),character.get_image(3360,0,120,120,True),character.get_image(3480,0,120,120,True),character.get_image(3600,0,120,120,True),character.get_image(3720,0,120,120,True),character.get_image(3840,0,120,120,True),character.get_image(3960,0,120,120,True),character.get_image(4080,0,120,120,True),character.get_image(4200,0,120,120,True),character.get_image(4320,0,120,120,True),character.get_image(4440,0,120,120,True),character.get_image(4560,0,120,120,True),character.get_image(4680,0,120,120,True),character.get_image(4800,0,120,120,True),character.get_image(4920,0,120,120,True),character.get_image(5040,0,120,120,True),character.get_image(5160,0,120,120,True),character.get_image(5280,0,120,120,True)]
# Special ingame mouse look
Mouse = anim('Mouse.png')
Point = [Mouse.get_image(0,0,32,32, True),Mouse.get_image(32,0,32,32,True)]
# Life Bar
Life = anim('Health.png')
Heal = [Life.get_image(15,0,34,7,True),pygame.transform.scale(Life.get_image(0,10,64,20,True),(192,60))]
# Aiming scope for player 2
Scope = anim('aim.png')
Aim = [pygame.transform.scale(Scope.get_image(0,0,38,50,True),(76,100)),pygame.transform.scale(Scope.get_image(38,0,38,50,True),(76,100)),pygame.transform.scale(Scope.get_image(76,0,38,50,True),(76,100)),pygame.transform.scale(Scope.get_image(114,0,38,50,True),(76,100)),pygame.transform.scale(Scope.get_image(152,0,38,50,True),(76,100)),pygame.transform.scale(Scope.get_image(190,0,38,50,True),(76,100))]

# The taller enemy's animations
Security = anim('Security.png')
Police = [pygame.transform.scale(Security.get_image(0,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(35,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(70,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(105,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(140,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(175,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(210,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(245,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(280,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(315,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(350,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(385,0,35,45,True),(105,135)),pygame.transform.scale(Security.get_image(420,0,35,45,True),(105,135))]

# Game Background
Street = anim('Street.png')
Road = [Street.get_image(0,0,800,600,False),Street.get_image(800,0,800,600,False),Street.get_image(1600,0,800,600,False),Street.get_image(2400,0,800,600,False),Street.get_image(3200,0,800,600,False),Street.get_image(0,600,800,600,False),Street.get_image(800,600,800,600,False),Street.get_image(1600,600,800,600,False),Street.get_image(2400,600,800,600,False),Street.get_image(3200,600,800,600,False),Street.get_image(0,1200,800,600,False),Street.get_image(800,1200,800,600,False),Street.get_image(1600,1200,800,600,False),Street.get_image(2400,1200,800,600,False),Street.get_image(3200,1200,800,600,False),Street.get_image(0,1800,800,600,False),Street.get_image(800,1800,800,600,False),Street.get_image(1600,1800,800,600,False),Street.get_image(2400,1800,800,600,False),Street.get_image(3200,1800,800,600,False),Street.get_image(0,2400,800,600,False),Street.get_image(800,2400,800,600,False),Street.get_image(1600,2400,800,600,False),Street.get_image(2400,2400,800,600,False),Street.get_image(3200,2400,800,600,False),Street.get_image(0,3000,800,600,False),Street.get_image(800,3000,800,600,False),Street.get_image(1600,3000,800,600,False),Street.get_image(2400,3000,800,600,False)]
# Death Animation
Dead = anim('playerdead.png')
Death = [Dead.get_image(0,0,120,120,True),Dead.get_image(120,0,120,120,True),Dead.get_image(240,0,120,120,True),Dead.get_image(360,0,120,120,True),Dead.get_image(480,0,120,120,True),Dead.get_image(600,0,120,120,True)]
Boxer = anim('enemy_box.png')
# Smaller enemy animations
Boxbub = [pygame.transform.scale(Boxer.get_image(0,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(46,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(92,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(138,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(184,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(230,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(276,0,46,45,True),(92,90)),pygame.transform.scale(Boxer.get_image(322,0,46,45,True),(92,90))]
# The controlls menu background
Pattern = anim('Pattern.png')
contback = [pygame.transform.scale(Pattern.get_image(0,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(80,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(160,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(240,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(320,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(400,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(480,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(560,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(640,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(720,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(800,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(880,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(960,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(1040,0,80,60,True),(800,600)),pygame.transform.scale(Pattern.get_image(1120,0,80,60,True),(800,600))]
# loading the cutscene
cutter = pygame.image.load('Hacker.png')
# loading the controls
keys = pygame.image.load('Keys.png')
mouse1 = pygame.image.load('click.png')

#loading main menu music
pygame.mixer.music.load('Galaxy.mp3')
shotbox = pygame.Rect(0,0,0,0)

# Getting all the fonts and text set up
fontMenu = pygame.font.SysFont("Impact",50)
fontMenu2 = pygame.font.SysFont("Impact",50)
fontDesc = pygame.font.SysFont("Impact",25)
fontDesc2 = pygame.font.SysFont("Impact",25)
text = fontMenu.render("E-Security",1,(0,255,0))
text2 = fontMenu2.render("E-Security",1,(0,0,0))
text3 = fontMenu.render("Play Game",1,(0,255,0))
text4 = fontMenu2.render("Play Game",1,(0,0,0))
text5 = fontMenu.render("Controls",1,(0,255,0))
text6 = fontMenu2.render("Controls",1,(0,0,0))
text7 = fontMenu.render("Players",1,(0,255,0))
text8 = fontMenu2.render("Players",1,(0,0,0))
text9 = fontMenu.render("Easy",1,(0,0,255))
text10 = fontMenu2.render("Easy",1,(0,0,0))
text11 = fontMenu.render("Hard",1,(255,0,0))
text12 = fontMenu2.render("Hard",1,(0,0,0))
text13 = fontMenu.render("Press back to return to the menu.",1,(0,255,255))
text14 = fontMenu2.render("Press back to return to the menu.",1,(0,0,0))
text15 = fontDesc.render("Punch left and punch right.",1,(0,255,255))
text16 = fontDesc2.render("Punch left and punch right.",1,(0,0,0))
text17 = fontDesc.render("Move up, down, left and right.",1,(0,255,255))
text18 = fontDesc2.render("Move up, down, left and right.",1,(0,0,0))
text19 = fontDesc.render("Crouch.",1,(0,255,255))
text20 = fontDesc2.render("Crouch.",1,(0,0,0))
text21 = fontDesc.render("Jump.",1,(0,255,255))
text22 = fontDesc2.render("Jump.",1,(0,0,0))
text23 = fontDesc.render("Shoot.",1,(255,255,0))
text24 = fontDesc2.render("Shoot.",1,(0,0,0))
text25 = fontDesc.render("Aim.",1,(255,255,0))
text26 = fontDesc2.render("Aim.",1,(0,0,0))
text27 = fontMenu.render("Player 1",1,(0,0,255))
text28 = fontMenu2.render("Player 1",1,(0,0,0))
text29 = fontMenu.render("Player 2",1,(255,0,0))
text30 = fontMenu2.render("Player 2",1,(0,0,0))

# Variables used for the placement of multiple moving objects
a = 0 # y variable for chip backgroud
b = 0 # y variable for chip backgroud
z = 20 # Used for animation by cycling through frames
x = 0 # mouse x loc
y = 0 # mouse y loc
p = 0 # used for main enemy animation
d = 0 # used for death animation
funimation = 0 # used for background in game animation
charx = 300 # Player x position
chary = 300 # Player y position
count = 0 # used for jumping animation
counter = 0 # used for crouching animation
state = 0 # Determining which menu you're in or if you are in game
but = True # game loop
time = 0 # making a timer for smooth animation
click = False # used for animation for the mouse
ply1 = False # for if 1 player is selected
ply2 = False # for if 2 players is selected
up = False # if the players input is up to be continuous
left = False # if the players input is left to be continuous
right = False # if the players input is right to be continuous
down = False # if the players input is down to be continuous
jump = False # if the players input is space to be continuous
jumping = False # if the players input was space to be continued after letting go
crouch = False # if the players input is ctrl to be continuous
crouching = False # if the players input was space to be continued after letting go
side = False # determining whether or not the character should face left
stop = False # making the character stop moving when crouched
music = "G" # what music is currntly playing
life = 4 # amount of player life
bar = 0 # health bar
variety = False # used for alternating in the game over screen
deathfx = False # death animation
noreplay = False # initiating deathfx
punch = False # for punching
punching = False # punching animation
county = 0 # enableing punching during certain frames
no_hit = False # making sure the enemies get hit once per punch
enemy_attack = False # allowing the enemies to attack
attacking = False # for when the enemies are attack
numto = 0 # cooldown for enemy attack
devmode = False # enabling devmode for frame data
change = False # used for determining whether devmode was previously held down
hard = False # game difficulty increase
ouch = True # stoping the boxes from dealing to much damage
recoil = 0 #player 2 cooldown
shoot = True # player 2 can shoot if true
noshot = False # cannot shoot if true
boxy = 0 # animation for the box enemies
gmovr = 0 # game over animations
boxcount = 0 # timer for box hitbox
wait = False # if the box enemy can deal damage
patty = 0 # animation for controls screen
cutscene = True #used for showing the story image

# timer
timetracker = pygame.time.get_ticks()

# locations and health of enemies
xloc = [700,700,700]
lastxloc = xloc
yloc = [random.randint(200,500),random.randint(200,500),random.randint(200,500)]
lastyloc = yloc
enemyh = [2,1,1]
dead = 0

# Setting up the music to play.
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


# Main game loop.
while but == True:
    
################################################################################
    
    # Main Menu
    if state == 0:
        
        # Background thats animated
        pygame.draw.rect(screen,RAND,(0,0,800,600))
        screen.blit(Back_me_up,(b,a))
        screen.blit(Menu_buttons[18],(275,80))
        screen.blit(text2,(294,92)) 
        screen.blit(text,(295,90))
        
        # Swapping button images based off mouse location
        if x <= 750 and x >=50 and y <= 450 and y >= 350:
            screen.blit(Menu_buttons[13],(50,350))
        else:
            screen.blit(Menu_buttons[12],(50,350))
        
        screen.blit(text6,(299,367))
        screen.blit(text5,(300,365))
            
        if x <= 750 and x >=50 and y <= 300 and y >= 200:
            screen.blit(Menu_buttons[13],(50,200))
        else:
            screen.blit(Menu_buttons[12],(50,200))
            
        screen.blit(text4,(289,217))
        screen.blit(text3,(290,215))
            
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Menu_buttons[1],(750,0))       
        else:
            screen.blit(Menu_buttons[0],(750,0))


################################################################################
   
    # Play Game
    if state == 1:
        
        # background images and text
        pygame.draw.rect(screen,RAND,(0,0,800,600))
        screen.blit(Back_me_up,(b,a))
        screen.blit(Menu_buttons[18],(275,220))
        screen.blit(Menu_buttons[18],(475,350))
        screen.blit(Menu_buttons[18],(75,350))
        screen.blit(Menu_buttons[18],(275,0))
        screen.blit(text4,(294,17)) 
        screen.blit(text3,(295,15))
        screen.blit(text8,(324,232)) 
        screen.blit(text7,(325,230))
        screen.blit(text10,(149,362)) 
        screen.blit(text9,(150,360))
        screen.blit(text12,(549,362)) 
        screen.blit(text11,(550,360))          
                
        # Swapping button images based off mouse location
        
        if x <600 and  x>550 and y<300 and y>250 or ply1 == True:
            screen.blit(Menu_buttons[5],(550,250))
        else:
            screen.blit(Menu_buttons[4],(550,250))
        
        if x <250 and  x>200 and y<300 and y>250 or ply2 == True:
            screen.blit(Menu_buttons[7],(200,250))
        else:
            screen.blit(Menu_buttons[6],(200,250))
        
        if x<246 and x>146 and y<560 and y>460:
            screen.blit(Menu_buttons[15],(146,460))
        else:
            screen.blit(Menu_buttons[14],(146,460))
                        
        if x<646 and x>546 and y<560 and y>460:  
            screen.blit(Menu_buttons[17],(546,460))
        else:
            screen.blit(Menu_buttons[16],(546,460))
        
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Menu_buttons[3],(750,0))          
        else:
            screen.blit(Menu_buttons[2],(750,0))
            
################################################################################    
    
    # Controls
    if state == 2:
        
        # Background images and text
        
        screen.blit(contback[patty],(0,0))
        screen.blit(Menu_buttons[18],(275,0))
        screen.blit(text6,(309,17)) 
        screen.blit(text5,(310,15))
        screen.blit(text28,(49,17)) 
        screen.blit(text27,(50,15))
        screen.blit(text30,(579,17)) 
        screen.blit(text29,(580,15))
        screen.blit(text16,(199,117)) 
        screen.blit(text15,(200,115))        
        screen.blit(text18,(199,277)) 
        screen.blit(text17,(200,275))
        screen.blit(text20,(199,437)) 
        screen.blit(text19,(200,435))
        screen.blit(text22,(399,557)) 
        screen.blit(text21,(400,555))
        screen.blit(text24,(699,157)) 
        screen.blit(text23,(700,155))
        screen.blit(text26,(699,457)) 
        screen.blit(text25,(700,455))            
        screen.blit(keys,(0,88)) 
        screen.blit(mouse1,(480,88)) 
        
        # Swapping button images based off mouse location.        
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Menu_buttons[3],(750,0))          
        else:
            screen.blit(Menu_buttons[2],(750,0))
            
################################################################################
    # Playing
    if state == 3:
        
        if cutscene == True:
            screen.blit(cutter,(0,0))
            if jump == True:
                cutscene = False
        else:
            # setting up the life bar
            if life > 0:
                if life == 1:
                    bar = 8
                elif life == 2:
                    bar = 5
                else:
                    bar = 0
                
                # background and life
                if devmode == True:
                    pygame.draw.rect(screen,WHITE,(0,0,800,600))
                    pygame.draw.rect(screen,YELLOW,(0,0,800,300))            
                else:
                    screen.blit(Road[funimation],(0,0))
                pygame.draw.ellipse(screen,BLACK,(0,0,192,60))
                pygame.draw.ellipse(screen,RED,(bar,0,48*life,60))
                screen.blit(Heal[1],(0,0))
                
                # drawing the player
                if side == True:
                    if jumping == False:
                        if crouch == False:
                            hitbox = pygame.Rect(charx+46,chary+8,60,90)
                            if devmode == True:
                                pygame.draw.rect(screen,RED,(charx+46,chary+8,60,90),5)
                        else:
                            hitbox = pygame.Rect(charx+46,chary+52,60,60)
                            if devmode == True:
                                pygame.draw.rect(screen,RED,(charx+46,chary+52,60,60),5)
    
                    if punch == True and jumping == False:
                        if z == 39 or z == 40 or z == 35 or z == 36 or z == 3 or z == 4 or z == 7 or z == 8:
                            punchbox = pygame.Rect(charx,chary+32,40,60)
                            if devmode == True:
                                pygame.draw.rect(screen,BLUE,(charx,chary+32,40,60),5)
                        
                    screen.blit(pygame.transform.flip(Hacker[z],True,False),(charx,chary))
                    
                else:
                    if jumping == False:
                        if crouch == False:
                            hitbox = pygame.Rect(charx+16,chary+8,60,90)
                            if devmode == True:
                                pygame.draw.rect(screen,RED,(charx+16,chary+8,60,90),5)
                        else:
                            hitbox = pygame.Rect(charx+16,chary+52,60,60)
                            if devmode == True:
                                pygame.draw.rect(screen,RED,(charx+16,chary+52,60,60),5)                        
                    if punch == True and jumping == False:
                        if z == 39 or z == 40 or z == 35 or z == 36 or z == 3 or z == 4 or z == 7 or z == 8:
                            punchbox = pygame.Rect(charx+85,chary+32,40,60)
                            if devmode == True:
                                pygame.draw.rect(screen,BLUE,(charx+85,chary+32,40,60),5)
                    
                    screen.blit(Hacker[z],(charx,chary))
                    
                if stop == False:
                    charx = movementx(charx,left,right,jumping)
                    chary = movementy(chary,up,down,jumping)
                
                    
                    # Drawing the tall enemy
                if enemyh[0] > 0:
                    if charx < xloc[0]:
                        hit = pygame.Rect(xloc[0] + 20 ,yloc[0],66,120)
                        if devmode == True:
                            pygame.draw.rect(screen,RED,(xloc[0] + 20 ,yloc[0],66,120),5)
                        screen.blit(pygame.transform.flip(Police[p],True,False),(xloc[0],yloc[0]))                    
                    
                    else:
                        hit = pygame.Rect(xloc[0] + 20 ,yloc[0],66,120)
                        if devmode == True:
                            pygame.draw.rect(screen,RED,(xloc[0] + 20 ,yloc[0],66,120),5)
                        screen.blit(Police[p],(xloc[0],yloc[0]))    
    
                # Drawing box #1
                if enemyh[1] > 0:
                    if charx < xloc[1]:
                        boxhit1 = pygame.Rect(xloc[1]+12,yloc[1]+62,60,62)
                        if devmode == True:
                            pygame.draw.rect(screen,RED,(xloc[1]+12,yloc[1]+62,60,62),5)
                        screen.blit(pygame.transform.flip(Boxbub[boxy],True,False),(xloc[1],yloc[1] + 50))                    
                    
                    else:
                        boxhit1 = pygame.Rect(xloc[1]+12,yloc[1]+12,60,62)
                        if devmode == True:
                            pygame.draw.rect(screen,RED,(xloc[1]+12,yloc[1]+62,60,62),5)
                        screen.blit(pygame.transform.flip(Boxbub[boxy],True,False),(xloc[1],yloc[1] + 50))
                
                # Drawing box #2
                if enemyh[2] > 0:
                    if charx < xloc[2]:
                        boxhit2 = pygame.Rect(xloc[2]+12,yloc[2]+62,60,62)
                        if devmode == True:
                            pygame.draw.rect(screen,RED,(xloc[2]+12,yloc[2]+62,60,62),5)
                        screen.blit(pygame.transform.flip(Boxbub[boxy],True,False),(xloc[2],yloc[2] + 50))                    
                    
                    else:
                        boxhit2 = pygame.Rect(xloc[2]+12,yloc[2]+62,60,62)
                        if devmode == True:
                            pygame.draw.rect(screen,RED,(xloc[2]+12,yloc[2]+62,60,62),5)
                        screen.blit(pygame.transform.flip(Boxbub[boxy],True,False),(xloc[2],yloc[2] + 50))    
                
                # determining if a 2nd player should be implemented
                if ply2 == False:
                    if click == True or recoil > 0:
                        if shoot == True:
                            if time % 10 == 0:
                                recoil += 1
                            if recoil > 4: 
                                recoil = 0
                                shoot = False
                        screen.blit(Aim[recoil],(x - 36,y - 60))
                        if recoil == 0:
                            shotbox = pygame.Rect(x,y,4,4)
                            if devmode == True:
                                pygame.draw.rect(screen,BLUE,(x,y,4,4),5)  
                    else:
                        screen.blit(Aim[0],(x - 36,y - 60))
                        shoot = True    
                        noshot = False
    
                        shotbox = pygame.Rect(0,0,0,0) 
                        if devmode == True:
                            pygame.draw.rect(screen,BLUE,(0,0,0,0),5)                      
                        
                # locations
                lastyloc[0] = yloc[0]
                lastxloc[0] = xloc[0]
                xloc[0] = enemyx(charx,xloc[0],hard,3)
                yloc[0] = enemyy(chary,yloc[0],hard,3)
                xloc[1] = enemyx(charx,xloc[1],hard,1)
                yloc[1] = enemyy(chary,yloc[1],hard,1)
                if enemyh[1] > 0 and time % 10 == 0:
                    xloc[2] += 2
                xloc[2] = enemyx(charx,xloc[2],hard,1)
                yloc[2] = enemyy(chary,yloc[2],hard,1)
                
                # if the enemy can attack
                if numto % 200 == True:
                    enemy_attack = True                
                
                # hit  boxes based off of health for the main enemy
                if enemyh[0] > 0:
                    if 7<= p <=9:
                        hitter = pygame.Rect(xloc[0],yloc[0]+50,100,70)
                        if devmode == True:
                            pygame.draw.rect(screen,GREEN,(xloc[0],yloc[0]+50,100,70),5)
                        if hitter.colliderect(hitbox) == 1:
                            if ouch == True:
                                life -= 1
                                ouch = False        
                                
                    
                    if hitbox.colliderect(hit) == 1:
                        numto += 1
                    else:
                        numto = 0
    
                        
                    if punch == True and no_hit == False:
                        if z == 39 or z == 40 or z == 35 or z == 36 or z == 3 or z == 4 or z == 7 or z == 8:
                            if punchbox.colliderect(hit) and time % 2 == 0:
                                if county % 3 == 0 or county % 7 == 0:
                                    enemyh[0] -= 1
                                    no_hit = True
                                    
                    if shotbox.colliderect(hit) == 1:
                        if noshot == False:
                            enemyh[0] -= 1
                            if devmode == True:
                                print ("hit")
                        noshot = True
    
                # hit  boxes based off of health for box #1
                if enemyh[1] > 0:
                    if shotbox.colliderect(boxhit1) == 1:
                        if noshot == False:
                            enemyh[1] -= 1
                            if devmode == True:
                                print ("hit")
                        noshot = True
                    
                    if punch == True and no_hit == False:
                        if z == 39 or z == 40 or z == 35 or z == 36 or z == 3 or z == 4 or z == 7 or z == 8:
                            if punchbox.colliderect(boxhit1) and time % 2 == 0:
                                if county % 3 == 0 or county % 7 == 0:
                                    enemyh[1] -= 1
                                    no_hit = True
                    
                    if wait == False:
                        if hitbox.colliderect(boxhit1) == 1:
                            life -= 1
                            if devmode == True:
                                print ("boxer")
                            wait = True
    
                # hit  boxes based off of health for box #2       
                if enemyh[2] > 0:
                    if shotbox.colliderect(boxhit2) == 1:
                        if noshot == False:
                            enemyh[2] -= 1
                            if devmode == True:
                                print ("hit")
                        noshot = True
                    
                    if punch == True and no_hit == False:
                        if z == 39 or z == 40 or z == 35 or z == 36 or z == 3 or z == 4 or z == 7 or z == 8:
                            if punchbox.colliderect(boxhit2) and time % 2 == 0:
                                if county % 3 == 0 or county % 7 == 0:
                                    enemyh[2] -= 1
                                    no_hit = True
                   
                    if wait == False:
                        if hitbox.colliderect(boxhit2) == 1:
                            life -= 1
                            if devmode == True:
                                print ("boxer")
                            wait = True
                
                # resetting locations and health of dead enemies along with regenerating one health
                if sum(enemyh) == 0:
                    xloc[0] = 700
                    yloc[0] = random.randint(200,500)
                    xloc[1] = 700
                    yloc[1] = random.randint(200,500)
                    xloc[2] = 700
                    yloc[2] = random.randint(200,500)                
                    enemyh[0] = 2
                    enemyh[1] = 2
                    enemyh[2] = 2
                    if hard == True:
                        enemyh[0] += 1
                        enemyh[1] += 1
                        enemyh[2] += 1
                    p = 0
                    boxy = 0
                    enemy_attack = False                
                    attacking = False
                    if life < 4:
                        life += 1
                                            
                    
            # initiating the death animation and sound
            elif life == 0:
                if noreplay == False:
                    deathfx = True
                    noreplay = True
                
                if deathfx == True:
                    pygame.mixer.music.load('Fluffing a Duck.mp3')                    
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(-1)     
                    deathfx = False            
                
                if devmode == True:
                    pygame.draw.rect(screen,WHITE,(0,0,800,600))
                    pygame.draw.rect(screen,YELLOW,(0,0,800,300))            
                else:
                    screen.blit(Road[funimation],(0,0))
                        
                pygame.draw.ellipse(screen,BLACK,(0,0,192,60))
                screen.blit(Heal[1],(0,0))
                
                screen.blit(Death[d],(charx,chary))
                
            elif life == -1:
                
                # game over screen
                if variety == False:
                    pygame.draw.rect(screen,BLUE,(0,0,800,600))
                    screen.blit(Over[gmovr],(70,50))
                    screen.blit(Menu_buttons[12],(50,400))
                else:
                    pygame.draw.rect(screen,(0,255,255),(0,0,800,600))
                    screen.blit(Over[gmovr],(70,50))
                    screen.blit(Menu_buttons[12],(50,400))
                
    
                screen.blit(text14,(59,412)) 
                screen.blit(text13,(60,410))              
                
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Menu_buttons[3],(750,0))          
        else:
            screen.blit(Menu_buttons[2],(750,0))        
################################################################################
    
    # The event for getting input.
    for event in pygame.event.get():     
        
        if event.type == pygame.KEYDOWN:
            if event.key == 115:
                up = True
            if event.key == 100:
                right = True
                if punch == False:
                    side = False
            if event.key == 97:         
                left = True
                if punch == False:
                    side = True
            if event.key == 119:
                down = True  
            if event.key == 32:
                jump = True
            if event.key == 306:
                crouch = True
                stop = True
            if event.key == 113:
                punch = True
                side = True
            if event.key == 101:
                punch = True
                side = False
            
            if event.key == 96:
                if change == False:
                    if devmode == False:
                        devmode = True
                    else:
                        devmode = False
                change = True
            if devmode == True:
                print(event.key)
            
        if event.type == pygame.KEYUP:
            if event.key == 115: 
                up = False
            if event.key == 97: 
                left = False
            if event.key == 100: 
                right = False
            if event.key == 119: 
                down = False
            if event.key == 32:
                jump = False
            if event.key == 306:
                crouch = False  
                stop = False
            if event.key == 113:
                punch = False
            if event.key == 101:
                punch = False
            if event.key == 96:
                change = False
            
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]      
        
        # Getting feedback to change the program based off of mouse clicks.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True
            if state == 0:
                if x <= 750 and x >=50 and y <= 300 and y >= 200:
                    state = 1
                if x <= 750 and x >=50 and y <= 450 and y >= 350:
                    state = 2              
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    but = False
                    break 
            elif state == 1:
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    state = 0
                    ply1 = False
                    ply2 = False
                if x <600 and  x>550 and y<300 and y>250:
                    ply1 = True
                    ply2 = False
                if x <250 and  x>200 and y<300 and y>250:
                    ply2 = True
                    ply1 = False
                if x<646 and x>546 and y<560 and y>460:
                    if ply1 == True or ply2 == True:
                        # reseting conditions
                        state = 3
                        hard = True
                        if hard == True:
                            enemyh[0] += 1                        
                            if music == "G":
                                pygame.mixer.music.load('Edge.mp3')
                                pygame.mixer.music.set_volume(0.1)
                                pygame.mixer.music.play(-1)                        
                if x<246 and x>146 and y<560 and y>460:
                    if ply1 == True or ply2 == True:
                        # reseting conditions
                        state = 3
                        if music == "G":
                            music = "E"
                            pygame.mixer.music.load('Edge.mp3')                    
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.play(-1)                    
            elif state == 2:
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    state = 0
            
            elif state == 3:
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    # reseting conditions
                    if music == "E":
                        music = "G"
                        pygame.mixer.music.load('Galaxy.mp3')                    
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1)                       
                    state = 1
                    charx = 300
                    chary = 300
                    xloc[0] = 700
                    yloc[0] = random.randint(200,500)
                    xloc[1] = 700
                    yloc[1] = random.randint(200,500)
                    xloc[2] = 700
                    yloc[2] = random.randint(200,500)                    
                    life = 4
                    noreplay = False
                    enemyh[0] = 2
                    enemyh[1] = 1
                    enemyh[2] = 1
                    hard = False
                    cutscene = True
        else: 
            click = False        
                    
    
    # Timer used for frames of animation.
    if timetracker % 1 == 0:
        time += 1
    
    if time % 50 == 0:
        if patty < 14:
            patty += 1
        else:
            patty = 0        
    
    if time % 15 == 0:
        
        if funimation < 28:
            funimation += 1
        else:
            funimation = 0
    
    if time % 350 == 0:
        if variety == False:
            variety = True
        else:
            variety = False
    
    
    # every value divisible by 10 is a new frame animation.
    if time % 10 == 0:
        
        if boxcount < 15:
            boxcount += 1
        else:
            boxcount = 0
            wait = False
            
        if gmovr != 7:
            gmovr += 1
        else:
            gmovr = 0
        
        if boxy != 7:
            boxy += 1
        else:
            boxy = 0
            
        # Used for main chip background
        if b <= -600:
            b = 0
            a = 0
        else:
            b -= 1
            a -= int(4/3)
            
        if life == 0:
            if d != 5:
                d += 1
            else:
                d = 0
                life = -1
            
        
        # Used for animation of player.
        if punch == False and jump == False and crouch == False:
            if left == True or right == True or up == True or down == True:
                if z < 20 or z > 31:
                    z = 20    
                if z == 31:
                    z = 20
                else:
                    z += 1
            else:
                z = 20
        
        if punch == True:
            county += 1
            if left == True or right == True or up == True or down == True:
                if z < 1 or z > 9:
                    z = 1
                if z == 9:
                    z = 2
                else:
                    z += 1  
            else:
                if z < 33 or z > 42:
                    z = 33
                if z == 42:
                    z = 34
                else:
                    z += 1       
            if z != 3 and z != 4 and z != 7 and z != 8 and z != 35 and z != 36 and z != 39 and z != 41:
                no_hit = False
        if jump == True or jumping == True:
            jumping = True
            count += 1
            if count == 1:
                z = 12
            elif count == 2:
                z = 13
            elif count == 5:
                z = 15
            elif count == 6:
                z = 20
                count = 0
            else:
                z = 14
            
            if count == 0:
                jumping = False

        if crouch == True or crouching == True:
            crouching = True
            counter += 1
            if counter == 1:
                z = 16
            elif counter == 2:
                z = 17
            elif counter == 5 and crouch != True:
                z = 19
            elif counter == 6 and crouch != True:
                z = 20
                counter = 0
            elif crouch == True:
                counter = 3
                z = 18
            else:
                z = 18
            
            if counter == 0:
                crouching = False

        # enemy attacking animation
        if enemy_attack == True or attacking == True:
            if enemy_attack == True:
                enemy_attack = False
                attacking == True
                p = 5
            attacking = True
            
            p += 1
            
            if p > 11:
                p = 5
                ouch = True
                attacking = False
            
        if enemy_attack == False and attacking == False:
            if lastxloc[0] == xloc[0] and lastyloc[0] == yloc[0] :
                p = 12
                
            if lastxloc[0] != xloc[0] or lastyloc[0] != yloc[0]:
                if p >= 3:
                    p = 0
                else:
                    p += 1
           
    if state != 3 or ply1 == False or life == -1:  
        if click == True:
                screen.blit(Point[1],(x,y))
        else:
            screen.blit(Point[0],(x,y))
        
    
    # Time to change the background
    if time % 60 == 0:
        RAND = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    #print ("up:",up,"down:",down,"left:",left,"right:",right)
    
    # Setting the frame rate to 120.
    myClock.tick(120)
    
    # putting the pictures on screen.
    pygame.display.flip()

# Stoping the music.    
pygame.mixer.quit

# Stopping the Menu
pygame.quit()