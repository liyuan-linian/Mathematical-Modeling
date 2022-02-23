import numpy as np
import geatpy as ea
import matplotlib.pyplot as plt


class MyProblem1(ea.Problem):
    def __init__(self):
        name = 'MyProblem1'
        M = 5
        maxormins = [-1] * M
        Dim = 5
        varTypes = [0] * Dim
        lb = [0] * 5
        ub = [100] * 5
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub)

    def aimFunc(self, pop):
        Vars = pop.Phen
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]

        f1 = 16.17 * x1 + 4.38 * (x1 + 82.6)
        f2 = 5.35 * x2 + 4.38 * (x2 - 8.2)
        f3 = 5.33 * x3 + 4.38 * (x3 + 227.1)
        f4 = 10.53 * x4 + 4.38 * (x4 - 136.6)
        f5 = 8.03 * x5 + 4.38 * (x5 - 35.8)

        pop.ObjV = np.hstack([f1, f2, f3, f4, f5])

        pop.CV = np.hstack([
            x1 + x2 + x3 + x4 + x5 - 100
        ])

#灵敏度分析
class MyProblem2(ea.Problem):
    def __init__(self):
        name = 'MyProblem2'
        M = 5
        maxormins = [-1] * M
        Dim = 5
        varTypes = [0] * Dim
        lb = [0] * 5
        ub = [100] * 5
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub)

    def aimFunc(self, pop):
        Vars = pop.Phen
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]

        f1 = 15.36 * x1 + 4.38 * (x1 + 82.6)
        f2 = 5.61 * x2 + 4.38 * (x2 - 8.2)
        f3 = 5.06 * x3 + 4.28 * (x3 + 227.1)
        f4 = 10 * x4 + 4.38 * (x4 - 136.6)
        f5 = 8.43 * x5 + 4.48 * (x5 - 35.8)

        pop.ObjV = np.hstack([f1, f2, f3, f4, f5])

        pop.CV = np.hstack([
            x1 + x2 + x3 + x4 + x5 - 100
        ])


problem1 = MyProblem1()
#problem2 = MyProblem2()

Encoding = 'RI'
NIND = 100

Field1 = ea.crtfld(Encoding, problem1.varTypes, problem1.ranges, problem1.borders)
population = ea.Population(Encoding, Field1, NIND)
my1 = ea.moea_NSGA2_templet(problem1, population)
'''
Field = ea.crtfld(Encoding, problem2.varTypes, problem2.ranges, problem2.borders)
population = ea.Population(Encoding, Field, NIND)
my2 = ea.moea_NSGA2_templet(problem2, population)
'''
my1.MAXGEN = 1000
#my2.MAXGEN = 1000
my1.mutOper.pm = 0.2
#my2.mutOper.pm = 0.2
my1.recOper.XOVR = 0.7
#my2.recOper.XOVR = 0.7
my1.logTras = 0
#my2.logTras = 1
my1.verbose = True
#my2.verbose = True
my1.drawing = 2
#my2.drawing = 0


[Best1, population1] = my1.run()
#[Best2, population2] = my2.run()

Best1.save()

# print('total time %s  % sec' % my1.passTime,my2.passTime)
# print('not controll 1 count % ge' % Best1.sizes) if Best1.sizes != 0 else print('None')

# print('not controll 2 count % ge' % Best2.sizes) if Best2.sizes != 0 else print('None')

# if my1.log is not None and Best1.sizes != 0:
#   print('GD', my1.log['gd'][-1])
#  print('IGD', my1.log['igd'][-1])
# print('HV', my1.log['hv'][-1])
# print('Spacing', my1.log['spacing'][-1])

metricName = [['spacing'], ['hv']]
Metrics = np.array([my1.log[metricName[i][0]] for i in range(len(metricName))]).T

ea.trcplot(Metrics, labels=metricName, titles=metricName)

'''
spacing1 = np.array([my1.log['spacing']]).T
spacing2 = np.array([my2.log['spacing']]).T

hv1 = np.array([my1.log['hv']]).T
hv2 = np.array([my2.log['hv']]).T

fig, ax = plt.subplots()
x1 = np.array([range(0, len(spacing1))]).T
x2 = np.array([range(0, len(spacing2))]).T
ax.plot(x1, spacing1, label='original set')
ax.plot(x2, spacing2, label='validation set')
ax.legend()
plt.show()

fig1, ax1 = plt.subplots()

ax1.plot(x1, hv1, label='original set')
ax1.plot(x2, hv2, label='validation set')
ax1.legend()
plt.show()

# Metrics = np.array([my.log[metricName[i][0]] for i in range(len(metricName))]).T
'''
