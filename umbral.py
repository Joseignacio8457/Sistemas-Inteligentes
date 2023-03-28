def encontrar_umbral_and():
    umbral = 0.5
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    salidas_esperadas = [0, 0, 0, 1]

    while True:
        errores = 0
        for i in range(len(entradas)):
            entrada = entradas[i]
            salida_esperada = salidas_esperadas[i]
            salida_real = 1 if sum(entrada) > umbral else 0
            if salida_real != salida_esperada:
                errores += 1
        if errores == 0:
            break
        umbral += 0.1

    return umbral


umbral_and = encontrar_umbral_and()
print("El umbral de la compuerta AND es:", umbral_and)


def encontrar_umbral_or():
    umbral = 0.5
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    salidas_esperadas = [0, 1, 1, 1]
    while True:
        errores = 0
        for i in range(len(entradas)):
            entrada = entradas[i]
            salida_esperada = salidas_esperadas[i]
            salida_real = 1 if sum(entrada) > umbral else 0
            if salida_real != salida_esperada:
                errores += 1
        if errores == 0:
            break
        umbral += 0.1
    return umbral


umbral_or = encontrar_umbral_or()
print("El umbral de la compuerta OR es:", umbral_or)
