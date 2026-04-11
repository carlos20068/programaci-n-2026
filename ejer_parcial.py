def calcular_billetes(monto):
    if monto % 20 != 0:
        print("Error: El monto no es múltiplo de 20.")
        return None

    billetes = [200, 100, 50, 20]
    resultado = []

    for billete in billetes:
        cantidad = monto // billete
        monto %= billete
        if cantidad > 0:
            resultado.append(f"{cantidad} x Q{billete}")

    return ", ".join(resultado)

# Ejemplo de uso
print(calcular_billetes(370))  # Salida: 1 x Q200, 1 x Q100, 1 x Q50, 1 x Q20
def calcular_billetes_bonus(monto):
    if monto % 5 != 0:
        print("Error: El monto no es múltiplo de 5.")
        return None

    billetes = [200, 100, 50, 20, 10, 5]
    resultado = []

    for billete in billetes:
        cantidad = monto // billete
        monto %= billete
        if cantidad > 0:
            resultado.append(f"{cantidad} x Q{billete}")

    return ", ".join(resultado)

# Ejemplo de uso
print(calcular_billetes_bonus(375))  # Maneja múltiplos de 5