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

def valida(nombre, conductividadAgua, solidosTotalesDisueltos, ras, sodio, bicarbonato, cloruro, boro, manganeso, hierro, sulfuroDeHidrogeno):
    
    if (isinstance(nombre, str) == False or len(nombre) == 0):
        return "El compuesto no puede estar vacio o nulo"
    if validarNumero(conductividadAgua) == False or float(conductividadAgua) < 0:
        return "La Conductividad Electrica del agua no puede estar vacio, nulo, negativo o letras"
    if validarNumero(solidosTotalesDisueltos) == False or float(solidosTotalesDisueltos) < 0:
        return "Los SDT no puede estar vacio, nulo, negativo o letras"
    if validarNumero(ras) == False or float(ras) < 0:
        return "El RAS no puede estar vacio, nulo, negativo o letras"
    if validarNumero(sodio) == False or float(sodio) < 0:
        return "El Sodio no puede estar vacio, nulo, negativo o letras"
    if validarNumero(bicarbonato) == False or float(bicarbonato) < 0:
        return "El Bicarbonato no puede estar vacio, nulo, negativo o letras"
    if validarNumero(cloruro) == False or float(cloruro) < 0:
        return "El Cloruro no puede estar vacio, nulo, negativo o letras"
    if validarNumero(boro) == False or float(boro) <= 0:
        return "El Boro no puede estar vacio, nulo, negativo o letras"
    if validarNumero(manganeso) == False or float(manganeso) < 0:
        return "El Manganeso no puede estar vacio, nulo, negativo o letras"
    if validarNumero(hierro) == False or float(hierro) < 0:
        return "El Hierro no puede estar vacio, nulo, negativo o letras"
    if validarNumero(sulfuroDeHidrogeno) == False or float(sulfuroDeHidrogeno) < 0:
        return "El H2S no puede estar vacio, nulo, negativo o letras"
    


    