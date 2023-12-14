from pplay.window import Window
from pplay.sprite import Sprite
from pplay.gameimage import GameImage
from pplay.sound import Sound
from fase2 import fase2
def playa(coin,vida):
 janela = Window(1200, 1000)
 janela.set_title("Space Invaders")
 cenario = GameImage("sprites/cenario.jpg")
 jogador = Sprite("sprites/max(1).png", frames=24)
 sound=Sound("sprites/8bitgame.ogg")
 jogador.set_position(0, 692)
 chao2 = Sprite("sprites/tem.png")
 chao3 = Sprite("sprites/tem.png")
 vidas=vida
 janela.clear()
 powerup = Sprite("sprites/powerup.png")
 powerup.set_position(200, 700)
 cenario.set_position(0, 0)
 tem = Sprite('sprites/tem.png')
 iconefire=Sprite("sprites/bolafogo1.png")
 iconefire.set_position(1000,300)
 tem.set_position(0, 621)
 chao2.set_position(tem.width - 50, 621)
 chao3.set_position(chao2.width + chao2.x - 50, 621)
 teclado = Window.get_keyboard()
 playvel = 30
 chaovel = 200
 inivel=40
 pulovel = 0
 pulo = False
 dano=False
 lista = []
 b = True
 d=True
 coin=0
 andar=0
 i1=0.5
 i2=0.5
 i4=1.5
 i5=2
 i3=1
 i6=0.4
 i7=0.8
 lista1=[]
 lista2=[]
 lista3=[]
 c=False
 coins=coin
 passar=False
 c1=True
 tempo_fps = 0
 fps = 0
 tempo_fps_p = 0
 so=0
 while True:
     tempo=janela.delta_time()
     so+=1
     if passar == False:
         janela.clear()
         passar = True
     if andar == 6 and pulo==False or pulo == False and andar == 5 :
         andar = 0
     cenario.draw()
     jogador.draw()
     #animacao do player
     if andar==0:
      jogador.set_sequence_time(1,3,500,True)
      jogador.set_total_duration(1000)
      andar=3
     powerup.draw()
     tem.draw()
     chao2.draw()
     chao3.draw()
     sound.play()
     inix=0
     x1=500
     tempo_fps_p+=janela.delta_time()
     print(andar)
     if tempo_fps >= 1:
         print(fps,"fps")
         fps = 0
         tempo_fps = 0
     #array de inimigo
     if d==True:
         for i in range(8):
             listaini = Sprite("sprites/ini2.png")
             listaini.x = inix + listaini.width + 600
             inix = listaini.x
             listaini.y = 680
             lista2.append(listaini)
         for i in range(6):
             listain = Sprite("sprites/ini.png")
             listain.x = x1
             x1 = listain.x + listain.width + 990
             listain.y = 640
             lista3.append(listain)
         d=False
     if d == False:
      for i in range(len(lista2)):
       lista2[i].draw()
       if tempo_fps_p>=0.00833333333:
        lista2[i].move_x(inivel * janela.delta_time() * -1)
       if lista2[i].x < tem.x-10:
           lista2.pop(i)
           break
      for i in range(len(lista3)):
       lista3[i].draw()
       if tempo_fps_p >= 0.00833333333:
        lista3[i].move_x(inivel * janela.delta_time() * -1)
       if lista3[i].x < tem.x - 20:
           lista3.pop(i)
           break
     #power up de fogo
     if jogador.collided(powerup) and c1==True:
         c = True
         c1=False
         powerup.hide()
     if c1==False:
         iconefire.draw()
     if c == True:
         if teclado.key_pressed("SPACE"):
             fogo = Sprite("sprites/bolafogo1.png")
             fogo.x = jogador.x+40
             fogo.y = jogador.y+20
             lista1.append(fogo)
             c=False
     if c==False:
      i2 -= tempo
      if i2 <= -1:
        c = True
        i2 = 0.5
     if lista1 != []:
      for i in range(len(lista1)):
           lista1[i].draw()
           if tempo_fps_p >= 0.00833333333:
            lista1[i].move_x(playvel * 4 * janela.delta_time())
           if lista1!=[]:
             if lista1[0].x >= jogador.x+200:
                 if lista1!=[]:
                   lista1.pop(0)
                   break
     x=0
     tempo=janela.delta_time()
    #gerar moeda
     if b == True:
         for i in range(18):
            if i%2==0:
             moeda1 = Sprite("sprites/moeda.png",frames=6)
             moeda1.x = x + moeda1.width + 400
             x = moeda1.x
             moeda1.y = 600
             lista.append(moeda1)
            if i % 2 == 1:
                moeda1 = Sprite("sprites/moeda.png", frames=6)
                moeda1.x = x + moeda1.width + 500
                x = moeda1.x
                moeda1.y = 700
                lista.append(moeda1)
                moeda1 = Sprite("sprites/moeda.png", frames=6)
                moeda1.x = x + moeda1.width
                x = moeda1.x
                moeda1.y = 700
                lista.append(moeda1)
         b = False
     if b==False:
      for i in range(len(lista)):
          lista[i].set_total_duration(1000)
          lista[i].update()
          lista[i].draw()
     #final da fase
     if jogador.x >= janela.width - 50:
      if tempo_fps_p >= 0.00833333333:
         sound.stop()
         jogador.x=0
         janela.x=0
         fase2(coin,vida, "easy")
         return None
     if teclado.key_pressed("RIGHT"):
       if tempo_fps_p >= 0.00833333333:
         if chao3.width + chao3.x > 1200:
             jogador.move_x(playvel*janela.delta_time())
             tem.move_x(chaovel * janela.delta_time() * -1)
             chao2.move_x(chaovel * janela.delta_time() * -1)
             chao3.move_x(chaovel * janela.delta_time() * -1)
             powerup.move_x(chaovel * janela.delta_time() * -1)
             for i in range(len(lista2)):
                lista2[i].move_x(chaovel * janela.delta_time() * -1)
             for i in range(len(lista3)):
                 lista3[i].move_x(chaovel * janela.delta_time() * -1)
             for i in range(len(lista)):
                 lista[i].move_x(chaovel * janela.delta_time()*-1)
             if andar!=5:
              andar=1
         else:
          jogador.move_x(chaovel * janela.delta_time())
          andar=1
     if teclado.key_pressed("LEFT"):
      if tempo_fps_p >= 0.00833333333:
         if tem.x < 0:
             jogador.move_x(playvel * janela.delta_time()*-1)
             powerup.move_x(chaovel * janela.delta_time())
             tem.move_x(chaovel * janela.delta_time())
             chao2.move_x(chaovel * janela.delta_time())
             chao3.move_x(chaovel * janela.delta_time())
             for i in range(len(lista)):
              lista[i].move_x(chaovel * janela.delta_time())
             for i in range(len(lista2)):
              lista2[i].move_x(chaovel * janela.delta_time())
             for i in range(len(lista3)):
              lista3[i].move_x(chaovel * janela.delta_time())
             if andar!=5:
              andar = 8
     if andar == 1:
       if tempo_fps_p >= 0.00833333333:
         i1-=janela.delta_time()
         if i1 <= 0:
             andar = 2
             i1 = 0.2
     if andar==2:
       if tempo_fps_p >= 0.00833333333:
         jogador.set_sequence_time(4,10,1000,True)
         i1-=tempo
         if i1 <= 0:
          andar = 0
          i1 = 0.5
     if andar == 8:
      if tempo_fps_p >= 0.00833333333:
       i1 -= janela.delta_time()
       if i1 <= 0:
         andar = 9
         i1 = 0.5
     if andar == 9:
      if tempo_fps_p >= 0.00833333333:
       jogador.set_sequence_time(19, 24, 1000, True)
       i1 -= tempo
       if i1 <= 0:
         andar = 0
         i1 = 0.5
     if (teclado.key_pressed("ESC")):
         janela.close()
     #Pulo
     if (teclado.key_pressed("UP")) and not pulo:
      if tempo_fps_p >= 0.00833333333:
         pulovel = -5
         pulo = True
         andar=4
     if pulo:
      if tempo_fps_p >= 0.00833333333:
       if andar==4 :
        jogador.set_sequence_time(11,18,2000,True)
        andar=5
       pulovel += 0.04
       jogador.y += pulovel
     if teclado.key_pressed("RIGHT"):
      if tempo_fps_p >= 0.00833333333:
        i7 -= tempo
        if i7 <= 0:
          andar = 2
          i7=1
     if andar == 5:
      if tempo_fps_p >= 0.00833333333:
       i4 -= tempo
       if i4 <= 0:
        jogador.set_sequence_time(16, 18, 1000, True)
        andar = 6
        i4=1.5
     if jogador.y >= 700:
      jogador.y = 700
      pulo = False

    #moeda colisao
     for i in range(len(lista)):
      if lista !=[]:
       if tempo_fps_p >= 0.00833333333:
        if lista[i].collided(jogador):
          lista.pop(i)
          coin+=1
          break
    #colisao do inimigo com fogo
     for i in range(len(lista2)):
      if lista2!=[] and lista1!=[]:
       if tempo_fps_p >= 0.00833333333:
        if lista2[i].collided(lista1[0]):
         if lista1 != [] and lista2!=[]:
            lista1.pop(0)
            lista2.pop(i)
            break
     for i in range(len(lista3)):
      if lista3!=[] and lista1!=[]:
       if tempo_fps_p >= 0.00833333333:
        if lista3[i].collided(lista1[0]):
         if lista1 != [] and lista2!=[]:
            lista1.pop(0)
            lista3.pop(i)
            break
    #colisao do inimigo
     for i in range(len(lista3)):
       print(jogador.y + jogador.height)
       print(lista3[i].y+30)
       if lista3[i].collided(jogador):
        if tempo_fps_p >= 0.00833333333:
         if jogador.y + jogador.height >= lista3[i].y and jogador.height + jogador.y <= lista3[i].y + 50:
                i6-=janela.delta_time()
                if lista3 != [] and i6<=0:
                     vida-=1
                     i6=0.4
                     break
         if lista3[i].collided(jogador):
             if tempo_fps_p >= 0.00833333333:
                 i3 -= tempo
                 if i3 <= 0:
                     vida -= 1
                     dano = True
                     i3 = 0.8
                     break
     for i in range(len(lista2)):
         if lista2[i].collided(jogador):
          if tempo_fps_p >= 0.00833333333:
             if jogador.height + jogador.y >= lista2[i].y and jogador.height + jogador.y <= lista2[i].y+80:
                 if lista2!=[]:
                    lista2.pop(i)
                    break
             if tempo_fps_p >= 0.00833333333:
              i3 -= tempo
              if i3 <= 0:
               vida -= 1
               dano = True
               i3 = 0.8
               break
     if vida == 0:
         sound.stop()
         vida-=1
     if vida==-1:
         playa(coins,vidas)
     if teclado.key_pressed("G"):
         vida = 0
     janela.draw_text(str(coin),0,200,50,(255,255,0),"Arial",False,False)
     janela.draw_text(f'Hp {str(vida)}', 1000, 200, 50, (255, 255, 0), "Arial", False, False)
     if dano == True:
         janela.draw_text("ouch", 1000, 300, 50, (255, 255, 0), "Arial", False, False)
         i5 -= janela.delta_time()
         if i5 <= 0:
          dano = False
          i5 = 2
     if tempo_fps_p>=0.00833333333:
      tempo_fps+=tempo_fps_p
      fps += 1
      print("ok")
      tempo_fps_p = 0
      janela.update()
      jogador.update()
if __name__ == "__main__":
   playa(0, 20)
