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

def validaAlc(nombre, volumenMuestra, concentracionAcidoSulfurico, volumenFenolftaleina, volumenDeNaranjaDeMetilo):
    
    if (isinstance(nombre, str) == False or len(nombre) == 0):
        return "El compuesto no puede estar vacio o nulo"
    if validarNumero(concentracionAcidoSulfurico) == False or float(concentracionAcidoSulfurico) <= 0:
        return "La concentración de H2SO4 no puede estar vacio, nulo, negativo o letras"
    if validarNumero(volumenFenolftaleina) == False or float(volumenFenolftaleina) < 0:
        return "El volumen de Fenolftaleina no puede ser negativo o letras"
    if validarNumero(volumenDeNaranjaDeMetilo) == False or float(volumenDeNaranjaDeMetilo) < 0:
        return "El volumen de Naranja de Metilo no puede ser negativo o letras"
    if validarNumero(volumenMuestra) == False or float(volumenMuestra) <= 0:
        return "El volumen de Muestra no puede ser negativo o letras"
    
def causasAlcalinidad(volumenMuestra, concentracionAcido, volumenFenolftaleina, volumenDeNaranjaDeMetilo):
    alcalinidadF = (volumenFenolftaleina * concentracionAcido / volumenMuestra) * 50 * 1000
    alcalinidadM = (((volumenDeNaranjaDeMetilo) * concentracionAcido )/ volumenMuestra) * 50 * 1000
    alcalinidadTotal = alcalinidadF + alcalinidadM
    if alcalinidadF == alcalinidadTotal:
        alcalinidadOh = alcalinidadF
        alcalinidadCo3 = 0
        alcalinidadHco3 = 0
    else:
        if alcalinidadF > alcalinidadTotal / 2:
            alcalinidadOh = 2 * alcalinidadF - alcalinidadTotal
            alcalinidadCo3 = 2 * (alcalinidadTotal - alcalinidadF)
            alcalinidadHco3 = 0
        else:
            if alcalinidadF == alcalinidadTotal / 2:
                alcalinidadCo3 = 2 * alcalinidadF
                alcalinidadHco3 = 0
                alcalinidadOh = 0
            else:
                if alcalinidadF < alcalinidadTotal / 2:
                    alcalinidadCo3 = 2 * alcalinidadF
                    alcalinidadHco3 = alcalinidadTotal - 2 * alcalinidadF
                    alcalinidadOh = 0
                else:
                    if alcalinidadF == 0:
                        alcalinidadHco3 = alcalinidadTotal
                        alcalinidadOh = 0
                        alcalinidadCo3 = 0
    return round(alcalinidadOh, 2), round(alcalinidadCo3, 2), round(alcalinidadHco3, 2), round(alcalinidadF, 2), round(alcalinidadM, 2), round(alcalinidadTotal, 2)