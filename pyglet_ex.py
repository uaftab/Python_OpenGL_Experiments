##import pyglet
##
##win = pyglet.window.Window()
##
##@win.event
##def on_draw():
##        win.clear()
##
##pyglet.app.run()


##import pyglet
##from pyglet.gl import *
##
##win = pyglet.window.Window()
##
##@win.event
##def on_draw():
##
##        # Clear buffers
##        glClear(GL_COLOR_BUFFER_BIT)
##
##        # Draw some stuff
##        glBegin(GL_POINTS)
##        glVertex2i(50, 50)
##        glVertex2i(75, 100)
##        glVertex2i(100, 150)
##        glEnd()
##
##pyglet.app.run()


##import pyglet
##from pyglet.gl import *
##
##win = pyglet.window.Window()
##
##@win.event
##def on_draw():
##
##        # Clear buffers
##        glClear(GL_COLOR_BUFFER_BIT)
##
##        # Draw some stuff
##        glBegin(GL_LINES)
##        glVertex2i(50, 50)
##        glVertex2i(75, 100)
##        glVertex2i(100, 150)
##        glVertex2i(200, 200)
##        glEnd()
##
##pyglet.app.run()


import pyglet

window = pyglet.window.Window()
image = pyglet.image.load('image1.jpg')

@window.event
def on_draw():
    window.clear()
    image.blit(1, 1,2)

pyglet.app.run()
