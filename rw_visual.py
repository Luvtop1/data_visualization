import matplotlib.pyplot as pst

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока програама остается активной.
while True:
    rw = RandomWalk()
    rw.fill_walk()
    pst.scatter(rw.x_values, rw.y_values, s=15)
    pst.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break