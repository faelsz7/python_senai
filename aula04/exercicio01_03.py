import cmath

# Coeficientes da equação quadrática
a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

# Calcula o discriminante
delta = b**2 - 4*a*c

print(f"O discriminante (delta) é igual a {delta:.2f}")