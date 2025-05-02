from pysat.formula import CNF
from pysat.solvers import Solver

class ConstraintSolver:
    """
    Encodes sensor constraints as SAT clauses and checks satisfiability.
    """
    def __init__(self):
        self.cnf = CNF()

    def encode_constraints(self, sensor_constraints):
        """
        sensor_constraints: list of lists representing clauses, e.g., [[1, -2], [-1, 3]]
        """
        for clause in sensor_constraints:
            self.cnf.append(clause)

    def is_satisfiable(self):
        with Solver(name='g4') as solver:
            solver.append_formula(self.cnf)
            return solver.solve()
