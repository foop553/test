import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

g = 9.8
v0 = 10
h0 = 0
dt = 0.05

plt.figure(figsize=(7,7), dpi=100)
plt.rcParams["font.size"] = 25

# Analytical Solution
t = np.linspace(0, 2*v0/g, 100)
h = -0.5*g*t**2 + v0*t + h0
la, = plt.plot(t, h, color='blue')

# Numerical Solution
t = 0
h = h0
while h>=h0:
	ln = plt.scatter(t, h, marker='o', c='black')
	h += (-g * t + v0) * dt
	t += dt

# ato syori
plt.grid(color='black', linestyle='dashed', linewidth=0.5)
plt.xlabel('Time')
plt.ylabel('Height')
plt.legend(handles=[la, ln], labels=['Analytical', 'Numerical'])
plt.show()
