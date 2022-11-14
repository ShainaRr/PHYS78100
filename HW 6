import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as nr

L = 101
N = 1000
up = 1
down = 2
left = 3
right = 4
fig = plt.figure(figsize=(10,10))
ax = plt.axes(xlim=(0, L), ylim=(0, L))
particle = plt.Circle((L/2, L/2), 0.5, fc='b')

def init():
    particle.center = (L/2, L/2)
    ax.add_patch(particle)
    return particle,

def move():
    direction = nr.randint(1, 5)
    if (direction == up):
        x = particle.center[0]
        y = 1 + particle.center[1]

    else:
        if (direction == down):
            x = particle.center[0]
            y = -1 + particle.center[1]

        else:
            if (direction == left):
                x = -1 + particle.center[0]
                y = particle.center[1]

            else:
                if (direction == right):
                    x = 1 + particle.center[0]
                    y = particle.center[1]
    if (x >= 0.5) and (x <= (L - 0.5)) and (y >= 0.5) and (y <= (L - 0.5)):
        particle.center = (x, y)
    else:
        move()

def animate(k):
    move()
    return particle,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=N, interval=40, blit=False)
#save as a gif
writergif = animation.PillowWriter(fps=25)
anim.save('filename.gif',writer=writergif)
