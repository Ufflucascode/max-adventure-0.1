from pplay.sprite import Sprite
from pplay.window import Window
def final():
 janela = Window(1200, 1000)
 janela.set_title("menu")
 a=Sprite("sprites/fechar.png")
 mouse=Window.get_mouse()
 dx = janela.width/2 - a.width/2
 a.set_position(dx,600)
 passar=True
 while True:
     if passar==True:
      janela.clear()
      passar=False
     if mouse.is_over_object(a) and mouse.is_button_pressed(1):
       janela.close()
     janela.set_background_color((255, 255, 0))
     a.draw()
     janela.draw_text("Feito pelo:", 400, 200, 50, (255,0, 0), "Arial", False, False)
     janela.draw_text("Ananias Correa ", 400, 300, 50, (255,0 , 0), "Arial", False, False)
     janela.draw_text("lucas de lima moura", 400, 400, 50, (255, 0, 0), "Arial", False, False)
     janela.update()
if __name__ == "__main__":
    final()
