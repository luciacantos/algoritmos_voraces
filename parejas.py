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

        if abs(pareja_index - index) > 1:
            row[index + 1], row[pareja_index] = row[pareja_index], row[index + 1]
            cambios += 1

        index += 2

    return cambios

# ejemplo
row = [0,2,1,3]
print("[0,2,1,3]")
print(cambios_minimos(row))


