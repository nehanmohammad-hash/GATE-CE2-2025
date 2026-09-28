import sympy as sp

x = sp.symbols('x')
f = x**3 - (15/2)*x**2 + 18*x + 20
df = sp.diff(f, x)
ddf = sp.diff(df, x)

critical_points = sp.solve(df, x)
for pt in critical_points:
    val = ddf.subs(x, pt)
    print(f"x = {pt}, Second Derivative = {val} ({'Local Min' if val > 0 else 'Local Max'})")
