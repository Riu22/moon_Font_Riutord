megas = input("por favor introduce el numero de megas quequieras pasar a gigas: ")
megas_int = int(megas)
resultado = megas_int / 2**10
resultado_redondo = int(round(resultado))
print(resultado_redondo)

