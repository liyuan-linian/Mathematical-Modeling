import numpy as np
import geatpy as ea
import matplotlib.pyplot as plt


class MyProblem1(ea.Problem):
    def __init__(self):
        name = 'MyProblem1'
        M = 6
        maxormins = [-1] * M
        Dim = 6
        varTypes = [0] * Dim
        lb = [0] * 6
        ub = [100] * 6
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub)

    def aimFunc(self, pop):
        Vars = pop.Phen
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]
        x6 = Vars[:, [5]]

        f1 = 8.60 * x1 + 88 * (x1 - 1.83)
        f2 = 11.78 * x2 + 88 * (x2 - 5.12)
        f3 = 16.29 * x3 + 88 * (x3 - 0.325)
        f4 = 13.4 * x4 + 88 * (x4 - 1.62)
        f5 = 11.09 * x5 + 88 * (x5 - 0.18)
        f6 = 14.7 * x5 + 88 * (x6 - 0.933)

        pop.ObjV = np.hstack([f1, f2, f3, f4, f5, f6])

        pop.CV = np.hstack([
            x1 + x2 + x3 + x4 + x5 + x6 - 100
        ])


class MyProblem2(ea.Problem):
    def __init__(self):
        name = 'MyProblem2'
        M = 6
        maxormins = [-1] * M
        Dim = 6
        varTypes = [0] * Dim
        lb = [0] * 6
        ub = [100] * 6
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub)

    def aimFunc(self, pop):
        Vars = pop.Phen
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]
        x6 = Vars[:, [5]]

        f1 = 8.61 * x1 + 88 * (x1 - 1.84) - 2548.29
        f2 = 11.73 * x2 + 88 * (x2 - 5.12) - 710.26
        f3 = 16.29 * x3 + 88 * (x3 - 0.335) - 201.39
        f4 = 13.41 * x4 + 88 * (x4 - 1.62) - 516.73

        f5 = (790 - 0.8 * 88) * x5 * 0.5
        f6 = (790 - 0.8 * 88) * x6 * 0.5

        pop.ObjV = np.hstack([f1, f2, f3, f4, f5, f6])

        pop.CV = np.hstack([
            x1 + x2 + x3 + x4 - 100,
            x5 + x6 - x1 - x2 - x3 - x4
        ])


problem1 = MyProblem1()
problem2 = MyProblem2()

Encoding = 'RI'
NIND = 100

Field1 = ea.crtfld(Encoding, problem1.varTypes, problem1.ranges, problem1.borders)
population = ea.Population(Encoding, Field1, NIND)
my1 = ea.moea_NSGA2_templet(problem1, population)

Field = ea.crtfld(Encoding, problem2.varTypes, problem2.ranges, problem2.borders)
population = ea.Population(Encoding, Field, NIND)
my2 = ea.moea_NSGA2_templet(problem2, population)

my1.MAXGEN = 1000
my2.MAXGEN = 1000
my1.mutOper.pm = 0.2
my2.mutOper.pm = 0.2
my1.recOper.XOVR = 0.7
my2.recOper.XOVR = 0.7
my1.logTras = 1
my2.logTras = 0
my1.verbose = True
my2.verbose = True
my1.drawing = 1
my2.drawing = 0


#[Best1, population1] = my1.run()
#Best1.save('/home/liyuan/1_temp')
[Best2, population2] = my2.run()
Best2.save('/home/liyuan/1_temp')
