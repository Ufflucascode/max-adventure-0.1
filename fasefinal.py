from pplay.window import Window
from pplay.sprite import Sprite
from pplay.gameimage import GameImage
from pplay.sound import Sound
from credito import final
import random
def fase1(coin,vida):
 janela = Window(1200, 1000)
 janela.set_title("Max's Odssey")
 janela.clear()
 vidas = vida
 coins=coin
 jog = Sprite("sprites/max(1).png",frames=24)
 cenario = GameImage("sprites/castelo.jpeg")
 sound=Sound("sprites/the-final-boss-battle-158700.ogg")
 chao = Sprite("sprites/chaopedra.png")
 powerup = Sprite("sprites/powerup.png")
 hp=Sprite("sprites/life.png")
 iconefire=Sprite("sprites/bolafogo1.png")
 iconefire.set_position(1000,300)
 dra=Sprite("sprites/dragon.png",frames=23)
 vidadrag=50
 dano=0
 dra.set_position(1500,615)
 jog.set_position(0,715)
 hp.set_position(300,730)
 powerup.set_position(200,730)
 cenario.set_position(0,0)
 chao.set_position(0,800)
 teclado=Window.get_keyboard()
 tp=2
 pulo = False
 andar=0
 b=True
 c=False
 lista=[]
 playvel = 150
 chaovel = 200
 passar=False
 janela.clear()
 b1=0
 i2=1
 i1=0.4
 i3=3
 i4=2
 i5=4
 i6=1
 i7=1.5
 hit=2
 b2=True
 b3=True
 b4=True
 b6=False
 danos=False
 b5=0
 f=False
 f2=False
 i9=3
 lista1=[]
 lista3=[]
 c1=True
 r=True
 tempo_fps = 0
 fps = 0
 tempo_fps_p = 0
 while True:

   if andar == 0:
       jog.set_sequence(1, 3, True)
       jog.set_total_duration(2000)
       andar = 3
   cenario.draw()
   powerup.draw()
   jog.draw()
   dra.draw()
   hp.draw()
   chao.draw()
   sound.play()
   tempo_fps_p += janela.delta_time()
   if tempo_fps >= 1:
       print(fps, "fps")
       fps = 0
       tempo_fps = 0
   if passar == False:
    janela.clear()
    passar = True
   x=0
   if powerup.collided(jog) and c1==True:
     c = True
     powerup.hide()
     c1 = False
   if c1==False:
    iconefire.draw()
   if hp.collided(jog) and r==True:
    if tempo_fps_p >= 0.00833333333:
       hp.hide()
       vida+=10
       r=False
   if teclado.key_pressed("ESC"):
       janela.close()
   if lista1 != []:
       for i in range(len(lista1)):
           lista1[i].draw()
           if tempo_fps_p >= 0.00833333333:
            lista1[i].move_x(chaovel*1.8* janela.delta_time())
           if lista1 != []:
               if lista1[0].x >= jog.x + 700:
                   if lista1 != []:
                       lista1.pop(0)
                       break
   if f==True:
     fogo = Sprite("sprites/Fire_Attack3.png")
     fogo.x = dra.x
     fogo.y = (dra.y+80)
     if len(lista3) <=2:
      lista3.append(fogo)
     f=False
     if lista3 != []:
      for i in range(len(lista3)):
        if len(lista3) > 1 :
          if i>0:
            lista3.pop(i)
  #fogo do dragao
   if lista3!=[]:
       for i in range(len(lista3)):
           lista3[i].draw()
           if tempo_fps_p >= 0.00833333333:
            lista3[i].move_x(chaovel*1.2*janela.delta_time()*-1)
       a = len(lista3) - 1
       for i in range(a, -1, -1):
           if lista3[i].x < -50:
               lista3.pop(i)
       for i in range(len(lista3)):
        if lista3!=[]:
         if tempo_fps_p >= 0.00833333333:
          if lista3[i].collided(jog):
              vida-=1
              danos=True
              if len(lista3) < 2:
               lista3.pop(i)
              else:
                lista3=[]
   if b == True:
    for i in range(6):
      moeda1 = Sprite("sprites/moeda.png", frames=6)
      moeda1.x = x + moeda1.width + 400
      x = moeda1.x
      moeda1.y = 750
      lista.append(moeda1)
    b = False
   if b == False:
     for i in range(len(lista)):
        lista[i].set_total_duration(1000)
        lista[i].update()
        lista[i].draw()
   if b1 == 0:
      dra.set_sequence(1, 7, True)
      dra.set_total_duration(2000)
      b1 = 3
 #movimento de dragao
   if b1 != 5 and b3 == False:
       b3 = True
   if dra.x >= 1000:
       b2 = True
       b3 = True
       b4=True
       b6 = False
       if b2==True:
        b1 = 0
   if (b2==True and b3==True and dano!=hit and b4==True):
    if tempo_fps_p >= 0.00833333333:
     dra.move_x(chaovel*1.5*janela.delta_time()*-1)
   if(dra.x <= 150):
    i6-=janela.delta_time()
    b4=False
    b1=10
    if b1==10:
      dra.set_sequence(1,2)
      b1=3
    if i6<=0:
     b3=False
     b6=True
     i6=1
     b2=False
   if b6==True:
       b1=1
   if b1==1:
      dra.set_sequence(8,14,True)
      b1=3
   if (b2==False and not dano==hit and b5==True or b6==True):
    if tempo_fps_p >= 0.00833333333:
     dra.move_x(chaovel *1.5*janela.delta_time())
 #andar
   if teclado.key_pressed("a") or vidadrag<=0:
      dra.hide()
      sound.stop()
      f2=True
   if f2==True:
    if tempo_fps_p >= 0.00833333333:
      i3 = 100
      dra.set_position(0,0)
      i9-=janela.delta_time()
      if i9<=0:
       print("teste")
       b3=False
       b6=False
       final()
   if teclado.key_pressed("RIGHT"):
    if tempo_fps_p >= 0.00833333333:
     if chao.width + chao.x > 1200:
        jog.move_x(playvel*janela.delta_time()*0.4)
        chao.move_x(chaovel*janela.delta_time()*-1)
        powerup.move_x(chaovel*janela.delta_time()*-1)
        if dano == hit:
            dra.move_x(chaovel * janela.delta_time() * -1)
        if b3==False:
            dra.move_x(chaovel * janela.delta_time()*-1)
        if lista3 != []:
            for i in range(len(lista3)):
                lista3[i].move_x(chaovel * janela.delta_time() * -1)
        if lista1!=[]:
            for i in range(len(lista1)):
             lista1[i].move_x(chaovel * janela.delta_time()*-1)
        andar=1
        for i in range(len(lista)):
            lista[i].move_x(playvel * janela.delta_time() * -1)
        hp.move_x(chaovel * janela.delta_time()*-1)
     else:
        jog.move_x(chaovel*janela.delta_time())
   if teclado.key_pressed("LEFT"):
     if tempo_fps_p >= 0.00833333333:
      if chao.x < 0:
          jog.move_x(playvel * janela.delta_time() * 0.4 * -1)
          chao.move_x(chaovel*janela.delta_time())
          powerup.move_x(chaovel * janela.delta_time())
          if lista1 != []:
           for i in range(len(lista1)):
             lista1[i].move_x(chaovel * janela.delta_time())
          if lista !=[]:
           for i in range(len(lista)):
            lista[i].move_x(chaovel * janela.delta_time())
          if dano == hit:
              dra.move_x(chaovel * janela.delta_time())
          if b3 == False:
              dra.move_x(chaovel * janela.delta_time())
          hp.move_x(chaovel * janela.delta_time())
          andar = 7
 #bola de fogo
   if teclado.key_pressed("SPACE"):
    if tempo_fps_p >= 0.00833333333:
       if c == True:
           fogo = Sprite("sprites/bolafogo1.png")
           fogo.x = jog.x
           fogo.y = jog.y+50
           lista1.append(fogo)
           c = False
   if c == False:
     if tempo_fps_p >= 0.00833333333:
        i2 -= janela.delta_time()
        if i2 <= 0:
           c = True
           i2 = 1
   for i in range(len(lista1)):
       if lista1[i].x > jog.x+400:
           lista1.pop(i)
           break
 #animacao
   if andar == 1:
       i1-=janela.delta_time()
       if i1<=0:
           andar=2
           i1=0.4
   if andar == 2:
       jog.set_sequence(4, 10,  True)
       i1 -= janela.delta_time()
       if tempo_fps_p >= 0.00833333333:
        if i1 <=0:
           andar = 0
           i1=0.5
   if andar == 7:
    if tempo_fps_p >= 0.00833333333:
       i1 -= janela.delta_time()
       if i1 <= 0:
           andar = 8
           i1 = 0.45
   if andar == 8:
       jog.set_sequence(19, 24, True)
       if tempo_fps_p >= 0.00833333333:
        i1 -= janela.delta_time()
        if i1 <= 0:
           andar = 0
           i1 = 0.5
   #fogo do dragao
   if tempo_fps_p >= 0.00833333333:
    i3-=janela.delta_time()
   if i3<=0 and b3==True:
    if b2==True and not dano==hit:
       b1=5
    if b1==5:
       dra.set_sequence(20, 21, True)
       b3=False
       f=True
   if b1==5:
    if tempo_fps_p >= 0.00833333333:
     i4-=janela.delta_time()
     if i4<=0:
       b1=0
       b3=True
       i3 = 3
       i4=2
   if jog.x >= janela.width-50:
      print("fim")
   if teclado.key_pressed("G"):
    if tempo_fps_p >= 0.00833333333:
       vida=0
   if vida==0:
     sound.stop()
     vida=-1
   if vida==-1:
     janela.clear()
     fase1(coins,vidas)
 #pulo
   if (teclado.key_pressed("UP")) and not pulo:
    if tempo_fps_p >= 0.00833333333:
     pulo = True
     pulovel = -5
   if pulo:
    if tempo_fps_p >= 0.00833333333:
      pulovel += 0.036
      jog.y += pulovel
      if jog.y >= 710:
          pulo = False
          pulovel = 0
   #Moeda
   for i in range(len(lista)):
     if lista != [] :
         if lista[i].collided(jog):
          if tempo_fps_p >= 0.00833333333:
             lista.pop(i)
             coin += 1
             break
   for i in range(len(lista1)):
     if lista1 != [] and not dano==hit:
      if tempo_fps_p >= 0.00833333333:
         if lista1[i].collided(dra):
             lista1.pop(i)
             vidadrag-=4
             dano+=1
             if hit==5:
                dano+=2
             break
   if dra.collided(jog) and dano!=hit:
    if tempo_fps_p >= 0.00833333333:
      i7-=janela.delta_time()
      if i7<=0:
       danos=True
       vida-=1
       i7=1.5

#dano
   if dano == hit:
     b1=6
     b6=False
     if dra.collided(jog):
        if jog.y <= dra.y+150 and jog.height + jog.y <= dra.y + 50:
          if tempo_fps_p >= 0.00833333333:
            if i7<=0:
             vidadrag=-4
             i7=1.5
            pulovel=-3
     dra.y = 630
     if b1==6:
      dra.set_sequence(22,23,True)
     if tempo_fps_p >= 0.00833333333:
      i5-=janela.delta_time()
      if i5<=0:
       b1=0
       b2=False
       b6=True
       i3=3
       dra.y=615
       dano=0
       hit+=1
       i5=6
   janela.draw_text(str(coin),0,200,50,(255,255,0),"Arial",False,False)
   janela.draw_text(f'Hp {str(vida)}', 1000, 200, 50, (255, 255, 0), "Arial", False, False)
   if danos == True:
       janela.draw_text("ouch", 1100, 280, 50, (255, 255, 0), "Arial", False, False)
       if tempo_fps_p >= 0.00833333333:
        tp -= janela.delta_time()
        if tp <= 0:
           danos = False
           tp = 1
   if tempo_fps_p >= 0.00833333333:
       tempo_fps += tempo_fps_p
       fps += 1
       tempo_fps_p = 0
       janela.update()
       dra.update()
       jog.update()
if __name__ == "__main__":
    fase1(0,20)