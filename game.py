from pplay.window import Window
from pplay.sprite import Sprite
from pplay.gameimage import GameImage
from pplay.sound import Sound
import random
from fasefloresta import playa
def fase0(nivel):
 janela = Window(1200, 1000)
 janela.set_title("Game")
 janela.clear()
 cenario = GameImage("sprites/Fase1.png")
 jogador = Sprite("sprites/max(1).png", frames=24)
 jogador.set_position(0, 700)
 placa=Sprite("sprites/pointer.png")
 chao = Sprite("sprites/tem.png")
 niveis=nivel
 cenario.set_position(0, 0)
 tem = Sprite('sprites/Tileset.png')
 tem.set_position(0,790)
 chao.set_position(tem.width + tem.x - 50, 640)
 placa.set_position(100,740)
 teclado = Window.get_keyboard()
 chaovel = 200
 inivel=40
 pulovel = 0
 pulo = False
 lista = []
 lista1=[]
 b =True
 d=True
 f=True
 dano=False
 coin=0
 if nivel=="easy":
   vida=20
 if nivel=="medio":
   vida=15
 if nivel=="difficult":
   vida=10
 andar=0
 i1=0.5
 i4=1.5
 i6=1
 i2=1.5
 i5=1
 sound = Sound("sprites/8-bit-dream-land-142093_1.ogg")
 lista2=[]
 lista3=[]
 plats=[]
 plat=False
 i3=1
 plat=0
 passar=True
 tempo_fps=0
 fps=0
 so=0
 tempo_fps_p=0
 while True:
     if passar==True:
        janela.clear()
        passar=False
     #draw
     cenario.draw()
     jogador.draw()
     placa.draw()
     sound.play()
     so+=1
     if tempo_fps >= 1:
         print(fps, "fps")
         print(andar, "andar")
         fps = 0
         tempo_fps = 0
     if andar == 6 and pulo==False or pulo == False and andar == 5:
         andar = 0
     #animacao do player
     if andar==0:
      jogador.set_sequence_time(1,3,500,True)
      jogador.set_total_duration(1000)
      andar=3
     tem.draw()
     chao.draw()
     tempo = janela.delta_time()
     tempo_fps_p += janela.delta_time()
     print(tempo_fps_p,janela.delta_time(),so)
    #fogo de dragao,plataforma e inimigos
     if lista1!=[] and f==True:
      if tempo_fps_p >= 0.00833333333:
        num=len(lista1)-1
        v=random.randint(0,num)
        fogo = Sprite("sprites/Fire_Attack3.png")
        fogo.x = lista1[v].x
        fogo.y = lista1[v].y+25
        lista3.append(fogo)
        f=False
     if f == False:
      if tempo_fps_p >= 0.00833333333:
         i2 -= tempo
         if i2 <= 0:
             if lista3 != []:
               a=len(lista3)-1
               for i in range(a,-1,-1):
                   lista3.pop(i)
             i2 =1.5
             f = True
     if lista3 != []:
      for i in range(len(lista3)):
        lista3[i].draw()
        lista3[i].move_x(100 * 2 * janela.delta_time()*-1)
     x = 0
     inix = 600
     inx = 300
     if d == True:
          for i in range(4):
             plataforma = Sprite("sprites/plat_terra.png")
             plataforma.x = x + 500
             x= plataforma.x + plataforma.width
             plataforma.y = 400
             plats.append(plataforma)
          for i in range(5):
            if i < 3:
             listaini = Sprite("sprites/Fase1eney.png")
             listaini.x = inix + listaini.width + 300
             inix = listaini.x
             listaini.y = 700
             lista2.append(listaini)
            else:
             listaini = Sprite("sprites/ini2.png")
             listaini.x = inix + listaini.width + 800
             inix = listaini.x
             listaini.y = 700
             lista2.append(listaini)
          for i in range(9):
            if i < 3:
             ini = Sprite("sprites/small.png")
             ini.x = inx
             inx = ini.x + ini.width + 200
             ini.y = 725
             lista1.append(ini)
            else:
              ini = Sprite("sprites/small.png")
              ini.x = inx
              inx = ini.x + + ini.width + 800
              ini.y = 730
              lista1.append(ini)

          d = False
     if d==False:
      for i in range(len(plats)):
        plats[i].draw()
      for i in range(len(lista2)):
         if lista2[i].x < tem.x-10:
             lista2.pop(i)
             break
         lista2[i].draw()
         if tempo_fps_p >= 0.00833333333:
          lista2[i].move_x(inivel * janela.delta_time()*-1)
     for i in range(len(lista1)):
        if lista1[i].x < tem.x - 10:
             lista1.pop(i)
             break
        lista1[i].draw()
        if tempo_fps_p >= 0.00833333333:
         lista1[i].move_x(inivel * janela.delta_time() * -1)
     x=0
     x1=500
     tempo=janela.delta_time()
    #gerar moeda
     if b == True:
         for i in range(12):
             if i%2==0:
              moeda1 = Sprite("sprites/moeda.png",frames=6)
              moeda1.x = x + moeda1.width + 200
              x = moeda1.x
              moeda1.y = 740
              lista.append(moeda1)
             else:
                 moeda1 = Sprite("sprites/moeda.png", frames=6)
                 moeda1.x = x + moeda1.width
                 x = moeda1.x
                 moeda1.y = 740
                 lista.append(moeda1)
         for i in range(8):
             if i % 2 == 0:
                 moeda1 = Sprite("sprites/moeda.png", frames=6)
                 moeda1.x = x1
                 x1 = moeda1.x + moeda1.width
                 moeda1.y = 300
                 lista.append(moeda1)
             else:
                 moeda1 = Sprite("sprites/moeda.png", frames=6)
                 moeda1.x = x1
                 x1 = moeda1.x + 600
                 moeda1.y = 300
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
         playa(coin,vida)
         return None
     if teclado.key_pressed("RIGHT"):
       if tempo_fps_p >= 0.00833333333:
         if chao.width + chao.x > 1200:
             jogador.move_x(40*janela.delta_time())
             tem.move_x(chaovel * janela.delta_time() * -1)
             chao.move_x(chaovel * janela.delta_time() * -1)
             placa.move_x(chaovel * janela.delta_time() * -1)
             for i in range(len(lista2)):
                lista2[i].move_x(chaovel * janela.delta_time() * -1)
             for i in range(len(lista)):
                 lista[i].move_x(chaovel * janela.delta_time()*-1)
             for i in range(len(lista1)):
                 lista1[i].move_x(chaovel * janela.delta_time() * -1)
             for i in range(len(plats)):
                 plats[i].move_x(chaovel*janela.delta_time()*-1)
             for i in range(len(lista3)):
                 lista3[i].move_x(100 * 2 * janela.delta_time() * -1)
             if andar!=5:
              andar=1
         else:
          jogador.move_x(chaovel * janela.delta_time())
          if andar != 5:
            andar=1
     if teclado.key_pressed("LEFT"):
      if tempo_fps_p >= 0.00833333333:
         if tem.x < 0:
             jogador.move_x(-40 * janela.delta_time())
             placa.move_x(chaovel * janela.delta_time())
             tem.move_x(chaovel * janela.delta_time())
             chao.move_x(chaovel * janela.delta_time())
             for i in range(len(lista)):
              lista[i].move_x(chaovel * janela.delta_time())
             for i in range(len(lista2)):
              lista2[i].move_x(chaovel * janela.delta_time())
             for i in range(len(lista1)):
              lista1[i].move_x(chaovel * janela.delta_time())
             for i in range(len(plats)):
              plats[i].move_x(chaovel * janela.delta_time())
             if andar != 5:
              andar=8
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
         i1 = 0.2
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
       if andar==4:
        jogador.set_sequence_time(11,18,2000,True)
        andar = 5
       pulovel += 0.03
       jogador.y += pulovel
      for p in plats:
          if jogador.y + jogador.height >= p.y + 25 and jogador.x + jogador.width / 2 >= p.x and jogador.x <= p.x + p.width and pulovel >= 0:
              jogador.y = p.y - jogador.height + 20
              plat_atual = p
              pulo = False
              plat = True
              pulovel = 0
              break
      if teclado.key_pressed("RIGHT"):
       if tempo_fps_p >= 0.00833333333:
        i6 -= tempo
        if i6 <= 0:
         andar = 2
         i6=1
     if andar == 5:
      if tempo_fps_p >= 0.00833333333:
       i4 -= tempo
       if i4 <= 0:
        jogador.set_sequence_time(16, 18, 1000, True)
        andar = 6
        i4 = 1.5
     if jogador.y >= 700:
         jogador.y = 700
         pulovel = 0
         pulo = False
         plat = False
         i4 = 2
     if plat:
      if (jogador.x + jogador.width < plat_atual.x or jogador.x > plat_atual.x + plat_atual.width or jogador.y + jogador.height > plat_atual.y + 20):
       if tempo_fps_p >= 0.00833333333:
        jogador.move_y(300 * janela.delta_time())
    #moeda colisao
     for i in range(len(lista)):
      if lista !=[]:
       if lista[i].collided(jogador):
          lista.pop(i)
          coin+=1
          break
     #pular no inimigos
     for i in range(len(lista2)):
         if lista2[i].collided(jogador):
             if jogador.y <= lista2[i].y - 10 or jogador.y <= lista2[i].y - 50:
                 if lista2 != []:
                     lista2.pop(i)
                     break
             if tempo_fps_p >= 0.00833333333:
              i3 -= tempo
              if i3 <= 0:
                 i3 -= tempo
                 if i3 <= 0:
                     vida -= 1
                     dano = True
                     i3 = 1
     for i in range(len(lista3)):
       if lista3[i].collided(jogador) or teclado.key_pressed("a"):
        if lista3 != []:
          lista3.pop(i)
          vida -= 1
          dano = True
          i3 = 1
          break

     for i in range(len(lista1)):
      if lista1[i].collided(jogador):
         if jogador.y <= lista1[i].y - lista1[i].height or jogador.y <= lista1[i].y - lista1[i].height - 30:
           if lista1 != []:
              lista1.pop(i)
              break
         if tempo_fps_p >= 0.00833333333:
           i3 -= tempo
           if i3 <= 0:
            vida -= 1
            dano = True
            i3 = 1
      if vida==0:
        sound.stop()
        vida=-1
      if vida==-1:
        fase0(niveis)
     if teclado.key_pressed("G"):
       vida=0
     janela.draw_text(str(coin),0,200,50,(255,255,0),"Arial",False,False)
     janela.draw_text(f'Hp {str(vida)}', 1000, 200, 50, (255, 255, 0), "Arial", False, False)
     if dano==True:
      janela.draw_text("ouch", 1000, 300, 50, (255, 255, 0), "Arial", False, False)
      if tempo_fps_p >= 0.00833333333:
       i5-=janela.delta_time()
       if i5<=0:
        dano=False
        i5=1
     if tempo_fps_p>=0.00833333333:
      tempo_fps+=tempo_fps_p
      fps += 1
      tempo_fps_p = 0
      janela.update()
      jogador.update()
if __name__ == "__main__":
    fase0("easy")