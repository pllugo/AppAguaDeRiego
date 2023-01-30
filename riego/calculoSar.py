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

def calculo(sodio, magnesio, relacionBicarbonato, salinidad):
    
    matriz = [[0, 0.1, 0.2, 0.3, 0.5, 0.7, 1, 1.5, 2, 3, 4, 6, 8], 
    [0.05, 13.20, 13.61, 14.40, 14.79, 15.26, 15.91, 16.43, 17.28, 17.97, 19.07, 19.94],
    [0.10, 8.31, 8.57, 8.77, 9.07, 9.31, 9.62, 10.02, 10.35, 10.89, 11.32, 12.01, 12.56],
    [0.15, 6.34, 6.54, 6.69, 6.92, 7.11, 7.34, 7.65, 7.90, 8.31, 8.64, 9.17, 9.58],
    [0.20, 5.24, 5.40, 5.52, 5.71, 5.87, 6.06, 6.31, 6.52, 6.86, 7.13, 7.57, 7.91],
    [0.25, 4.51, 4.65, 4.76, 4.92, 5.06, 5.22, 5.44, 5.62, 5.91, 6.15, 6.52, 6.82],
    [0.30, 4, 4.12, 4.21, 4.36, 4.48, 4.62, 4.82, 4.98, 5.24, 5.44, 5.77, 6.04],
    [0.35, 3.61, 3.72, 3.80, 3.94, 4.04, 4.17, 4.35, 4.49, 4.72, 4.91, 5.21, 5.45],
    [0.4, 3.30, 3.40, 3.48, 3.60, 3.70, 3.82, 3.98, 4.11, 4.32, 4.49, 4.77, 4.98],
    [0.45, 3.05, 3.14, 3.22, 3.33, 3.42, 3.53, 3.68, 3.80, 4, 4.15, 4.41, 4.61],
    [0.5, 2.84, 2.93, 3, 3.1, 3.19, 3.29, 3.43, 3.54, 3.72, 3.87, 4.11, 4.30],
    [0.75, 2.17, 2.24, 2.29, 2.37, 2.43, 2.51, 2.62, 2.70, 2.84, 2.95, 3.14, 3.28],
    [1, 1.79, 1.85, 1.89, 1.96, 2.01, 2.09, 2.16, 2.23, 2.35, 2.44, 2.59, 2.71],
    [1.25, 1.54, 1.59, 1.63, 1.68, 1.73, 1.78, 1.86, 1.92, 2.02, 2.10, 2.23, 2.33],
    [1.50, 1.37, 1.41, 1.44, 1.49, 1.53, 1.58, 1.65, 1.70, 1.79, 1.86, 1.97, 2.07],
    [1.75, 1.23, 1.27, 1.30, 1.35, 1.38, 1.43, 1.49, 1.54, 1.62, 1.68, 1.78, 1.86],
    [2, 1.13, 1.16, 1.19, 1.23, 1.26, 1.31, 1.36, 1.40, 1.48, 1.54, 1.63, 1.70],
    [2.25, 1.04, 1.08, 1.10, 1.14, 1.17, 1.21, 1.26, 1.30, 1.37, 1.42, 1.51, 1.58],
    [2.50, 0.97, 1, 1.02, 1.06, 1.09, 1.12, 1.17, 1.21, 1.27, 1.32, 1.40, 1.47],
    [3, 0.85, 0.89, 0.91, 0.94, 0.96, 1, 1.04, 1.07, 1.13, 1.17, 1.24, 1.30],
    [3.50, 0.78, 0.80, 0.82, 0.85, 0.87, 0.9, 0.94, 0.97, 1.02, 1.06, 1.12, 1.17],
    [4, 0.71, 0.73, 0.75, 0.78, 0.80, 0.82, 0.86, 0.88, 0.93, 0.97, 1.03, 1.07],
    [4.50, 0.66, 0.68, 0.69, 0.72, 0.74, 0.76, 0.79, 0.82, 0.86, 0.90, 0.95, 0.99],
    [5, 0.61, 0.63, 0.65, 0.67, 0.69, 0.71, 0.74, 0.76, 0.80, 0.83, 0.88, 0.93],
    [7, 0.49, 0.50, 0.52, 0.53, 0.55, 0.57, 0.59, 0.61, 0.64, 0.67, 0.71, 0.74],
    [10, 0.39, 0.40, 0.41, 0.42, 0.43, 0.45, 0.47, 0.48, 0.51, 0.53, 0.56, 0.58],
    [20, 0.24, 0.25, 0.26, 0.26, 0.27, 0.28, 0.29, 0.30, 0.32, 0.33, 0.35, 0.371],
    [30, 0.18, 0.19, 0.20, 0.20, 0.21, 0.21,  0.22, 0.23, 0.24, 0.25, 0.27, 0.28]]
    
   
    

    for i in range(len(matriz[0])):
        if salinidad < matriz[0][i]:
            for j in range(len(matriz)):
               
                if relacionBicarbonato < matriz[j][0]:
                    x2 = matriz[j][0]
                    x1 = matriz[j-1][0]
                    x1prima2 = matriz[0][i]
                    x1prima = matriz[0][i-1]
                    y2 = matriz[j][i]
                    y1 = matriz[j-1][i]
                    y1prima = matriz[j-1][i-1]
                    y2prima = matriz[j][i-1]
                    pendientePrima = (y1 - y1prima) / (x1prima2 - x1prima)
                    intercepto = y1 - (pendientePrima * x1prima2)
                    ybuscada1 = pendientePrima*salinidad + intercepto
                    
                    pendientePrima2 = (y2 - y2prima) / (x1prima2 - x1prima)
                    intercepto = y2 - (pendientePrima2 * x1prima2)
                    ybuscada2 = pendientePrima2*salinidad + intercepto
                    
                    pendiente = (ybuscada2 - ybuscada1) / (x2 - x1)
                    
                    interceptoResultado = ybuscada1 - (pendiente*x1)
                    
                    ybuscada3 = pendiente*relacionBicarbonato + interceptoResultado

                    return round((sodio / (math.sqrt((ybuscada3 + magnesio)/2))), 2)
                    
                else:
                    if relacionBicarbonato == matriz[j][0]:
                        x1 = matriz[0][i]
                        x2 = matriz[0][i-1]
                        y1 = matriz[j][i]
                        y2 = matriz[j][i-1]
                        pendiente = (y2 - y1) / (x2 - x1)
                        intercepto = y2 - pendiente * x2
                        ysalida = pendiente * salinidad + intercepto
                        return round((sodio / (math.sqrt(( ysalida + magnesio)/2))), 2)
                        break
                    else:
                        continue
            break
        else:
            if salinidad == matriz[0][i]:
                
                for j in range(len(matriz)):
                    
                    if relacionBicarbonato < matriz[j][0]:
                        x1 = matriz[j-1][0]
                        y1 = matriz[j-1][i]
                        x2 = matriz[j][0]
                        y2 = matriz[j][i]
                        
                        pendiente = (y2 - y1) / (x2 - x1)
                        intercepto = y2 -pendiente*x2
                        ysalida = pendiente*relacionBicarbonato + intercepto
                        return round((sodio / (math.sqrt(( ysalida + magnesio)/2))), 2)
                        
                    else:
                        if relacionBicarbonato == matriz[j][0]:
                            x1 = matriz[0][i]
                            x2 = matriz[0][i-1]
                            y1 = matriz[j][i]
                            y2 = matriz[j][i-1]
                            pendiente = (y2 - y1) / (x2 - x1)
                            intercepto = y2 - pendiente * x2
                            ysalida = pendiente * salinidad + intercepto
                            return round((sodio / (math.sqrt(( ysalida + magnesio)/2))), 2)
                        else:
                            continue
                break
            else:
                continue


def calculoSarNormal(sodio, calcio, magnesio):
    return round((sodio / (math.sqrt((calcio + magnesio)/2))), 2)


def riesgoSar(relacionSar, salinidadCe):    
    if relacionSar > 0 and relacionSar < 3:
        if salinidadCe > 0.7:
            resultado = 0
        else:
            if salinidadCe > 0.7 and salinidadCe < 0.2:
                resultado = 1
            else:
                resultado = 2
    else:
        if relacionSar > 3 and relacionSar < 6:
            if salinidadCe > 1.2:
                resultado = 0
                
            else:
                if salinidadCe > 0.3 and salinidadCe < 1.2:
                    resultado = 1
                    
                else:
                    resultado = 2
        else:
            if relacionSar > 6 and relacionSar < 12:
                if salinidadCe > 1.9:
                    resultado = 0
                else:
                    if salinidadCe > 0.5 and salinidadCe < 1.9:
                        resultado = 1
                    else:
                        resultado = 2
            else:
                if relacionSar > 12 and relacionSar < 20:
                    if salinidadCe > 2.9:
                        resultado = 0
                    else:
                        if salinidadCe > 1.3 and salinidadCe < 2.9:
                            resultado = 1
                        else:
                            resultado = 2
                else:
                    if relacionSar > 20 and relacionSar < 40:
                        if salinidadCe > 5:
                            resultado = 0
                        else:
                            if salinidadCe > 2.9 and salinidadCe < 5:
                                resultado = 1
                            else:
                                resultado = 2
    return resultado
        

