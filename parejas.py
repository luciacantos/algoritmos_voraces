def cambios_minimos(row):
    cambios = 0
    index = 0

    while index < len(row) - 1:
        estado_actual = row[index]
        if estado_actual % 2 == 0:
            estado_esperado = estado_actual + 1
        else:
            estado_esperado = estado_actual - 1

        pareja_index = row.index(estado_esperado)

        
