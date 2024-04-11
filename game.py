from pygame import*
init()
wight = 900
hight = 500
window = display.set_mode((wight,hight))
fps = time.Clock()
bg = image.load("пинг понг.jpg")
bg = transform.scale(bg, (wight,hight))
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    window.blit(bg,(0,0))


    display.update()
    fps.tick(60)


