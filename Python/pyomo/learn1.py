import numpy as np
import pandas as pd
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = ConcreteModel()
I = 9
J = 3
p = 2
d_ij = [[5, 2, 5], [2, 5, 6], [0, 7, 8], [7, 0, 3], [
    6, 1, 2], [5, 4, 5], [12, 5, 4], [8, 3, 0], [8, 7, 6]]

print(d_ij)

model.i = range(I)
model.j = range(J)
model.x = Var(model.i, model.j, within=Binary)
model.z = Var(model.j, within=Binary)


def obj(model):
    return sum(d_ij[i][j]*model.x[i, j] for i in model.i for j in model.j)


model.obj = Objective(rule=obj, sense=minimize)


def cnsd1(model):
    return sum(model.z[j] for j in model.j) == p


model.cnsd1 = Constraint(rule=cnsd1)


def cnsd2(model):
    return model.x[i, j] <= model.z[j]


model.cnsd2 = Constraint(rule=cnsd2)
