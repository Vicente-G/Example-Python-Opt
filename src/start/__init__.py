from os import path, remove

import pyomo.environ as pyo
from amplpy import modules
from werkzeug.datastructures import FileStorage

from .model import model


def main(data: FileStorage) -> dict[str, str | dict[str, float]]:
    filename = path.join("/".join(__file__.split("/")[:-1]), "temp.dat")
    with open(filename, "w") as file:
        file.write(data.read().decode("utf-8"))
    final_result = {}
    solver = pyo.SolverFactory(modules.find("highs"))
    instance = model.create_instance(filename)
    result = solver.solve(instance)

    final_result["status"] = result.solver.status
    final_result["condition"] = result.solver.termination_condition
    final_result["result"] = {
        "time": result.solver.time,
        "objective": pyo.value(instance.OBJ),
    }
    for v in instance.component_data_objects(pyo.Var, active=True):
        final_result["result"][str(v)] = v.value
    remove(filename)
    return final_result
