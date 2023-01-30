from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .validarAgua import valida
from .validaSar import validaDatos
from .validarAlcalinidad import *
from .calculoSar import *
from .validarDureza import valiDureza, calculoDureza
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px
import io
import base64
import matplotlib
matplotlib.use('Agg')   # For multi thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import matplotlib.transforms as mtransforms
from plotly.offline import plot
from plotly.graph_objs import Scatter
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def listaAgua(request):
    listadoCaracteristicas = Agua.objects.all()

    return render(request, 'caracterizacion/lista.html', {'listadoCaracteristicas': listadoCaracteristicas})


def edicionAgua(request, id):
    muestra = Agua.objects.get(id=id)
    return render(request, 'caracterizacion/editar.html', {'muestra': muestra})


def editarAgua(request):
    id = int(request.POST['id'])
    muestra = Agua.objects.get(id=id)
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        conductividadAgua = str(request.POST['conductividadAgua'])
        solidosTotalesDisueltos = str(request.POST['solidosTotalesDisueltos'])
        ras = str(request.POST['ras'])
        sodio = str(request.POST['sodio'])
        bicarbonato = str(request.POST['bicarbonato'])
        cloruro = str(request.POST['cloruro'])
        boro = str(request.POST['boro'])
        manganeso = str(request.POST['manganeso'])
        hierro = str(request.POST['hierro'])
        sulfuroDeHidrogeno = str(request.POST['sulfuroDeHidrogeno'])
        
        respuesta = valida(nombre, conductividadAgua, solidosTotalesDisueltos, ras, sodio, bicarbonato, cloruro, boro, manganeso, hierro, sulfuroDeHidrogeno)

        try:
            if respuesta == None:
                muestra.nombre = nombre
                muestra.conductividadAgua = conductividadAgua
                muestra.solidosTotalesDisueltos = solidosTotalesDisueltos
                muestra.ras = ras
                muestra.sodio = sodio
                muestra.bicarbonato = bicarbonato
                muestra.cloruro = cloruro
                muestra.boro = boro
                muestra.manganeso = manganeso
                muestra.hierro = hierro
                muestra.sulfuroDeHidrogeno = sulfuroDeHidrogeno
                muestra.save()
                messages.success(request, "Success!! You have successfully edited your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'caracterizacion/editar.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'caracterizacion/editar.html')

    else:

        return render(request, 'caracterizacion/editar.html')

def crearAgua(request):
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        conductividadAgua = str(request.POST['conductividadAgua'])
        solidosTotalesDisueltos = str(request.POST['solidosTotalesDisueltos'])
        ras = str(request.POST['ras'])
        sodio = str(request.POST['sodio'])
        bicarbonato = str(request.POST['bicarbonato'])
        cloruro = str(request.POST['cloruro'])
        boro = str(request.POST['boro'])
        manganeso = str(request.POST['manganeso'])
        hierro = str(request.POST['hierro'])
        sulfuroDeHidrogeno = str(request.POST['sulfuroDeHidrogeno'])
        
        respuesta = valida(nombre, conductividadAgua, solidosTotalesDisueltos, ras, sodio, bicarbonato, cloruro, boro, manganeso, hierro, sulfuroDeHidrogeno)

        try:
            if respuesta == None:
                Agua(nombre = nombre, conductividadAgua = conductividadAgua, solidosTotalesDisueltos = solidosTotalesDisueltos, ras = ras, sodio = sodio, bicarbonato = bicarbonato, cloruro= cloruro, boro = boro, manganeso = manganeso, hierro = hierro, sulfuroDeHidrogeno = sulfuroDeHidrogeno).save()
                
                messages.success(request, "Success!! You have successfully registered your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'caracterizacion/crear.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'caracterizacion/crear.html')

    else:

        return render(request, 'caracterizacion/crear.html')

def eliminarAgua(request, id):
    muestra = Agua.objects.get(id=id)
    muestra.delete()
    listadoCaracteristicas = Agua.objects.all()
    return render(request, 'caracteristizacion/lista.html', {'listadoCaracteristicas': listadoCaracteristicas})

def listaSar(request):
    listadoSars = Sar.objects.all()

    return render(request, 'sar/lista.html', {'listadoSars': listadoSars})


def crearSar(request):
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        sodio = str(request.POST['sodio'])
        calcio = str(request.POST['calcio'])
        magnesio = str(request.POST['magnesio'])
        bicarbonato = str(request.POST['bicarbonato'])
        salinidadCe = str(request.POST['salinidadCe'])
        respuesta = validaDatos(nombre, sodio, calcio, magnesio, bicarbonato, salinidadCe)

        try:
            if respuesta == None:
                sarNormal = calculoSarNormal(float(sodio), float(calcio), float(magnesio))
               
                relacionSar = calculo(float(sodio), float(magnesio), float(bicarbonato)/float(calcio), float(salinidadCe))
                
                riesgo = riesgoSar(relacionSar, float(salinidadCe))
                
                Sar(nombre = nombre, sodio = sodio, calcio = calcio, magnesio = magnesio, bicarbonato = bicarbonato, salinidadCe = salinidadCe, sarNormal = sarNormal, relacionSar = relacionSar, riesgo = riesgo).save()
                
                messages.success(request, "Success!! You have successfully registered your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'sar/crear.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'sar/crear.html')

    else:

        return render(request, 'sar/crear.html')


def edicionSar(request, id):
    muestra = Sar.objects.get(id=id)
    return render(request, 'sar/editar.html', {'muestra': muestra})


def editarSar(request):
    id = int(request.POST['id'])
    muestra = Sar.objects.get(id=id)

    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        sodio = str(request.POST['sodio'])
        calcio = str(request.POST['calcio'])
        magnesio = str(request.POST['magnesio'])
        bicarbonato = str(request.POST['bicarbonato'])
        salinidadCe = str(request.POST['salinidadCe'])
        respuesta = validaDatos(nombre, sodio, calcio, magnesio, bicarbonato, salinidadCe)

        try:
            if respuesta == None:
                sarNormal = calculoSarNormal(float(sodio), float(calcio), float(magnesio))
                relacionSar = calculo(float(sodio), float(magnesio), float(bicarbonato)/float(calcio), float(salinidadCe))
                muestra.nombre = nombre
                muestra.sodio = sodio
                muestra.calcio = calcio
                muestra.magnesio = magnesio
                muestra.bicarbonato = bicarbonato
                muestra.salinidadCe = salinidadCe
                muestra.sarNormal = sarNormal
                muestra.relacionSar = relacionSar
                muestra.save()
                messages.success(request, "Success!! You have successfully edited your water sample")
                return redirect('/')
            else:
                messages.error(request, "Error, existen datos negativos")
                return render(request, 'sar/editar.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'sar/editar.html')

    else:

        return render(request, 'sar/editar.html')


def eliminarSar(request, id):
    muestra = Sar.objects.get(id=id)
    muestra.delete()
    listadoSars = Sar.objects.all()
    messages.success(request, "Success!! You have deleted your water sample")
    return render(request, 'sar/lista.html', {'listadoSars': listadoSars})


def displaySar(request):
    try:

        todoSar = Sar.objects.all().values()
        df = pd.DataFrame(todoSar)
        df1 = df['salinidadCe'].to_list()
        df2 = df['relacionSar'].to_list()
        df3 = df['nombre'].to_list()
        x = [0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4] 
        y = [0.55296, 1.87688, 3.2008, 4.52472, 5.84864, 7.17256, 8.49648, 9.8204, 11.14432, 12.46824, 13.79216, 15.11608, 16.44, 17.76392, 19.08784, 20.41176, 21.73568, 23.0596, 24.38352, 25.70744, 27.03136, 28.35528, 29.6792, 31.00312, 32.32704]

        
        salinidadCe = [0.1, 0.2, 0.2, 0.2, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.8, 0.85, 0.9, 0.95, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2]
        relacionSar = [0, 0, 1, 2, 5.6667, 6.5417, 7.4167, 8.2917, 9.1667, 9.743635, 11.09182, 11.541215, 11.99061, 12.440005, 12.8894, 14.68698, 16.48456, 18.28214, 20.07972, 21.8773, 23.67488, 25.47246, 27.27004, 29.06762, 30.8652, 32.66278]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=salinidadCe, y=relacionSar, showlegend=False,
                            line=dict(color='firebrick', width=4)))
        fig.add_trace(go.Scatter(x=x, y=y, showlegend=False, name='High 2014',
                            line=dict(color='firebrick', width=4)))
        fig.add_trace(go.Scatter(x=df1, y=df2, text = df3,
                        mode='markers', name="Samples", marker=dict(
                color='rgba(0, 0, 0, 0.8)',
                
                )))
        fig.update_xaxes(title_text='Electric conductivity or Salinity (dS/m)')
        fig.update_yaxes(title_text='RAS')
        fig.add_annotation(text="Severe reduction in rate of infiltration",
                    xref="paper", yref="paper",
                    x=0.2, y=0.95, showarrow=False)
        fig.add_annotation(text="Slight to moderate reduction in rate of infiltration",
                    xref="paper", yref="paper",
                    x=0.9, y=0.92, showarrow=False)
        fig.add_annotation(text="No reduction in rate of infiltration",
                    xref="paper", yref="paper",
                    x=0.85, y=0.5, showarrow=False)
        
        figura = plot(fig, output_type="div")
        context ={'plot_div': figura}
        return render(request, 'sar/dashboard.html', context)
    except:
        messages.error(request, "There is no data. Please register a sample!!")
        return render(request, 'sar/error.html')


def crearAlcalinidad(request):
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        concentracionAcidoSulfurico = str(request.POST['concentracionAcidoSulfurico'])
        volumenFenolftaleina = str(request.POST['volumenFenolftaleina'])
        volumenNaranjaDeMetilo = str(request.POST['volumenNaranjaDeMetilo'])
        volumenMuestra = str(request.POST['volumenMuestra'])
        
        respuesta = validaAlc(nombre, volumenMuestra, concentracionAcidoSulfurico, volumenFenolftaleina, volumenNaranjaDeMetilo)
        

        try:
            if respuesta == None:
                alcalinidadOh, alcalinidadCo3, alcalinidadHco3, alcalinidadFenolftaleina, alcalinidadDeNaranjaDeMetilo, alcalinidadTotal = causasAlcalinidad(float(volumenMuestra), float(concentracionAcidoSulfurico), float(volumenFenolftaleina), float(volumenNaranjaDeMetilo))
                Alcalinidad(nombre = nombre, concentracionAcidoSulfurico = concentracionAcidoSulfurico, volumenFenolftaleina = volumenFenolftaleina, volumenNaranjaDeMetilo = volumenNaranjaDeMetilo, volumenMuestra = volumenMuestra, alcalinidadDeNaranjaDeMetilo = alcalinidadDeNaranjaDeMetilo, alcalinidadFenolftaleina = alcalinidadFenolftaleina, alcalinidadHco3 = alcalinidadHco3, alcalinidadCo3 = alcalinidadCo3, alcalinidadOh = alcalinidadOh, alcalinidadTotal = alcalinidadTotal).save()
                messages.success(request, "Success!! You have successfully registered your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'alcalinidad/crear.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'alcalinidad/crear.html')

    else:

        return render(request, 'alcalinidad/crear.html')


def edicionAlcalinidad(request, id):
    muestra = Alcalinidad.objects.get(id=id)
    return render(request, 'alcalinidad/editar.html', {'muestra': muestra})


def editarAlcalinidad(request):
    id = int(request.POST['id'])
    muestra = Alcalinidad.objects.get(id=id)
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        concentracionAcidoSulfurico = str(request.POST['concentracionAcidoSulfurico'])
        volumenFenolftaleina = str(request.POST['volumenFenolftaleina'])
        volumenNaranjaDeMetilo = str(request.POST['volumenNaranjaDeMetilo'])
        volumenMuestra = str(request.POST['volumenMuestra'])
        
        respuesta = validaAlc(nombre, volumenMuestra, concentracionAcidoSulfurico, volumenFenolftaleina, volumenNaranjaDeMetilo)
        

        try:
            if respuesta == None:
                alcalinidadOh, alcalinidadCo3, alcalinidadHco3, alcalinidadFenolftaleina, alcalinidadDeNaranjaDeMetilo, alcalinidadTotal = causasAlcalinidad(float(volumenMuestra), float(concentracionAcidoSulfurico), float(volumenFenolftaleina), float(volumenNaranjaDeMetilo))
                muestra.nombre = nombre
                muestra.concentracionAcidoSulfurico = concentracionAcidoSulfurico
                muestra.volumenFenolftaleina = volumenFenolftaleina
                muestra.volumenNaranjaDeMetilo = volumenNaranjaDeMetilo
                muestra.volumenMuestra = volumenMuestra
                muestra.alcalinidadCo3 = alcalinidadCo3
                muestra.alcalinidadHco3 = alcalinidadHco3
                muestra.alcalinidadOh = alcalinidadOh
                muestra.alcalinidadFenolftaleina = alcalinidadFenolftaleina
                muestra.alcalinidadDeNaranjaDeMetilo = alcalinidadDeNaranjaDeMetilo
                muestra.alcalinidadTotal = alcalinidadTotal
                muestra.save()
                messages.success(request, "Success!! You have successfully edited your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'alcalinidad/editar.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'alcalinidad/editar.html')

    else:

        return render(request, 'alcalinidad/editar.html')


def listaAlcalinidad(request):
    listadoAlcalinidades = Alcalinidad.objects.all()

    return render(request, 'alcalinidad/lista.html', {'listadoAlcalinidades': listadoAlcalinidades})
    

def eliminarAlcalinidad(request, id):
    muestra = Alcalinidad.objects.get(id=id)
    muestra.delete()
    listadoAlcalinidades = Alcalinidad.objects.all()
    return render(request, 'alcalinidad/lista.html', {'listadoAlcalinidades': listadoAlcalinidades})


def displayAlcalinidad(request):
    try:

        otracosa = Alcalinidad.objects.all().values()
        df = pd.DataFrame(otracosa)
        df2 = df['alcalinidadTotal'].tolist()
        df3 = df['nombre'].tolist()
        df4 = df['alcalinidadHco3'].tolist()
        listaRangoAlto = []
        listaRangoBajo = []
        for i in range(df.shape[0]):
            listaRangoAlto.append("75")
            listaRangoBajo.append("20")

        diccionario = {
            'df3': df3,
            'df2': df2,
            'df4': df4,
            'listaRangoAlto' : listaRangoAlto,
            'listaRangoBajo' : listaRangoBajo
        }
        return render(request, 'alcalinidad/dashboard.html', context = diccionario)
    except:
        messages.error(request, "There is no data. Please register a sample!!")
        return render(request, 'alcalinidad/error.html')


def crearDureza(request):
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        calcio = str(request.POST['calcio'])
        magnesio = str(request.POST['magnesio'])
        bicarbonato = str(request.POST['bicarbonato'])
        carbonato = str(request.POST['carbonato'])
        alcalinidadTotalIngresado = str(request.POST['alcalinidadTotalIngresado'])
        respuesta = valiDureza(nombre, calcio, magnesio, bicarbonato, carbonato, alcalinidadTotalIngresado)

        try:
            if respuesta == None:
                durezaTotal, durezaCarbonacea, durezaNoCarbonacea, alcalinidadTotal = calculoDureza(float(calcio), float(magnesio), float(bicarbonato), float(carbonato), float(alcalinidadTotalIngresado))
                
                Dureza(nombre = nombre, calcio = calcio, magnesio = magnesio, bicarbonato = bicarbonato, carbonato = carbonato, durezaCarbonacea = durezaCarbonacea, durezaNoCarbonacea = durezaNoCarbonacea, alcalinidadTotal = alcalinidadTotal, durezaTotal = durezaTotal).save()
                messages.success(request, "Success!! You have successfully registered your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'dureza/crear.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'dureza/crear.html')
    else:

        return render(request, 'dureza/crear.html')


def edicionDureza(request, id):
    muestra = Dureza.objects.get(id=id)
    return render(request, 'dureza/editar.html', {'muestra': muestra})


def editarDureza(request):
    id = int(request.POST['id'])
    muestra = Dureza.objects.get(id=id)
    if request.method == 'POST':
        nombre = str(request.POST['nombre'])
        calcio = str(request.POST['calcio'])
        magnesio = str(request.POST['magnesio'])
        bicarbonato = str(request.POST['bicarbonato'])
        carbonato = str(request.POST['carbonato'])
        alcalinidadTotalIngresado = str(request.POST['alcalinidadTotalIngresado'])
        respuesta = valiDureza(nombre, calcio, magnesio, bicarbonato, carbonato, alcalinidadTotalIngresado)

        try:
            if respuesta == None:
                durezaTotal, durezaCarbonacea, durezaNoCarbonacea, alcalinidadTotal = calculoDureza(float(calcio), float(magnesio), float(bicarbonato), float(carbonato), float(alcalinidadTotalIngresado))
                muestra.nombre = nombre
                muestra.calcio = calcio
                muestra.magnesio = magnesio
                muestra.bicarbonato = bicarbonato
                muestra.carbonato = carbonato
                muestra.durezaCarbonacea = durezaCarbonacea
                muestra.durezaNoCarbonacea = durezaNoCarbonacea
                muestra.alcalinidadTotal = alcalinidadTotal
                muestra.durezaTotal = durezaTotal
                muestra.save()
                messages.success(request, "Success!! You have successfully edited your water sample")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'dureza/editar.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'dureza/editar.html')
    else:

        return render(request, 'dureza/editar.html')


def listaDureza(request):
    listadoDurezas = Dureza.objects.all()

    return render(request, 'dureza/lista.html', {'listadoDurezas': listadoDurezas})


def eliminarDureza(request, id):
    muestra = Dureza.objects.get(id=id)
    muestra.delete()
    listadoDurezas = Dureza.objects.all()
    return render(request, 'dureza/lista.html', {'listadoDurezas': listadoDurezas})


def displayDureza(request):
    try:
        otracosa = Dureza.objects.all().values()
        df = pd.DataFrame(otracosa)
        df2 = df['durezaTotal'].tolist()
        df3 = df['nombre'].tolist()
        df4 = df['durezaCarbonacea'].tolist()
        listaRangoAlto = []
        listaRangoBajo = []
        listaRangoModerado = []
        listaRangoModeradamenteBlanda = []
        for i in range(df.shape[0]):
            listaRangoAlto.append("180")
            listaRangoModerado.append("120")
            listaRangoModeradamenteBlanda.append("60")
            listaRangoBajo.append("17")

        diccionario = {
            'df3': df3,
            'df2': df2,
            'df4': df4,
            'listaRangoAlto' : listaRangoAlto,
            'listaRangoModerado' : listaRangoModerado,
            'listaRangoModeradamenteBlanda' : listaRangoModeradamenteBlanda,
            'listaRangoBajo' : listaRangoBajo
        }
        return render(request, 'dureza/dashboard.html', context = diccionario)
    except:
        messages.error(request, "There is no data. Please register a sample!!")
        return render(request, 'dureza/error.html')
