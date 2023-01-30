from django.db import models

# Create your models here.

class Agua(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="nombre", null=True)
    conductividadAgua = models.FloatField(verbose_name="conductividadAgua", null=True)
    solidosTotalesDisueltos = models.FloatField(verbose_name="solidosTotalesDisueltos", null=True)
    ras = models.FloatField(verbose_name="ras", null=True)
    sodio = models.FloatField(verbose_name="sodio", null=True)
    bicarbonato = models.FloatField(verbose_name="bicarbonato", null=True)
    cloruro = models.FloatField(verbose_name="cloruro", null=True)
    boro = models.FloatField(verbose_name="boro", null=True)
    manganeso = models.FloatField(verbose_name="manganeso", null=True)
    hierro = models.FloatField(verbose_name="hierro", null=True)
    sulfuroDeHidrogeno = models.FloatField(verbose_name="sulfuroDeHidrogeno", null=True)

    def __str__(self):
        
        return self.nombre


class Alcalinidad(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="nombre", null=True)
    concentracionAcidoSulfurico = models.FloatField(verbose_name="concentracionAcidoSulfurico", null=True)
    volumenFenolftaleina = models.FloatField(verbose_name="volumenFenolftaleina", null=True)
    volumenNaranjaDeMetilo = models.FloatField(verbose_name="volumenNaranjaDeMetilo", null=True)
    volumenMuestra = models.FloatField(verbose_name="volumenMuestra", null= True)
    alcalinidadDeNaranjaDeMetilo = models.FloatField(verbose_name="alcalinidadDeNaranjaDeMetilo", null=True)
    alcalinidadFenolftaleina = models.FloatField(verbose_name="alcalinidadFenolftaleina", null = True)
    alcalinidadHco3 = models.FloatField(verbose_name="alcalinidadHco3", null=True)
    alcalinidadCo3 = models.FloatField(verbose_name="alcalinidadCo3", null=True)
    alcalinidadOh = models.FloatField(verbose_name="alcalinidadOh", null = True)
    alcalinidadTotal = models.FloatField(verbose_name="alcalinidadTotal", null = True)

    def __str__(self):
        
        return self.nombre


class Sar(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="nombre", null=True)
    sodio = models.FloatField(verbose_name="sodio", null=True)
    calcio = models.FloatField(verbose_name="calcio", null=True)
    magnesio = models.FloatField(verbose_name="magnesio", null=True)
    bicarbonato = models.FloatField(verbose_name="bicarbonato", null=True)
    salinidadCe = models.FloatField(verbose_name="salinidadCe", null=True)
    sarNormal = models.FloatField(verbose_name="sarNormal", null=True)
    relacionSar = models.FloatField(verbose_name="relacionSar", null=True)
    riesgo = models.IntegerField(verbose_name="riesgo", null = True)

    def __str__(self):
        
        return self.nombre
        

class Dureza(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="nombre", null=True)
    calcio = models.FloatField(verbose_name="calcio", null=True)
    magnesio = models.FloatField(verbose_name="magnesio", null=True)
    bicarbonato = models.FloatField(verbose_name="bicarbonato", null=True)
    carbonato = models.FloatField(verbose_name="carbonato", null=True)
    durezaCarbonacea = models.FloatField(verbose_name="durezaCarbonacea", null= True)
    durezaNoCarbonacea = models.FloatField(verbose_name="durezaNoCarbonacea", null= True)
    alcalinidadTotal = models.FloatField(verbose_name="alcalinidadTotal", null = True)
    durezaTotal = models.FloatField(verbose_name="durezaTotal", null= True)

    def __str__(self):
        
        return self.nombre