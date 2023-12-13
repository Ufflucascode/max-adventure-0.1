import os,sys
dirparth=os.getcwd()
sys.path.append(dirparth)
if getattr(sys,"frozen",False):
    os.chdir(sys._MEIPASS)

from pplay.sprite import Sprite
from pplay.window import Window
from game import fase0
from dil import dif
def menu():
 janela = Window(1200,1000)
 janela.set_title("menu")
 d = Sprite("sprites/JOGAR6.png")
 janela.clear()
 dx = janela.width/2 - d.width/2
 d.set_position(dx,200)
 a= Sprite("sprites/DIFICULDADE3.png")
 a.set_position(dx,400)
 c = Sprite("sprites/SAIR3.png")
 c.set_position(dx,600)
 mouse=Window.get_mouse()
 passar=True
 click=False
 nivel="easy"
 i1=1
 while True:
     i1-=janela.delta_time()
     if i1<=-1:
         click=False
     if mouse.is_over_object(d) and mouse.is_button_pressed(1) and click==False:
       janela.clear()
       fase0(nivel)
     if mouse.is_over_object(a) and mouse.is_button_pressed(1) and click==False:
        click=True
        nivel=dif()
     if mouse.is_over_object(c) and mouse.is_button_pressed(1) and click==False:
       janela.close()
     janela.set_background_color((255, 255, 0))
     d.draw()
     a.draw()
     c.draw()
     janela.update()
if __name__ == "__main__":
 menu()