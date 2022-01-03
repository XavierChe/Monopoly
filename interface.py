import pyglet
from pyglet import shapes
import propriete as prop


def draw_prop(propriete: prop.Property = prop.Property(), width=300, height=400, color=(100, 100, 100)):
    card = pyglet.window.Window(width + 15, height + 15, propriete.name())
    pyglet.gl.glClearColor(255, 255, 255, 0)
    batch_card = pyglet.graphics.Batch()
    rec0 = shapes.Rectangle(5, 5, width, height, color=(0, 0, 0), batch=batch_card)
    rec1 = shapes.Rectangle(5 + 2, 5 + 2, width - 4, height - 4, color=(255, 255, 255), batch=batch_card)
    rec2 = shapes.Rectangle(5 + 2, 5 + 4 * height / 5, width - 4, height / 5 - 2, color=color, batch=batch_card)
    rec3 = shapes.Rectangle(5 + 2, 5 + 4 * height / 5 - 2, width - 4, 2, color=(0, 0, 0), batch=batch_card)
    label_name_prop = pyglet.text.Label(propriete.name(),
                              font_name='Arial',
                              font_size=20,
                              x=width // 2, y= height - 35,
                              anchor_x='center', anchor_y='center')
    label_price_no_houses = pyglet.text.Label("Loyer terrain nu : ",
                                        font_name='Arial',
                                        font_size=15,
                                        x=width // 2, y=height - 100,
                                        anchor_x='center', anchor_y='center',color=(0,0,0,255))
    @card.event
    def on_draw():
        card.clear()
        batch_card.draw()
        label_name_prop.draw()
        label_price_no_houses.draw()

    return [card,rec0, rec1, rec2, rec3, label_name_prop, label_price_no_houses]


rec = draw_prop(prop.Property(name="Rue de la Paix"), color=(34,66,124))


print("hello")
pyglet.app.run()
