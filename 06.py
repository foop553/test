#2.12
# Murman-Cole
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

dt	= 0.05
dx	= 0.1

xmax = 2.0
jmax = (int)(xmax/dx)+1
nmax = 6

def init(q1, q2, dx, jmax):
	xs = -1.0 #始点
	x = np.linspace(xs, xs + dx * (jmax-1), jmax)
	q = np.array([( float(q1) if i < 0.0 else float(q2) ) for i in x])
	return (x, q)

def do_computing(x, q, dt, dx, nmax, ff, order=1, interval=2):
	plt.figure(figsize=(7,7), dpi=100)
	plt.rcParams["font.size"] = 15

	# 初期分布
	plt.plot(x, q, marker='o', lw=2, label='n=0')

	for n in range(1, nmax+1):
		qold = q.copy()
		for j in range(order, jmax-order):
			ff1 = ff(qold, qold[j], dt, dx, j)
			ff2 = ff(qold, qold[j], dt, dx, j-1)
			q[j] = qold[j] - dt / dx * (ff1 - ff2)

		if n%interval == 0:
			plt.plot(x, q, marker='o', lw=2, label=f'n={n}')

	# グラフの後処理
	plt.grid(color='black', linestyle='dashed', linewidth=0.5)
	plt.xlabel('x')
	plt.ylabel('q')
	plt.legend()
	plt.show()

def MC(q, c, dt, dx, j):
	ur = q[j+1]
	ul = q[j]
	fr = 0.5 * ur**2
	fl = 0.5 * ul**2
	c = 0.5 * (ur + ul)
	return 0.5 * (fr + fl - np.sign(c) * (fr - fl))


q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
nmax = 20
do_computing(x, q, dt, dx, nmax, MC, interval = 5)
