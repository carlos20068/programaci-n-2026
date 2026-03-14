"""Funciones matemáticas útiles.

Este módulo puede usarse como una pequeña biblioteca de funciones
reutilizables para diferentes programas escolares.
"""

import math


def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio.

    Parámetros:
        radio (float): El radio del círculo (debe ser >= 0).

    Retorna:
        float: El área del círculo.

    Ejemplo:
        >>> area_circulo(2)
        12.566370614359172
    """

    if radio < 0:
        raise ValueError("El radio no puede ser negativo")

    return math.pi * radio ** 2
