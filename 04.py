import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

dt = 0.05
dx = 0.1

xmax = 2.0
jmax = (int)(xmax/dx)+1
nmax = 6

def init(q1, q2, dx, jmax):
	x = np.linspace(0, dx * (jmax-1), jmax)
	q = np.array([( float(q1) if i < 0.5 * jmax else float(q2) ) for i in range(jmax)])
	return (x, q)

# FTCS
def FTCS(q, c, dt, dx, j):
	return 0.5 * c * (q[j+1] + q[j])

# １次精度風上法
def UPWIND1(q, c, dt, dx, j):
	return c * q[j]

# Lax
def LAX(q, c, dt, dx, j):
	nu2 = dx / (c * dt)
	return 0.5 * c * ( (1-nu2) * q[j+1] + (1+nu2) * q[j] )

# Lax-Wendroff
def LAXWEN(q, c, dt, dx, j):
	nu = c * dt / dx
	return 0.5 * c * ( (1-nu) * q[j+1] + (1+nu) * q[j] )

# グラフ
def do_computing(x, q, c, dt, dx, nmax, ff):

	plt.figure(figsize=(7,7), dpi=100)
	plt.rcParams["font.size"] = 15

	# 初期分布
	plt.plot(x, q, marker='o', lw=2, label='n=0')

	for n in range(1, nmax+1):
		qold = q.copy()
		for j in range(1, jmax-1):
			ff1 = ff(qold, c, dt, dx, j)
			ff2 = ff(qold, c, dt, dx, j-1)
			q[j] = qold[j] - dt / dx * (ff1 - ff2)

		if n%2 == 0:
			plt.plot(x, q, marker='o', lw=2, label=f'n={n}')

	# グラフの後処理
	plt.grid(color='black', linestyle='dashed', linewidth=0.5)
	plt.xlim([0, xmax])
	plt.ylim([0, 1.2])
	plt.xlabel('x')
	plt.ylabel('q')
	plt.legend()
	plt.show()


c = 1
q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, UPWIND1)

c = 1
q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, FTCS)

c = 1
q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, LAX)

c = 1
q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, LAXWEN)
