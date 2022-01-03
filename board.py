from __future__ import division
from pyglet.window import key
import pyglet
from pyglet import shapes

width = 600
height = 600
window = pyglet.window.Window(visible=True, fullscreen=True, caption='Monopoly')
board = pyglet.image.load("pictures/board.png")

label = pyglet.text.Label('Bienvenue au Monopoly',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height//2,
                      anchor_x='center', anchor_y='center')

window.set_mouse_visible(False)
pyglet.gl.glClearColor(0, 0, 0, 1)

batch = pyglet.graphics.Batch()
label_chance = pyglet.text.Label('Chance',font_name='Times New Roman',font_size=20, color = (0,0,0,255), x=11*window.height//22, y=11*window.height//22,anchor_x='center', anchor_y='center')

label_player = pyglet.text.Label('C\'est à :',font_name='Times New Roman',font_size=25, color = (0,0,0,255), x=window.height + 10, y=21*window.height//22,anchor_x='left', anchor_y='center')
label_name = pyglet.text.Label('Player Name',font_name='Times New Roman',font_size=25, color = (0,0,0,255), x=window.height + 150, y=21*window.height//22,anchor_x='left', anchor_y='center')
label_have = pyglet.text.Label('Vous avez :',font_name='Times New Roman',font_size=18, color = (0,0,0,255), x=window.height + 10, y=19*window.height//22,anchor_x='left', anchor_y='center')
label_money = pyglet.text.Label('X €',font_name='Times New Roman',font_size=18, color = (0,0,0,255), x=window.height + 150, y=19*window.height//22,anchor_x='left', anchor_y='center')
label_properties1 = pyglet.text.Label('prop1',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150, y=18*window.height//22,anchor_x='left', anchor_y='center')
label_properties2 = pyglet.text.Label('prop2',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150, y=17*window.height//22,anchor_x='left', anchor_y='center')
label_properties3 = pyglet.text.Label('prop3',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150, y=16*window.height//22,anchor_x='left', anchor_y='center')
label_properties4 = pyglet.text.Label('prop4',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150, y=15*window.height//22,anchor_x='left', anchor_y='center')
label_properties5 = pyglet.text.Label('prop5',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150 + (window.width - (window.height + 150))/2, y=19*window.height//22,anchor_x='left', anchor_y='center')
label_properties6 = pyglet.text.Label('prop6',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150 + (window.width - (window.height + 150))/2, y=18*window.height//22,anchor_x='left', anchor_y='center')
label_properties7 = pyglet.text.Label('prop7',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150 + (window.width - (window.height + 150))/2, y=17*window.height//22,anchor_x='left', anchor_y='center')
label_properties8 = pyglet.text.Label('prop8',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150 + (window.width - (window.height + 150))/2, y=16*window.height//22,anchor_x='left', anchor_y='center')
label_properties9 = pyglet.text.Label('prop9',font_name='Times New Roman',font_size=15, color = (0,0,0,255), x=window.height + 150 + (window.width - (window.height + 150))/2, y=15*window.height//22,anchor_x='left', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    #player.draw()
    batch.draw()
    #label.draw()
    board.blit(0,0)
    label_chance.draw()
    label_player.draw()
    label_name.draw()
    label_money.draw()
    label_have.draw()
    label_properties1.draw()
    label_properties2.draw()
    label_properties3.draw()
    label_properties4.draw()
    label_properties5.draw()
    label_properties6.draw()
    label_properties7.draw()
    label_properties8.draw()
    label_properties9.draw()

if __name__ == '__main__':
    pyglet.app.run()

print(window.width)
print(window.height)