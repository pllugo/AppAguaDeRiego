#!/usr/bin/env python
'''
Impactos Ambientales
---------------------------
Autor: Pedro Luis Lugo Garcia
Version: 1.0
 
Descripcion:
Programa creado para realizar los cálculos del ODP.
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pedro.lugo@unc.edu.ar"
__version__ = "1.0"


import math


def validarNumero(numero):
    try:
        if len(numero) == 0:
            return False
        else:
            if isinstance(numero, str) == False:
                return False
            else:
                return True
    except ValueError:
        return False

def validaDatos(nombre, sodio, calcio, magnesio, bicarbonato, salinidadCe):
    
    if (isinstance(nombre, str) == False or len(nombre) == 0):
        return "El compuesto no puede estar vacio o nulo"
    if validarNumero(sodio) == False or float(sodio) <= 0:
        return "El Sodio no puede estar vacio, nulo, negativo o letras"
    if validarNumero(calcio) == False or float(calcio) <= 0:
        return "El Calcio no puede estar vacio, nulo, negativo o letras"
    if validarNumero(magnesio) == False or float(magnesio) <= 0:
        return "El Magnesio puede estar vacio, nulo, negativo o letras"
    if validarNumero(bicarbonato) == False or float(bicarbonato) <= 0:
        return "El Bicarbonato HCO3- no puede estar vacio, nulo, negativo o letras"
    if validarNumero(salinidadCe) == False or float(salinidadCe) <= 0:
        return "La salinidad no puede estar vacio, nulo, negativo o letras"



    