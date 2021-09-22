import random
import matplotlib.pyplot as plt

plt.autoscale(enable=True, axis='y', tight=None)

y = 0
MovBrown = []

for n in range(200):
    rand = random.randint(0,1)
    if rand == 0:
        y = y+10
    else:
        y = y-10
    MovBrown.append(y)

plt.plot(MovBrown)
plt.show()