for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}" .format(i, i **2, i ** 3)) # default right aligned

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:5}" .format(i, i **2, i ** 3)) # right aligned

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<5}" .format(i, i **2, i ** 3)) # left aligned

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^5}" .format(i, i **2, i ** 3)) # center aligned

print()

print("Pi es approximately {0:12}".format(22/7))  # puntos flotantes por defecto
print("Pi es approximately {0:12f}".format(22/7)) # puntos flotantes
print("Pi es approximately {0:12.50f}".format(22/7)) # 50 decimales
print("Pi es approximately {0:52.50f}".format(22/7))  # 50 decimales, ancho 52
print("Pi es approximately {0:62.50f}".format(22/7))  # 50 decimales, ancho 62
print("Pi es approximately {0:72.50f}".format(22/7))  # 50 decimales, ancho 72

print()

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}" .format(i, i **2, i ** 3)) # sin indices, lo que significa que se usan en orden de los valores pasados a format()