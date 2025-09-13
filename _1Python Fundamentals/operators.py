a = 12
b = 3

print(a + b)    #15
print(a - b)    #9
print(a * b)    #36
print(a / b)    #4.0
print(a // b)   #4 integer division, redondeado hacia abajo hacia menos infinito
print(a % b)    #0 modulo: el resto después de la división de números enteros

print()

print(a + b / 3 - 4 * 12)   # precedencia de operadores es *, /, //, % antes que +, -
print(a+(b / 3) - (4 * 12))   # igual que la línea anterior
print((((a+b)/3)-4)*12)   # paréntesis para cambiar la precedencia de operadores
print(((a+b)/3-4)*12)   # igual que la línea anterior

c = a+b
d= c/3
e = d-4
print(e*12)   # igual que la línea anterior, pero usando variables intermedias

# PEMDAS es una mnemotecnia para recordar la precedencia de operadores:
# Paréntesis (Parentheses) -> Exponentes (Exponents) -> Multiplicación y División (Multiplication and Division)
# -> Adición y Sustracción (Addition and Subtraction)

# BEDMAS es otra mnemotecnia que algunas personas usan:
# Paréntesis (Brackets) -> Exponentes (Exponents) -> División y Multiplicación (Division and Multiplication)
# -> Adición y Sustracción (Addition and Subtraction)

# BODMAS es otra mnemotecnia que algunas personas usan:
# Paréntesis (Brackets) -> Orden (Order, que se refiere a exponentes) -> División y Multiplicación (Division and Multiplication)    
# -> Adición y Sustracción (Addition and Subtraction)

# BIDMAS es otra mnemotecnia que algunas personas usan:
# Paréntesis (Brackets) -> Índices (Indices, que se refiere a exponent
# -> División y Multiplicación (Division and Multiplication) -> Adición y Sustracción (Addition and Subtraction)

# Todos estos acrónimos representan la misma idea general de la precedencia de operadores en matemáticas y programación.
