import sympy as sp

# Define symbols for molecular formula components and measurements
a, b, c, d = sp.symbols('a b c d', integer=True, positive=True)
MW = sp.symbols('MW', positive=True) # Molecular weight of CaHbOcNd
C_atom_mass = 12.011                 # Atomic weight of Carbon (g/mol)
H_atom_mass = 1.008                  # Atomic weight of Hydrogen (g/mol)
O_atom_mass = 15.999                 # Atomic weight of Oxygen (g/mol)
N_atom_mass = 14.007                 # Atomic weight of Nitrogen (g/mol)

# Given problem parameters
given_mw = 187.0                     # Total molecular weight (g/mol)
measured_toc = 360.0                 # Measured TOC in mg/L
solution_conc = 935.0                # Concentration of compound in mg/L

# Step 1: Define the theoretical mass fraction of Carbon (TOC fraction) in the compound
# Total mass of carbon per mole = a * C_atom_mass
# Molecular Weight MW = a*C_atom_mass + b*H_atom_mass + c*O_atom_mass + d*N_atom_mass
mass_fraction_C = (a * C_atom_mass) / MW

# Step 2: Derive theoretical TOC contribution per unit mass of compound concentration (mg/L)
# TOC_theoretical = Concentration * mass_fraction_C
TOC_theo_expr = solution_conc * mass_fraction_C

# Step 3: Use the empirical data ratio to solve for stoichiometric coefficient 'a'
# The ratio of measured TOC to solution concentration gives the experimental mass fraction of carbon
experimental_C_fraction = measured_toc / solution_conc

# Equating theoretical fraction to experimental fraction and solving for 'a'
# a * C_atom_mass / MW = experimental_C_fraction
formula_a = (experimental_C_fraction * MW) / C_atom_mass
calculated_a = formula_a.subs(MW, given_mw)

print(f"Formula derivation for carbon atom coefficient a:")
print(f"a = (Measured_TOC / Concentration) * (MW / Atomic_Mass_C)")
print(f"Calculated stoichiometric coefficient a = {float(calculated_a):.2f}")
print(f"Rounded integer value: {round(float(calculated_a))}")
