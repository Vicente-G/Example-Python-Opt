import pyomo.environ as pyo

model = pyo.AbstractModel()
model.I = pyo.Set()
model.J = pyo.Set()
model.a = pyo.Param(model.I, model.J)
model.b = pyo.Param(model.I)
model.c = pyo.Param(model.J)
model.x = pyo.Var(model.J, domain=pyo.NonNegativeReals)

objective = lambda model: pyo.summation(model.c, model.x)
model.OBJ = pyo.Objective(sense=pyo.minimize, rule=objective)

cons1 = lambda m, i: sum(m.a[i, j] * m.x[j] for j in m.J) >= m.b[i]
model.cons1 = pyo.Constraint(model.I, rule=cons1)
