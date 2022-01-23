import pygame
import random
pygame.mixer.init() #thư viện nhạc
pygame.init() # khởi tạo game

se_intro = pygame.mixer.Sound("./music/Intro.mp3")
se_high = pygame.mixer.Sound("./music/high1.mp3")
se_fail = pygame.mixer.Sound("./music/fail1.mp3")
se_back = pygame.mixer.Sound("./music/back.mp3")
se_crash = pygame.mixer.Sound("./music/crash.mp3")

#kích thước màn 
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
# đếm thời gian
clock = pygame.time.Clock()
# số khung hình trên 1 giây
fps = 70
#chọn phông
font = pygame.font.SysFont('./fonts/font1.TTF', 55)
font1 = pygame.font.SysFont('./fonts/font1.TTF', 50)
#xác định màu sắc
white = (255, 255, 255)
colorscore = (0,0,139)
green = (100,255,100)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)

purple = (252,67,255)
#camnau = (255,255,0) 
camnau = (145,0,0)


# Thông số nền trò chơi
bg = pygame.image.load('./img/begin4.png')
img_bg1 = pygame.image.load('./img/bg1.png')
img_bg2 = pygame.image.load('./img/bg2.png')
img_bg3 = pygame.image.load('./img/bg3.png')
img_bg4 = pygame.image.load('./img/bg4.png')
img_bg5 = pygame.image.load('./img/bg5.png')
img_bg6 = pygame.image.load('./img/bg6.png')
img_bg7 = pygame.image.load('./img/bg7.png')
# ----- Kết thúc và bắt đầu -------
begin = pygame.image.load('./img/start_bt.png')

#over = pygame.image.load('./img/over.png')
khung = pygame.image.load('./img/khung3.png')
button_restart = pygame.image.load('./img/restart.png')
button_restart = pygame.transform.scale2x(button_restart)

#---------------------------------------
h1 = pygame.image.load('./img/h1.png')
h2 = pygame.image.load('./img/h2.png')
h3 = pygame.image.load('./img/h3.png')

l1 = pygame.image.load('./img/p1.png')
l2 = pygame.image.load('./img/p2.png')
l3 = pygame.image.load('./img/p3.png')

end_sad = pygame.image.load('./img/end_sad.png')
end_hp = pygame.image.load('./img/end_hp.png')

#--------------------------------------
i = 0
flying = False
scroll_speed = 5 # tốc độ cuộn 

# khoảng cách giữa  2 cột
pipe_gap = 150
asteroid_gap = random.randint(200,500)
demon_gap = 300
laze_gap = 300
file_gap = random.randint(250,300)
file_gap1 = random.randint(200,250)
pipe_frequency =random.randint(1000,1200) #milliseconds : tần xuất xuất hiện vật cản theo thời gian (miligiay)
last_pipe = pygame.time.get_ticks() - pipe_frequency # biến để xác định độ lặp lại vật cản theo thời gian
score = 0
pass_pipe = False # biến xác định vượt qua vật cản
pass_asteroid = False
pass_asteroid1 = False
pass_demon = False
pass_laze = False
#==============================================================================================
# tạo các tuple chứa thông số, trạng thái 
begin_button = {
    'px':400,
    'py':450,
    'width':begin.get_rect().width,
    'height':begin.get_rect().height
}
# Thông số chuẩn bị cho trò chơi
game_run = {
    'isOver': False,
    'begin': False,
    'musixover' : False
}
#============================================
# function xuất(render) văn bản ra màn hình
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#========================================================================================================
# Lớp sprite được sử dụng làm lớp cơ sở cho các đối tượng trong trò chơi ,cung cấp các chức năng để duy trì chính nó
class Mage(pygame.sprite.Sprite):
    def __init__(self, x, y ):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 3):    
            img = pygame.image.load(f"img/mage{num}.png")  #duyệt hoạt ảnh 
            self.images.append(img)
        self.image = self.images[self.index] #gán các hoạt ảnh vào 1 biến chung
        #self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect() # tạo 1 khối chứa các hoạt ảnh
        
        #self.rect.topleft = pos
        #points = getRandomPolygonPointList( random.randrange( 3, 12 ), size )
        #pygame.draw.polygon( self.image, WHITE, points)
        self.rect.center = [x, y] # tọa độ của khối chữ nhật
        self.vel = 0 #velocity tốc độ bay lên xuống
    def update(self): # hàm này để up date các thông số khác
        if flying == True: 
            #apply gravity Tạo trọng lực cho nhân vật \

            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom <= 730: # vị trí của khối sao cho vẫn xuất hiện trên khung hình
                self.rect.y += int(self.vel) #....

        if game_run['isOver'] == False:
            #Jump
            if self.rect.x <= screen_width /4 :
                self.rect.x += 2
            if pygame.mouse.get_pressed()[0] == 1 :
               
                #a.play()
                # khi giữ chuột thì nhân vật bay lên
                self.vel = -8
           
            #rotate độ nghieng của nhan vat , xuay ảnh theo độ nghieeng
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
    
#----------------------------------------------------------------------------------------------


class Pipe(pygame.sprite.Sprite):   
    # class này tương tự như class Mage
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        #self.image = pygame.image.load("img/pipe.png")
        for num in range (1, 3):
            img = pygame.image.load(f"./img/cot{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # biến vị trí xác định xem đường ống đến từ dưới cùng hay trên cùng
        #position 1 là từ trên cùng, -1 là từ dưới cùng
        if position == 1:
            #transform.flip hàm đảo cột 
            self.image = pygame.transform.flip(self.image, False, False)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        elif position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]


    def update(self):
        # tạo hoạt ảnh cho khối
        #self.rect.y -= 0.5
        flap_cooldown = 5
        self.counter += 1
        
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]


        # cuộn khối theo chiều ngang phải - trái
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill() 

      

#===========================================================================================

# tạo thiên thạch 
class asteroid(pygame.sprite.Sprite):

    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 4):
            img = pygame.image.load(f"./img/h{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # biến vị trí xác định xem đường ống đến từ dưới cùng hay trên cùng
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(asteroid_gap / 2)]
        elif position == -1:
            self.rect.topleft = [x, y + int(asteroid_gap / 2)]
    def update(self):
        flap_cooldown = 5
     
      
        self.rect.y += 1.5
        self.rect.x -= 1
       
    
        self.counter += 1
        if self.rect.y > random.randint(400,500) :
            self.rect.y -= 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
       
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
#tạo dải 3 
# tạo thiên thạch 
class asteroid2(pygame.sprite.Sprite):

    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 4):
            img = pygame.image.load(f"./img/h{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # biến vị trí xác định xem đường ống đến từ dưới cùng hay trên cùng
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(asteroid_gap / 2)]
        elif position == -1:
            self.rect.topleft = [x, y + int(asteroid_gap / 2)]
    def update(self):
        flap_cooldown = 5  
        self.rect.y += 2.2
        self.rect.x -= 1   
        self.counter += 1
        if self.rect.y > random.randint(400,500) :
            self.rect.y -= 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
       
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

#====================================================================================================
class asteroid1(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 4):
            img = pygame.image.load(f"./img/h{num}.png")
            img = pygame.transform.scale2x(img)
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # biến vị trí xác định xem đường ống đến từ dưới cùng hay trên cùng
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(asteroid_gap / 2)]
        elif position == -1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.topleft = [x, y + int(asteroid_gap / 2)]
    def update(self):
         
        self.rect.y += 1
        self.rect.x -= 1
        flap_cooldown = 5
        self.counter += 1
        
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
       
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


#=====================================================================================================


# tạo demon
class Demon(pygame.sprite.Sprite):

    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 4):
            img = pygame.image.load(f"./img/de{num}.png")
            #img = pygame.transform.scale2x(img)
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # biến vị trí xác định xem đường ống đến từ dưới cùng hay trên cùng
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(demon_gap / 2)]
        elif position == -1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.topleft = [x, y + int(demon_gap / 2)]
    def update(self):
        if self.rect.y >= random.randint(50,150):  
            self.rect.y -= 0.7
            self.rect.x -= 0.1
        flap_cooldown = 5
        self.counter += 1  
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
       
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()



#=======================================================================================

# tạo thiên thạch 
class Laze(pygame.sprite.Sprite):

    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 4):
            img = pygame.image.load(f"./img/p{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # biến vị trí xác định xem đường ống đến từ dưới cùng hay trên cùng
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(laze_gap / 2)]
        elif position == -1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.topleft = [x, y + int(laze_gap / 2)]
    def update(self):
        flap_cooldown = 5
        self.counter += 1     
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()



#===========================================================================================

#tạo button 
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        action = False
        #lấy vị trí chuột
        pos = pygame.mouse.get_pos()
        #kiểm tra điều kiện di chuột qua và nhấp chuột
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        #nút vẽ
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#================================================================================================


class pipe1(pygame.sprite.Sprite):

    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(file_gap  / 2)]
        elif position == -1:
            #self.image = pygame.transform.flip(self.image, False, True)
            self.rect.topleft = [x, y + int(file_gap  / 2)]
    def update(self):
        flap_cooldown = 5
        self.counter += 1       
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            #self.image = self.images[self.index]          
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


#================================================================================================

class pipe2(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0     
        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(file_gap1  / 2)]
        elif position == -1:
            #self.image = pygame.transform.flip(self.image, False, True)
            self.rect.topleft = [x, y + int(file_gap1  / 2)]
    def update(self):
        if self.rect.y >= 200: # nó chỉ đến tọa độ 450 là dứng lại
            self.rect.y -= 1
        else :
            self.rect.y += 1
        flap_cooldown = 5
        self.counter += 1      
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            #self.image = self.images[self.index]          
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

#================================================================================================


# Khởi tạo màn bắt đầu game
def game_init():  
    screen.blit(bg, (0, 0))
    game_run['begin'] = False
    game_run['isOver'] = False
    game_run['musixover'] = False
game_init()


# function khởi động lại game
def reset_game():
    global time_now1
    time_now1 =0 
    pipe_group.empty() #xóa hết cột
    asteroid_group.empty()
    asteroid1_group.empty()
    asteroid2_group.empty()
    demon_group.empty()
    laze_group.empty()
    mage.rect.x = 150
    pipe1_group.empty()
    pipe2_group.empty()
    mage.rect.y = int(screen_height / 2)
    score = 0
    scroll_speed = 6
    return score

# thiết kế nút bắt đầu game 
def draw_begin():
    if game_run['begin'] is False:
       
        begin_button['px'] = 80
        begin_button['py'] = 355
    screen.blit(begin, (begin_button['px'], begin_button['py']))


draw_begin()
#mx , my tọa dộ chuột click
def bt_crash(mx,my):
    if  begin_button["px"] <= mx <= (begin_button['px'] + begin_button['width']) and begin_button['py'] <= my <= (begin_button['py'] + begin_button['height']):
        # đơn giản là xét vị trí click của button , nếu click ra ngoài tọa độ thỏa mãn thì return False    
        return True
    return False


    #===================KIỂM TRA VA CHẠM===========================================
        
def collide() :
    if pygame.sprite.groupcollide(mage_group, pipe_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, asteroid_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, asteroid1_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, asteroid2_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, demon_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, laze_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, pipe1_group, False, False) :
        game_run['isOver'] = True
    if pygame.sprite.groupcollide(mage_group, pipe2_group, False, False) :
        game_run['isOver'] = True

    if mage.rect.bottom >= 730:
        game_over = True
        flying = False

    if mage.rect.bottom >= 730:
        game_run['isOver'] = True
        flying = False

    if mage.rect.top < -10 :
        game_run['isOver'] = True
        flying = False        



#UPDATE LEVEL
def updatelevel() :
    global score
    if score <=9:
        draw_text("Level 1",font,camnau,20,20)
    elif score >= 10 and score <= 19 :
        draw_text("Level 2",font,camnau,20,20)
    elif score >= 20 and score <= 29:
        draw_text("Level 3",font,camnau,20,20)
    elif score >= 30 and score <= 39:
        draw_text("Level 4",font,camnau,20,20)
    elif score >= 40 and score <= 49:
        draw_text("Level 5",font,camnau,20,20)
    elif score >=50 and score <= 59:
        draw_text("Level 6",font,camnau,20,20)
    elif score >= 60 and score <= 69 :
        draw_text("Level 7",font,camnau,20,20)
    elif score >= 70 and score <= 79 :
        draw_text("Level 8",font,camnau,20,20)
    else :
        draw_text("Level max",font,camnau,20,20)
def Checkscore() :
    global pass_laze,pass_demon,pass_asteroid,pass_pipe,score,pass_asteroid1
    #check đk điểm   
    #sprites là các đối tượng có chức năng của hàm đã gọi , chỉ 1 nhân vật đơn lẻ nên index luôn  = 0 
    if len(pipe_group) > 0:
        if mage_group.sprites()[0].rect.left < pipe_group.sprites()[0].rect.left\
            and pass_pipe== False:
            # xét điều kiện thỏa mãn bay qua vật cản :             
            pass_pipe = True
        if pass_pipe == True:
            if mage_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(asteroid_group) > 0:
        if mage_group.sprites()[0].rect.left < asteroid_group.sprites()[0].rect.left\
            and pass_asteroid== False:
            # xét điều kiện thỏa mãn bay qua vật cản :             
            pass_asteroid = True
        if pass_asteroid == True:
            if mage_group.sprites()[0].rect.left > asteroid_group.sprites()[0].rect.right:
                score += 1
                pass_asteroid = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(asteroid1_group) > 0:
        if mage_group.sprites()[0].rect.left < asteroid1_group.sprites()[0].rect.left\
            and pass_asteroid== False:
            # xét điều kiện thỏa mãn bay qua vật cản :             
            pass_asteroid1 = True
        if pass_asteroid1 == True:
            if mage_group.sprites()[0].rect.left > asteroid1_group.sprites()[0].rect.right:
                score += 1
                pass_asteroid1 = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(asteroid2_group) > 0:
        if mage_group.sprites()[0].rect.left < asteroid2_group.sprites()[0].rect.left\
            and pass_asteroid1== False:
            # xét điều kiện thỏa mãn bay qua vật cản :              
            pass_asteroid1 = True
        if pass_asteroid1 == True:
            if mage_group.sprites()[0].rect.left > asteroid2_group.sprites()[0].rect.right:
                score += 1
                pass_asteroid1 = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(demon_group) > 0:
        if mage_group.sprites()[0].rect.left < demon_group.sprites()[0].rect.left\
            and pass_demon== False:
            # xét điều kiện thỏa mãn bay qua vật cản :             
            pass_demon = True
        if pass_demon == True:
            if mage_group.sprites()[0].rect.left > demon_group.sprites()[0].rect.right:
                score += 1
                pass_demon = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(laze_group) > 0:
        if mage_group.sprites()[0].rect.left < laze_group.sprites()[0].rect.left\
            and pass_laze == False:
            pass_laze= True
        if pass_laze== True:
            if mage_group.sprites()[0].rect.left > laze_group.sprites()[0].rect.right:
                score += 1
                pass_laze = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(pipe1_group) > 0:
        if mage_group.sprites()[0].rect.left < pipe1_group.sprites()[0].rect.left\
            and pass_laze == False:
            pass_laze= True
        if pass_laze== True:
            if mage_group.sprites()[0].rect.left > pipe1_group.sprites()[0].rect.right:
                score += 1
                pass_laze = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

    if len(pipe2_group) > 0:
        if mage_group.sprites()[0].rect.left < pipe2_group.sprites()[0].rect.left\
            and pass_laze == False:
            pass_laze= True
        if pass_laze== True:
            if mage_group.sprites()[0].rect.left > pipe2_group.sprites()[0].rect.right:
                score += 1
                pass_laze = False
        draw_text(str(score), font, camnau, int(screen_width / 2 + 20), 20)

def levelgui():
    global score,i
    if score <= 9:
        # tạo cuộn nền 
        screen.blit(img_bg1, (i, 0))
        screen.blit(img_bg1, (screen_width+i, 0))
        if i == -screen_width:
            screen.blit(img_bg1, (screen_width+i, 0))
            i = 0
        i -= 1

    elif score>=10 and score <=19 :
        screen.blit(img_bg2, (0,0))
        screen.blit(img_bg2, (i, 0))
        screen.blit(img_bg2, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1
    elif score>=20 and score <=29 :
        screen.blit(img_bg3, (0,0))
        screen.blit(img_bg3, (i, 0))
        screen.blit(img_bg3, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1
    elif score>=30 and score <=39 :
        screen.blit(img_bg4, (0,0))
        screen.blit(img_bg4, (i, 0))
        screen.blit(img_bg4, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1
    elif score>=40 and score <=49 :
        screen.blit(img_bg5, (0,0))
        screen.blit(img_bg5, (i, 0))
        screen.blit(img_bg5, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1
    elif score>=50 and score <=59 :
        screen.blit(img_bg6, (0,0))
        screen.blit(img_bg6, (i, 0))
        screen.blit(img_bg6, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1
    elif score>=60 and score <=69 :
        screen.blit(img_bg7, (0,0))
        screen.blit(img_bg7, (i, 0))
        screen.blit(img_bg7, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1
    else :
        screen.blit(img_bg2, (0,0))
        screen.blit(img_bg2, (i, 0))
        screen.blit(img_bg2, (screen_width+i, 0))
        if i == -screen_width:

            screen.blit(img_bg2, (screen_width+i, 0))
            i = 0
        i -= 1

#=================sinh vật cản theo level===========================================
def createobject():
    global score,time_now,last_pipe,scroll_speed
    # level 1 : cột lửa
    if score <= 7: #7
        scroll_speed = 6
        pipe_height = random.randint(10,200)   
        btm_pipe = Pipe(screen_width, int(screen_height / 6) + pipe_height, -1)
        pipe_group.add(btm_pipe) # thêm khối vào trong group
        last_pipe = time_now          
    # lv 2 1 sao chổi
    elif score >= 8 and score <= 18 :
        scroll_speed = 6
        asteroid_height = random.randint(-200, 300) 
        a = random.randint(1200,1500)  
        btm_asteroid = asteroid(a, int(screen_height /1.8) + asteroid_height, 1)
        asteroid_group.add(btm_asteroid)  
        last_pipe = time_now

    # level 3 : 2 cột trên dưới
    elif score >=19 and score <= 28 : 
        scroll_speed = 7
        pipe_height = random.randint(-100,200) 
        btm_pipe = pipe1(screen_width, int(screen_height / 2) + pipe_height, -1)
        top_pipe = pipe1(screen_width, int(screen_height / 2) + pipe_height, 1)
        pipe_group.add(btm_pipe)
        last_pipe = time_now
        pipe_group.add(top_pipe)
  
    # lv 4 quỷ bay 
    elif score >= 29 and score <= 38 : 
        scroll_speed = 7
        demon_height = random.randint(-200, 300) 
        a = random.randint(1200,1500)  
        btm_demon = Demon(a, int(screen_height /1.1) + demon_height, 1)      
        demon_group.add(btm_demon)
        last_pipe = time_now
    # lv 5 : laze sole
    elif score >= 39 and score <= 48 :
        scroll_speed = 7
        laze_height = random.randint(-200, 300) 
        a = random.randint(1200,1500)  
        btm_laze = Laze(a, int(screen_height /1.5) + laze_height, -1)
        top_laze = Laze(screen_width, int(screen_height / 2) + laze_height, 1)
        laze_group.add(btm_laze)
        laze_group.add(top_laze)
        last_pipe = time_now
    # 2 sao chổi nhỏ
    elif score >= 49 and score <= 58 :
        scroll_speed = random.randint(6,7)
        asteroid_height = random.randint(-100, 250) 
        asteroid_height1 = random.randint(-150, 100)
        a = random.randint(1200,1500) 
        b = random.randint(1100,1200) 
        btm_asteroid = asteroid(a, int(screen_height /1.4) + asteroid_height, 1)
        top_asteroid = asteroid(a, int(screen_height /3.5) + asteroid_height1, 1)
        asteroid_group.add(btm_asteroid)
        asteroid_group.add(top_asteroid)
        last_pipe = time_now
    # 3  chôi to 
    elif score >=  59 and score <= 68 :
        scroll_speed = 7 
        asteroid_height = random.randint(-300, 300)
        asteroid_height1 = random.randint(-300, 200) 
        a = random.randint(1100,1180)  
        b = random.randint(1100,1200) 
        c = random.randint(1200,1300) 
        btm_asteroid = asteroid2(a, int(screen_height /1.6) + asteroid_height, 1)
        asteroid_group.add(btm_asteroid) 
        btm1_asteroid = asteroid2(b, int(screen_height /1.9) + asteroid_height1, 1)
        btm2_asteroid = asteroid2(c, int(screen_height /1.3) + asteroid_height, 1)
        asteroid_group.add(btm1_asteroid)
        asteroid_group.add(btm2_asteroid)  
        last_pipe = time_now

    # lv 7 2 sao chổi to
    elif score >= 69 and score <= 78:
        scroll_speed = random.randint(6,7)
        asteroid_height = random.randint(-200, 200) 
        asteroid_height1 = random.randint(-140, 100)
        a = random.randint(1200,1500) 
        b = random.randint(900,1000) 
        btm_asteroid = asteroid1(a, int(screen_height /1.8) + asteroid_height, 1)
        top_asteroid = asteroid1(b, int(screen_height /3) + asteroid_height1, -1)
        asteroid1_group.add(btm_asteroid)
        asteroid1_group.add(top_asteroid)
        last_pipe = time_now
    #lv max ống hẹp dần
    else :
        scroll_speed = 6
        pipe_height = random.randint(-100,100) 
        btm_pipe = pipe2(screen_width, int(screen_height / 1.6) + pipe_height, -1)
        top_pipe = pipe2(screen_width, int(screen_height / 4.2) + pipe_height, 1)
        pipe2_group.add(btm_pipe)
        last_pipe = time_now
        pipe2_group.add(top_pipe)


def gameover():
    #Bao gồm giao diện và hiển thị điểm số sau khi kết thúc trận và thực hiện chức năng restart()
    global score
    if game_run['isOver'] == True :
        se_back.stop()      
        # đọc điểm highscore từ file log và nếu file đấy ko tồn tại thì sẽ tự tạo 1 file mới.
        try:
            #reading highscore
            hscore = open ("highscore/score.log", 'r')
            high_score = hscore.read ()
            hscore.close()
        except:
            writescore = open ("highscore/score.log", "w")
            writescore.write (str (0))
            writescore.close ()
        # điều kiện để xét màn thua , sẽ thay đổi theo thành tích .
        if high_score =="" or (int(high_score) <= int(score)) :
            se_high.play()
            screen.blit(end_hp,(0,0))
            writescore=open("highscore/score.log","w")
            writescore.write(str(score))
            writescore.close()

            
            
        if int(high_score) > score :
            # cái này thêm nhạc vào
            se_fail.play()
            
            screen.blit(end_sad, (0,0))
        screen.blit(khung,(85,190))
        draw_text("Score : "+str(score),font1,camnau,int(289),(405))
        draw_text("Highscore : "+str(high_score),font,camnau,int(231),(355))
        if button.draw():           
            game_run['isOver'] = False
            score = reset_game()
            se_high.stop()
            
            se_fail.stop()
button = Button(235, 500, button_restart)

mage = Mage(random.randint(200,250), int(screen_height / 2))

mage_group = pygame.sprite.Group()
mage_group.add(mage)
pipe_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
asteroid2_group = pygame.sprite.Group()
asteroid1_group = pygame.sprite.Group()
demon_group = pygame.sprite.Group()
laze_group = pygame.sprite.Group()
pipe1_group = pygame.sprite.Group()
pipe2_group = pygame.sprite.Group()



#=============================================================================================================
#=============================================================================================================


run = True
# tạo vòng lặp khi begin game
while run:
    se_intro.play()
    clock.tick(fps)
    # Vẽ têu đề
    #screen.blit(img_title, (screen_width-1250, 0))
    if  game_run['begin'] is True   :
        se_back.play()
        se_intro.stop()        
        levelgui()  
        # draw và update các thông số hình ảnh
        mage_group.draw(screen)
        pipe_group.draw(screen)
        mage_group.update()
        asteroid_group.draw(screen)
        demon_group.draw(screen)
        laze_group.draw(screen)
        pipe1_group.draw(screen)
        pipe2_group.draw(screen)
        asteroid2_group.draw(screen)
        asteroid1_group.draw(screen)
        updatelevel()
        Checkscore()
        gameover()
        collide()
        #đặt thêm img_title trong khi chs
        #screen.blit(img_title, (screen_width-1250, 0))  

        if mage.rect.bottom >= 730:
            game_over = True
            flying = False

        if mage.rect.bottom >= 730:
            game_run['isOver'] = True
            flying = False

        if mage.rect.top < -10 :
            game_run['isOver'] = True
            flying = False        

        #============= Sinh vẬt cản mới =========================

        if game_run['isOver'] == False and flying == True :
        #generate new pipes
            #thiết lập thời gian hiện tại khi bắt đầu game
            time_now = pygame.time.get_ticks()
            #if score <= 5:
            # thời gian thực trừ đi đường ống cuối cùng > tần suất xuất hiện thì tiền hành lặp lại vật cản
            if time_now - last_pipe > pipe_frequency:
                createobject()
            pipe_group.update()
            asteroid_group.update()
            asteroid1_group.update()
            asteroid2_group.update()
            demon_group.update()
            laze_group.update()
            pipe1_group.update()
            pipe2_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # đơn giản là click thoát nếu ko sd sẽ ko clickthoat game đc
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN  and game_run['isOver'] == False:
            # restart nhân vật sẽ cố định vị trí 
            flying = True
            mx, my = event.pos           
    # Click chuột
    m1, m2, m3 = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos() #lấy ví trí bấm chuột lưu trong biến pos
    if m1:
        # xác định vị trí  begin_button để click chuột
        if  bt_crash(mx,my) and  begin_button['px'] ==80:
            game_run['begin'] = True
    pygame.display.update()
pygame.QUIT
