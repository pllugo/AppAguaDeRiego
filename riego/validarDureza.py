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

def valiDureza(nombre, calcio, magnesio, bicarbonato, carbonato, alcalinidadTotalIngresado):
    if (isinstance(nombre, str) == False or len(nombre) == 0):
        return "El nombre de la muestra no puede estar vacio o nulo"
    if validarNumero(calcio) == False or float(calcio) < 0:
        return "El Calcio no puede estar vacio, nulo, negativo o letras"
    if validarNumero(magnesio) == False or float(magnesio) < 0:
        return "El Magnesio no puede estar vacio, nulo, negativo o letras"
    if validarNumero(bicarbonato) == False or float(bicarbonato) < 0:
        return "El Bicarbonato no puede estar vacio, nulo, negativo o letras"
    if validarNumero(carbonato) == False or float(carbonato) < 0:
        return "El Carbonato no puede estar vacio, nulo, negativo o letras"
    if validarNumero(alcalinidadTotalIngresado) == False or float(alcalinidadTotalIngresado) < 0:
        return "La alcalinidad total no puede estar vacio, nulo, negativo o letras"
    


def analisisDureza(durezaTotal, alcalinidadTotal):
    if durezaTotal >= alcalinidadTotal:
        durezaCarbonacea = alcalinidadTotal
        durezaNoCarbonacea = durezaTotal - alcalinidadTotal
    else:
        durezaCarbonacea = durezaTotal
        durezaNoCarbonacea = 0
    return durezaCarbonacea, durezaNoCarbonacea
    

def calculoDureza(calcio, magnesio, bicarbonato, carbonato, alcalinidadTotal):
    durezaTotal = (calcio / 20 + magnesio / 12.2) * 50
    if bicarbonato == 0 and carbonato == 0 and alcalinidadTotal != 0:
       durezaCarbonacea, durezaNoCarbonacea = analisisDureza(durezaTotal, alcalinidadTotal)
    else:
        if alcalinidadTotal == 0:
            alcalinidadHco3 = (bicarbonato * 50) / 61
            alcalinidadCo3 = (carbonato * 50) / 30
            alcalinidadTotal = alcalinidadHco3 + alcalinidadCo3
            durezaCarbonacea, durezaNoCarbonacea = analisisDureza(durezaTotal, alcalinidadTotal)
    return round(durezaTotal, 2), round(durezaCarbonacea, 2), round(durezaNoCarbonacea, 2), round(alcalinidadTotal, 2)

        
