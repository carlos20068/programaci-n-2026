def tiene_mayuscula(texto):
    """Verifica si el texto tiene al menos una letra mayúscula."""
    for char in texto:
        if char.isupper():
            return True
    return False

def tiene_digito(texto):
    """Verifica si el texto tiene al menos un dígito."""
    for char in texto:
        if char.isdigit():
            return True
    return False

def tiene_especial(texto):
    """Verifica si el texto tiene al menos un carácter especial."""
    especiales = ['!', '@', '#', '$', '%']
    for char in texto:
        if char in especiales:
            return True
    return False

def tiene_secuencia(texto):
    """Verifica si el texto contiene 3 caracteres iguales seguidos."""
    for i in range(len(texto) - 2):
        if texto[i] == texto[i+1] == texto[i+2]:
            return True
    return False

def validar_password(password):
    """Valida si la contraseña cumple con todas las reglas."""
    if len(password) < 8:
        return False
    if not tiene_mayuscula(password):
        return False
    if not tiene_digito(password):
        return False
    if not tiene_especial(password):
        return False
    if tiene_secuencia(password):
        return False
    return True

def diagnosticar_password(password):
    """Diagnostica qué reglas no se cumplen en la contraseña."""
    errores = []
    if len(password) < 8:
        errores.append("La contraseña debe tener mínimo 8 caracteres.")
    if not tiene_mayuscula(password):
        errores.append("La contraseña debe tener al menos una letra mayúscula.")
    if not tiene_digito(password):
        errores.append("La contraseña debe tener al menos un dígito.")
    if not tiene_especial(password):
        errores.append("La contraseña debe tener al menos un carácter especial (!, @, #, $, %).")
    if tiene_secuencia(password):
        errores.append("La contraseña no puede contener 3 caracteres iguales seguidos.")
    
    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(f"- {error}")
    else:
        print("La contraseña es válida.")

                
# Ejemplo de uso
password = input("Ingresa una contraseña: ")
if validar_password(password):
    print("La contraseña es válida.")
else:
    diagnosticar_password(password)