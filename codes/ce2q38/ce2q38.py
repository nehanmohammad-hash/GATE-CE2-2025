# By Nehan mohammad
# 05-October-26, Monday, question no: cantilever_deflection
import sympy as sp

# Define symbolic variables
M, L, EI, Delta, RB = sp.symbols('M L EI Delta RB', real=True, positive=True)

# 1. Deflection at support B due to the applied moment M
# (Standard cantilever deflection formula for an end moment)
delta_M = - (M * L**2) / (2 * EI)

# 2. Deflection at support B due to the upward redundant reaction RB
delta_R = (RB * L**3) / (3 * EI)

# 3. Compatibility equation: Total deflection equals the given settlement (-Delta)
compatibility_equation = sp.Eq(delta_M + delta_R, -Delta)

# 4. Solve for the unknown reaction RB
solution_rb = sp.solve(compatibility_equation, RB)

# Print the resulting symbolic expression
print("Derived expression for RB:")
sp.pprint(solution_rb[0])

