from pygame import*
init()
wigth = 900
hight = 500
window = display.set_mode((wigth,hight))
fps = time.Clock()
bg = image.load("пинг понг.jpg")
bg = transform.scale(bg, (wigth,hight))

class Rocet():
    def __init__(self, img, x, y, wigth_rocet, hight_rocet, speed):
        self.image = transform.scale(image.load(img),(wigth_rocet, hight_rocet))
        self.image_hit = self.image.get_rect()
        self.image_hit.x = x
        self.image_hit.y = y
        self.speed = speed

    def show_s(self):
        window.blit(self.image, (self.image_hit.x, self.image_hit.y))

class Rocet_player1(Rocet):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.image_hit.y > 5:
            self.image_hit.y -= self.speed
        if keys[K_DOWN] and self.image_hit.y < wigth - 80:
            self.image_hit.y += self.speed

class Rocet_player2(Rocet):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.image_hit.y > 5:
            self.image_hit.y -= self.speed
        if keys[K_a] and self.image_hit.y < wigth - 80:
            self.image_hit.y += self.speed


Roket1 = Rocet_player1("палка1-removebg-preview.png", 30, 200, 25, 150, 4)
Roket2 = Rocet_player2('палка2-removebg-preview.png', 30, 200, 25, 150, 4)
ball = Rocet('мячик-removebg-preview.png', 200, 200,50,50,4)

speed_x = 3
speed_y = 3

fps = time.Clock()
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    window.blit(bg,(0,0))

    Roket1.show_s()
    Roket2.show_s()
    ball.show_s()
    Roket1.update_r()
    Roket2.update_r()

    ball.image_hit.x += speed_x
    ball.image_hit.y += speed_y

    display.update()
    fps.tick(60)

