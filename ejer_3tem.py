def celsius_a_fahrenheit(c):
    """Convierte Celsius a Fahrenheit."""
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius."""
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    """Convierte Celsius a Kelvin."""
    return c + 273.15

def convertir(valor, origen, destino):
    """
    Función principal que convierte temperatura entre escalas.
    origen/destino pueden ser 'C', 'F' o 'K'.
    """
    if origen == destino:
        return valor
    
    if origen == 'C':
        if destino == 'F':
            return celsius_a_fahrenheit(valor)
        elif destino == 'K':
            return celsius_a_kelvin(valor)
    elif origen == 'F':
        if destino == 'C':
            return fahrenheit_a_celsius(valor)
        elif destino == 'K':
            return celsius_a_kelvin(fahrenheit_a_celsius(valor))
    elif origen == 'K':
        c = valor - 273.15
        if destino == 'C':
            return c
        elif destino == 'F':
            return celsius_a_fahrenheit(c)
    return None

# Bonus: Conversión a Rankine
def fahrenheit_a_rankine(f):
    """Convierte Fahrenheit a Rankine."""
    return f + 459.67

def convertir_con_rankine(valor, origen, destino):
    if origen == 'R':
        f = valor - 459.67
        return convertir(f, 'F', destino)
    elif destino == 'R':
        f = convertir(valor, origen, 'F')
        return fahrenheit_a_rankine(f)
    else:
        return convertir(valor, origen, destino)

# Ejemplos de uso
if __name__ == "__main__":
    print(convertir(30, 'C', 'F'))  # 86.0
    print(convertir(86, 'F', 'K'))  # 303.15
    print(convertir_con_rankine(500, 'R', 'C'))  # 4.627777777777756