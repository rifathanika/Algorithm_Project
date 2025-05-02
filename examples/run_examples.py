from iot_uncertainty.sat.constraint_solver import ConstraintSolver
from iot_uncertainty.prob.probability_model import ProbabilityModel

# SAT Part: Temperature and humidity constraints
solver = ConstraintSolver()
# Example: [temperature between 25-26], [humidity between 55-65]
# Let's assume literals: x1 for temp in range, x2 for humidity in range
solver.encode_constraints([[1], [2]])  # Both must be true

result = solver.is_satisfiable()
print("SATISFIABLE" if result else "UNSATISFIABLE")

# Probability Part
temp_model = ProbabilityModel(mean=25.5, std=1.0)
humidity_model = ProbabilityModel(mean=60.0, std=5.0)

temp_prob = temp_model.probability_within_range((25, 26))
humidity_prob = humidity_model.probability_within_range((55, 65))

print(f"Probability temperature in [25, 26]: {temp_prob:.2f}")
print(f"Probability humidity in [55, 65]: {humidity_prob:.2f}")
