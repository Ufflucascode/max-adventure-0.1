from pplay.window import Window
from pplay.sprite import Sprite
from pplay.gameimage import GameImage
from pplay.sound import Sound
from fasefinal import fase1
def fase2(coin, vida, difficulty):
    janela = Window(1200, 1000)
    vidas=vida
    cenario = GameImage("sprites/backgrounddes.jpg")
    janela.clear()
    sound=Sound("sprites/cruising-down-8bit-lane-159615_1.ogg")
    janela.set_title("sprites/Max's Odssey")
    player = Sprite("sprites/max(1).png", frames=24)
    chao = Sprite("sprites/fase2-1.png")
    powerup = Sprite("sprites/powerup.png")
    bola = Sprite("sprites/bolafogo1.png")
    janela.x=0
    plats = []
    moedas = []
    warriors = []
    esqueletos = []
    bolas = []
    arrow = []
    plat = False
    cenario.set_position(0, 0)
    player.set_position(0, 785 - player.height)
    chao.set_position(0,770)
    powerup.set_position(1000, 620 + powerup.height)
    iconefire = Sprite("sprites/bolafogo1.png")
    iconefire.set_position(1010, 280)
    teclado = Window.get_keyboard()
    playvel = 30
    pulovel = 0
    cenvel = 200
    passar=False
    b = True
    t1=1
    dano=False
    pulo = False
    bola_de_fogo = False
    ultima_tecla = 1
    cooldown_bola = 0.5
    tempo_passado = 0
    c1=False
    tempo_passado_powerup = 0
    tempo_passado_hurt = 0
    tempo_passado_hit = 0
    hurt = False
    fire=False
    hit = False
    cooldown_powerup = 0.5
    cooldown = False
    idle = True
    idle_temp = 0
    right = False
    left = False
    right_temp = 0
    left_temp = 0
    pulo_ani = False
    pulo_ani_temp = 0
    cdd = 0
    f = False
    caindo = False
    tempo_fps = 0
    fps = 0
    tempo_fps_p = 0
    while True:
        cenario.draw()
        player.draw()
        chao.draw()
        sound.play()
        powerup.draw()
        if passar==False:
            janela.clear()
            passar=True
        tempo_fps_p += janela.delta_time()
        if tempo_fps >= 1:
            print(fps, "fps")
            fps = 0
            tempo_fps = 0
        x = 0
        if b == True:
            plats = []
            esqueletos = []
            warriors = []
            arrow = []
            bolas = []
            moedas = []
            for i in range(2):
                plataforma = Sprite("sprites/plat_des.png")
                plataforma.x = x + plataforma.width + 1200
                x = plataforma.x
                plataforma.y = 350
                plats.append(plataforma)
            x = 30
            for i in range(10):
                moeda = Sprite("sprites/moeda.png", frames = 6)
                if i <= 1:
                    moeda.x = x + plats[0].x + moeda.width*1.5
                    moeda.y = plats[0].y - plats[0].height/2
                elif i <= 3 and i > 1:
                    moeda.x = x + plats[1].x + (moeda.width*1.5) - 60
                    moeda.y = plats[1].y - plats[1].height/2
                elif i <= 7 and i > 3:
                    moeda.x = x + 500
                    moeda.y = 700
                else:
                    moeda.x = x + 1800
                    moeda.y = 700
                x += 30
                moedas.append(moeda)
            x = 0
            for i in range(6):
                warrior = Sprite("sprites/Warrior_Maior_Att2.png", frames = 42)
                warrior.pause()
                if i <= 1:
                    warrior.x = x + 600
                    warrior.y = chao.y - warrior.height
                elif i == 2 or i == 3 :
                    warrior.x = x + 1900
                    warrior.y = chao.y - warrior.height
                else:
                    warrior.x = x + 3200
                    warrior.y = chao.y - warrior.height
                x += 30
                infos = [warrior, 70, False, False, 0, 0, False, 0, warrior.x - player.x, False, 0, True, 0]
                warriors.append(infos)
            x = 30
            for i in range(4):
                esqueleto = Sprite("sprites/Esqueletos_att3.png", frames = 47)
                esqueleto.set_total_duration(16000)
                if i <= 1:
                    esqueleto.x = x + plats[0].x
                    esqueleto.y = chao.y - esqueleto.height
                else:
                    esqueleto.x = x + plats[1].x - 60
                    esqueleto.y = chao.y - esqueleto.height
                x += 30
                infos = [esqueleto, 70, False, esqueleto.x - player.x, 0, True, 0, True, 2]
                esqueletos.append(infos)
            b = False
        if b == False:
            for i in range(2):
               plats[i].draw()
            for i in range(len(moedas)):
                moedas[i].set_total_duration(1000)
                moedas[i].update()
                moedas[i].draw()
            for i in range(6):
                if warriors[i][0] != 0:
                    warriors[i][8] = warriors[i][0].x - player.x
                    if warriors[i][2] == True and not warriors[i][0].is_playing() and warriors[i][11] == True:
                        if warriors[i][8] < 0:
                            warriors[i][0].set_sequence_time(39, 40, 1000, True)
                        else:
                            warriors[i][0].set_sequence_time(41, 42, 1000, True)
                    elif warriors[i][3] == True and warriors[i][11] == True:
                        if warriors[i][8] < 0:
                            if warriors[i][5] >= 1:
                                warriors[i][0].set_sequence_time(1, 2, 1000, True)
                            else:
                                warriors[i][0].set_sequence_time(3, 4, 1000, True)
                    if warriors[i][8] >= 0 and warriors[i][3] == True and warriors[i][11] == True:
                        if warriors[i][5] >= 1:
                            warriors[i][0].set_sequence_time(5, 6, 1000, True)
                        else:
                            warriors[i][0].set_sequence_time(6, 7, 1000, True)
                    elif warriors[i][6] == True and warriors[i][11] == True and not warriors[i][0].is_playing():
                        if warriors[i][8] < 0:
                            warriors[i][0].set_sequence_time(15, 22, 1000, True)
                        else:
                            warriors[i][0].set_sequence_time(23, 30, 1000, True)
                    elif warriors[i][9] == True and not warriors[i][0].is_playing() and warriors[i][11] == True:
                        if warriors[i][8] < 0:
                            warriors[i][0].set_sequence_time(31, 34, 1000, False)
                            warriors[i][11] = False
                        else:
                            warriors[i][0].set_sequence_time(35, 38, 1000, False)
                            warriors[i][11] = False
                    elif warriors[i][2] == False and warriors[i][3] == False and not warriors[i][0].is_playing() and warriors[i][11] == True:
                        warriors[i][0].set_sequence_time(9, 14, 1000, True)

                    if warriors[i][9] == True:
                        warriors[i][10] += janela.delta_time()
                        if warriors[i][10] >= 2:
                            warriors[i][0] = 0
                            break
                    warriors[i][0].set_total_duration(2000)
                    warriors[i][0].play()
                    warriors[i][4] -= janela.delta_time()
                    warriors[i][7] -= janela.delta_time()
                    warriors[i][12] += janela.delta_time()
                    warriors[i][0].update()
                    warriors[i][0].draw()
            if hurt:
                tempo_passado_hurt += janela.delta_time()
            if tempo_passado_hurt >= 2:
                for e in warriors:
                    if e[0] != 0:
                        if e[2] == True:
                            e[2] = False
                            tempo_passado_hurt = 0
                            hurt = False
                            break
            for i in range(4):
                if esqueletos[i][0] != 0:
                    esqueletos[i][3] = esqueletos[i][0].x - player.x
                    if esqueletos[i][2] == True and esqueletos[i][7] == True:
                        if esqueletos[i][3] < 0:
                            esqueletos[i][0].set_sequence_time(23, 27, 1000, True)
                            esqueletos[i][0].set_total_duration(2000)
                            esqueletos[i][7] = False
                        else:
                            esqueletos[i][0].set_sequence_time(43, 47, 1000, True)
                            esqueletos[i][0].set_total_duration(2000)
                            esqueletos[i][7] = False
                    if esqueletos[i][2] == True:
                        esqueletos[i][4] += janela.delta_time()
                        if esqueletos[i][4] >= 1.1:
                            esqueletos[i][0] = 0
                            continue
                    if esqueletos[i][5] == True and esqueletos[i][7] == True and not esqueletos[i][0].is_playing():
                        if esqueletos[i][3] < 0:
                            esqueletos[i][0].set_sequence_time(8, 22, 1000, True)
                            esqueletos[i][0].set_total_duration(1000)
                        else:
                            esqueletos[i][0].set_sequence_time(28, 42, 1000, True)
                            esqueletos[i][0].set_total_duration(1000)
                    if esqueletos[i][5] == False and warriors[i][7] == False and esqueletos[i][2] == False:
                        esqueletos[i][0].set_sequence_time(1, 8, 1000, True)
                        esqueletos[i][0].set_total_duration(2000)

                    if esqueletos[i][8] >= 2:
                        esqueletos[i][0].pause()
                        esqueletos[i][8] = 0

                    
                    esqueletos[i][0].play()
                    esqueletos[i][6] -= janela.delta_time()
                    esqueletos[i][8] += janela.delta_time()
                    esqueletos[i][0].update()
                    esqueletos[i][0].draw()

        if player.x + player.width < 1200 and teclado.key_pressed("RIGHT"):
         if tempo_fps_p >= 0.00833333333:
            if chao.x + chao.width >= 1200:
                player.move_x(playvel * janela.delta_time())
                chao.move_x(cenvel*janela.delta_time()*-1)
                powerup.move_x(cenvel*janela.delta_time()*-1)
                for i in range(2):
                    plats[i].move_x(cenvel * janela.delta_time() * -1)
                for i in range(len(moedas)):
                    moedas[i].move_x(cenvel * janela.delta_time() * -1)
                for i in range(6):
                    if warriors[i][0] != 0:
                        warriors[i][0].move_x(cenvel * janela.delta_time() * -1)
                for i in range(4):
                    if esqueletos[i][0] != 0:
                        esqueletos[i][0].move_x(cenvel * janela.delta_time() * -1)
                for f in arrow:
                    if f[0] != 0:
                        f[0].move_x(cenvel * janela.delta_time() * -1)
            else:
                player.move_x((playvel+180)*janela.delta_time())
        if teclado.key_pressed("LEFT") and player.x >= 0:
         if tempo_fps_p >= 0.00833333333:
            if chao.x + chao.width >= 1200:
                player.move_x(playvel * janela.delta_time() * -1)
                chao.move_x(cenvel * janela.delta_time())
                powerup.move_x(cenvel*janela.delta_time())
                for i in range(2):
                    plats[i].move_x(cenvel * janela.delta_time())
                for i in range(len(moedas)):
                    moedas[i].move_x(cenvel * janela.delta_time())
                for i in range(6):
                    if warriors[i][0] != 0:
                        warriors[i][0].move_x(cenvel * janela.delta_time())
                for i in range(4):
                    if esqueletos[i][0] != 0:
                        esqueletos[i][0].move_x(cenvel * janela.delta_time())
                for f in arrow:
                    if f[0] != 0:
                        f[0].move_x(cenvel * janela.delta_time())
            else:
                player.move_x((playvel+80)*janela.delta_time() * -1)
        if not teclado.key_pressed("RIGHT") and not teclado.key_pressed("LEFT") and not teclado.key_pressed("UP") and idle_temp <= 0:
            idle = True
        if idle:
            player.set_sequence_time(1, 4, 1000, True)
            player.set_total_duration(2000)
            player.play()
            idle_temp = 2
            idle = False
        idle_temp -= janela.delta_time()
        if teclado.key_pressed("LEFT"):
            if left_temp <= 0:
                left = True
            ultima_tecla = 0
        elif teclado.key_pressed("RIGHT"):
            if right_temp <= 0:
                right = True
            ultima_tecla = 1
        if right and not pulo:
            player.set_sequence_time(5, 9, 2000, True)
            player.set_total_duration(1000)
            player.play()
            right_temp = 2
            right = False
        right_temp -= janela.delta_time()
        if left and not pulo:
            player.set_sequence_time(20, 24, 2000, True)
            player.set_total_duration(1000)
            player.play()
            left_temp = 2
            left = False
        left_temp -= janela.delta_time()
        if teclado.key_pressed("ESC"):
            janela.close()
        if player.collided(powerup) and fire==False:
            powerup.hide()
            bola_de_fogo = True
            fire=True
            c1=True
        if bola_de_fogo:
            tempo_passado += janela.delta_time()
        if c1==True:
            iconefire.draw()
        if bola_de_fogo == True and teclado.key_pressed("SPACE") and tempo_passado >= cooldown_bola:
            tempo_passado = 0
            c = Sprite("sprites/bolafogo1.png")
            if ultima_tecla == 0:
                c_d = 0    
                c.set_position(player.x - c.width, player.y + c.height)
            else:
                c_d = 1
                c.set_position(player.x + player.width, player.y + c.height)
            infos = [c, c_d, player.x-c.width, player.y+player.height/2+c.height]
            bolas.append(infos)
            infos = []
        for d in range(len(bolas)):
            if bolas[d][0] != 0:
                bolas[d][0].draw()
            if bolas[d][0] != 0:
             if tempo_fps_p >= 0.00833333333:
                if bolas[d][1] == 0:
                    bolas[d][0].move_x(400*janela.delta_time()*-1)
                else:
                    bolas[d][0].move_x(400*janela.delta_time())
                if bolas[d][2] + 400 <= bolas[d][0].x or bolas[d][2] - 300 >= bolas[d][0].x:
                    bolas[d][0] = 0
                    break
                for e in warriors:
                    if bolas[d][0] != 0 and e[0] != 0:
                        if bolas[d][0].collided(e[0]):
                            bolas[d][0] = 0
                            hurt = True
                            e[2] = True
                            e[1] -= 35
                            break
                for e in esqueletos:
                    if bolas[d][0] != 0 and e[0] != 0:
                        if bolas[d][0].collided(e[0]):
                            bolas[d][0] = 0
                            hurt = True
                            e[2] = True
                            e[1] -= 35
                            break
        for e in esqueletos:
            if e[0] !=0:
             dis = e[0].x - player.x
            if e[0] != 0:
                if e[1] <= 0:
                    e[2] = True
                if dis <= 1000 and e[6] <= 0:
                    e[5] = True
                    e[0].pause()
                    if dis <= 0:
                        dire = 1
                        flecha = Sprite("sprites/Arrow.png")
                        flecha.set_position(e[0].x + e[0].width, e[0].y + e[0].height/2)
                    else:
                        dire = -1
                        flecha = Sprite("sprites/Arrow_invertida.png")
                        flecha.set_position(e[0].x, e[0].y + e[0].height/2)
                    infos = [flecha, dire]
                    arrow.append(infos)
                    e[6] = 4
        for e in warriors:
            if e[0] != 0:
                dis = e[0].x - player.x
                if e[1] <= 0:
                    e[9] = True
                    e[0].pause()
                if abs(dis) <= 1000 and e[3] == False and e[2] == False and e[9] == False:
                 if tempo_fps_p >= 0.00833333333:
                    if dis < 0:
                        e[0].move_x(150*janela.delta_time())
                    else:
                        e[0].move_x(150*janela.delta_time()*-1)
                    e[6] = True
                    if e[7] <= 0:
                        e[0].pause()
                        e[7] = 2
                if abs(dis) <= 75 and e[4] <= 0 and e[9] == False:
                    hit = True
                    e[3] = True
                    e[0].pause()
                    e[4] = 2
                    e[5] = 2
                if e[3] == True:
                    if e[5] > 0:
                        e[5] -= janela.delta_time()
                    if e[5] <= 0.7:
                        if dis <= 0 and dis >= -75 and e[12] >= 2:
                         if tempo_fps_p >= 0.00833333333:
                            vida -= 1
                            dano=True
                            e[12] = 0
                        elif dis > 0 and dis <= 75 and e[12] >= 2:
                          if tempo_fps_p >= 0.00833333333:
                            vida -= 1
                            dano=True
                            e[12] = 0
                    if e[5] <= 0:
                        e[0].pause()
                        e[3] = False
                        e[5] = 0
                if e[6] and e[2]:
                    e[6] = False
                    e[0].pause()
        for f in arrow:
            if f[0] != 0:
             if tempo_fps_p >= 0.00833333333:
                if f[1] == 1:
                    f[0].move_x(300*janela.delta_time())
                else:
                    f[0].move_x(300*janela.delta_time()*-1)
                if f[0].collided(player) or f[0].x < 0 or f[0].x > 1200:
                    if f[0].collided(player):
                     if tempo_fps_p >= 0.00833333333:
                        vida -= 1
                        dano=True
                    arrow.remove(f)
                if f[0] != 0:
                    f[0].draw()
        if player.x >= janela.width-200:
         if tempo_fps_p >= 0.00833333333:
            sound.stop()
            player.x=0
            janela.x=0
            janela.clear()
            fase1(coin,vida)
        if teclado.key_pressed("UP") and not pulo:
            pulo = True
            pulo_ani = True
            pulovel = -7
        if pulo_ani and pulo_ani_temp <= 0:
            player.set_sequence_time(11, 18, 1000, True)
            player.set_total_duration(500)
            pulo_ani_temp = 1
            pulo_ani = False
        pulo_ani_temp -= janela.delta_time()

        if vida <= 0:
            janela.clear()
            cenario.set_position(0, 0)
            player.set_position(0, 785 - player.height)
            chao.set_position(0,770)
            powerup.set_position(1000, 620 + powerup.height)
            powerup.unhide()
            fire = False
            c1 = False
            bola_de_fogo = False
            b = True
            vida = vidas
        if pulo:
            plat = False
            pulovel += 0.05
            player.y += pulovel
            if pulovel >= 0:
                for e in warriors:
                    if e[0] != 0 and e[9] == False:
                        if player.y + player.height >= e[0].y and player.collided(e[0]):
                            pulovel = -7
                            hurt = True
                            e[2] = True
                            e[1] -= 100
                            caindo = False
                            break
                for e in esqueletos:
                    if e[0] != 0:
                        if player.y + player.height >= e[0].y and player.collided(e[0]):
                            pulovel = -7
                            e[1] -= 100
                            caindo = False
                            break
            for p in plats:
                if pulovel >= 0 and player.y > p.y:
                    caindo = True
                if player.y + player.height >= p.y and player.x >= p.x - 20 and player.x <= p.x + p.width - 30 and pulovel >= 0 and not caindo:
                    player.y = p.y - player.height + 20
                    plat_atual = p
                    pulo = False
                    plat = True
                    pulovel = 0
                    break
        if not plat and player.y < 785 - player.height and pulo_ani_temp <= 0:
            player.set_sequence_time(17, 18, 1000, True)
            player.set_total_duration(500)
        if plat:
            if player.x < plat_atual.x - 20 or player.x > plat_atual.x + plat_atual.width - 30 or player.y + player.height > plat_atual.y + 20:
                pulo = True
                caindo = True
                pulovel = 0
        if player.y >= 785 - player.height:
            pulo = False
            plat = False
            caindo = False
            pulovel = 0
        for i in range(len(moedas)):
         if moedas != []:
            if moedas[i].collided(player):
                moedas.pop(i)
                coin += 1
                break
        janela.draw_text(str(coin), 0, 200, 50, (255, 255, 0), "Arial", False, False)
        janela.draw_text(f'Hp {str(vida)}', 1000, 200, 50, (255, 255, 0), "Arial", False, False)
        if dano == True:
            janela.draw_text("ouch", 1000, 300, 50, (255, 255, 0), "Arial", False, False)
            t1 -= janela.delta_time()
            if t1 <= 0:
                dano = False
                t1 = 1
        if tempo_fps_p >= 0.00833333333:
            tempo_fps += tempo_fps_p
            fps += 1
            tempo_fps_p = 0
            player.play()
            player.update()
            janela.update()
if __name__ == "__main__":
    fase2(0,20,"easy")

