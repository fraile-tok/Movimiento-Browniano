import random
import matplotlib.pyplot as pyplot

brownianMotion = []

# Variables
steps = 200
dist = 10
pos = 0

# Simulation
for n in range(steps):
    rand = random.randint(0,1)
    if rand == 0:
        pos = pos+dist
    else:
        pos = pos-dist
    brownianMotion.append(pos)

# Styling
pyplot.title("Movimiento Browniano")
pyplot.xlabel("Pasos")
pyplot.ylabel("Distancia")

# Plotting
pyplot.plot(brownianMotion)

pyplot.show()