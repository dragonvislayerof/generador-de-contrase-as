import random

caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

largo = int(input("cuantos caracteres quieres que tenga tu contraseña:"))

contrasena = ""

for i in range(largo):
    contrasena += random.choice(caracteres)
print(contrasena)
