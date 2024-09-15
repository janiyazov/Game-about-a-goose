#pgzero

WIDTH = 600 # Ширина окна
HEIGHT = 300 # Высота окна

TITLE = "Goose" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду

#Переменные с графикой
fon = Actor('fonback')
q = Actor('guspravo2', (50,240))
fireball = Actor('trash1', (700, 240))
fireball_2 = Actor('trash2', (1000, 150))
go = Actor('guspravo2')
game_over = 0
count = 0

#Отрисовка
def draw():
    fon.draw()
    q.draw()
    fireball.draw()
    fireball_2.draw()
    if game_over == 1:
        go.draw()

    screen.draw.text(count, pos=(10, 10), color="white", fontsize=24)

def update(dt):
    global game_over
    global count
    #Перемещение препятствия
    if fireball.x > -20:
        fireball.x = fireball.x - 5
    else:
        fireball.x = WIDTH + 20
        #Увелечение переменной ⬇
        count += 1
    #Второе препятствие
    if fireball_2.x > -20:
        fireball_2.x = fireball_2.x - 5
    else:
        fireball_2.x = WIDTH + 20
        #Увелечение переменной ⬇
        count += 1
        
    #Управление
    if keyboard.left and q.x > 20:
        q.image = "guslevo2"
        q.x = q.x - 5
    elif keyboard.right and q.x < 580:
        q.image = "guspravo2"
        q.x = q.x + 5
    
    #Перезапуск
    if game_over == 1 and keyboard.enter:
        game_over = 0
        count = 0
        q.pos = (50,240)
        fireball.pos = (700, 240)
        fireball_2.pos = (1000, 150)
    
    # Столкновение
    if q.colliderect(fireball) or q.colliderect(fireball_2):
        q.image = 'gusd2 (2)'
        game_over = 1

def on_key_down(key):
    #Прыжок
    if keyboard.up:
        q.image = "gusprig"
        q.y = 100
        animate(q, tween='bounce_end', duration=2, y=240)
    #Уклонение    
    elif keyboard.down:
