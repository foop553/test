import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

dt	= 0.05
dx	= 0.1

xmax = 2.0
jmax = (int)(xmax/dx)+1
nmax = 6

def init(q1, q2, dx, jmax):
	x = np.linspace(0, dx * (jmax-1), jmax)
	q = np.array([( float(q1) if i < 0.5 * jmax else float(q2) ) for i in range(jmax)])
	return (x, q)

# １次精度風上法
def UPWIND1(q, c, dt, dx, j):
	ur = q[j+1]
	ul = q[j]
	fr = c * ur
	fl = c * ul
	return 0.5 * (fr + fl - abs(c) * (ur - ul))

def UPWIND2(q, c, dt, dx, j):
	ur = 1.5 * q[j+1] - 0.5 * q[j+2]
	ul = 1.5 * q[j]   - 0.5 * q[j-1]
	fr = c * ur
	fl = c * ul
	return 0.5 * (fr + fl - abs(c) * (ur - ul))

# グラフ
def do_computing(x, q, c, dt, dx, nmax, ff, order=1, interval=2, ylim=None, yticks=None):
	plt.figure(figsize=(7,7), dpi=100)
	plt.rcParams["font.size"] = 15

	# 初期分布
	plt.plot(x, q, marker='o', lw=2, label='n=0')

	for n in range(1, nmax+1):
		qold = q.copy()
		for j in range(order, jmax-order):
			ff1 = ff(qold, c, dt, dx, j)
			ff2 = ff(qold, c, dt, dx, j-1)
			q[j] = qold[j] - dt / dx * (ff1 - ff2)

		if n%interval == 0:
			plt.plot(x, q, marker='o', lw=2, label=f'n={n}')

	# グラフの後処理
	plt.grid(color='black', linestyle='dashed', linewidth=0.5)
	plt.xlabel('x')
	plt.ylabel('q')
	plt.legend()
	plt.xlim([0, xmax])
	if ylim is not None:
		plt.ylim(ylim)
	if yticks is not None:
		plt.yticks(yticks)
	plt.show()

c = 1
q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, UPWIND1)

c = -1
q1, q2 = 0, 1
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, UPWIND1)

c = 1
q1, q2 = 1, 0
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, UPWIND2, order=2, ylim=[-1, 1.1], yticks=np.arange(-1, 1.1, 0.2))

c = -1
q1, q2 = 0, 1
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, c, dt, dx, nmax, UPWIND2, order=2, ylim=[-1, 1.1], yticks=np.arange(-1, 1.1, 0.2))
