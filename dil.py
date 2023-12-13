from pplay.sprite import Sprite
from pplay.window import Window
def dif():
    janela = Window(1200, 1000)
    janela.set_title("Space Invaders")
    b = Sprite("sprites/FACIL.png")
    b.x = janela.width / 2 - b.width / 2
    b.y = 150

    l = Sprite("sprites/MEDIO.png")
    l.x = janela.width / 2 -b.width / 2
    l.y = 400
    janela.clear()
    d = Sprite("sprites/DIFICIL.png")
    d.x = janela.width / 2 -b.width / 2
    d.y = 650
    mouse = Window.get_mouse()
    teclado=Window.get_keyboard()
    passar=False
    cl=False
    i1=1
    while True:
        if cl==False:
            i1-=janela.delta_time()
            if i1<=-0.4:
             cl=True
        if passar==False:
            janela.clear()
            passar=True
        if mouse.is_over_object(b) and mouse.is_button_pressed(1) and cl==True:
            janela.clear()
            return "easy"
        if mouse.is_over_object(l) and mouse.is_button_pressed(1) and cl==True:
            janela.clear()
            return "medio"
        if mouse.is_over_object(d) and mouse.is_button_pressed(1) and cl==True:
            janela.clear()
            return "difficult"
        if teclado.key_pressed("esc"):
            janela.close()
        janela.set_background_color((255, 255, 0))
        b.draw()
        l.draw()
        d.draw()
        janela.update()
if __name__ == "__main__":
    dif()