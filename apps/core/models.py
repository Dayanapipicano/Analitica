from django.db import models


    
    
class Municipios(models.Model):
    
    
    class Municipio(models.TextChoices):
    
        ALMAGUER = 'ALMAGUER','Almaguer',
        ARGELIA = 'ARGELIA','Argelia',
        BALBOA = 'BALBOA','Balboa',
        BOLIVAR = 'BOLÍVAR','Bolívar',
        BUENOS_AIRES = 'BUENOS AIRES','Buenos Aires',
        CAJIBIO = 'CAJIBIO','Cajibío',
        CALDONO = 'CALDONO','Caldono',
        CALOTO = 'CALOTO','Caloto',
        CORINTO = 'CORINTO','Corinto',
        EL_TAMBO = 'EL TAMBO','El Tambo',
        FLORENCIA = 'FLORENCIA','Florencia',
        GUACHENE = 'GUACHENÉ','Guachené',
        GUAPI = 'GUAPI','Guapi',
        INZA = 'INZA','Inza',
        JAMBALO = 'JAMBALO','Jambaló',
        LA_SIERRA = 'LA SIERRA','La Sierra',
        LA_VEGA ='LA VEGA','La Vega',
        LOPEZ = 'LOPEZ','López',
        MERCADERES = 'MERCADERES','Mercaderes',
        MIRANDA = 'MIRANDA','Miranda',
        MORALES = 'MORALES','Morales',
        PATIA_EL_BORDO = 'PATIA (EL BORDO)','Patía (El Bordo)',
        PAEZ_BELALCAZAR = 'PAEZ (BELALCAZAR)','Páez (Belalcázar)',
        POPAYAN ='POPAYÁN','Popayán',
        PUERTO_TEJADA = 'PUERTO TEJADA','Puerto Tejada',
        PURACÉ_COCONUCO = 'PURACÉ (COCONUCO)','Puracé (Coconuco)',
        SAN_SEBASTIAN = 'SAN SEBASTIÁN','San Sebastián',
        SANTANDER_DE_QUILICHAO = 'SANTANDER DE QUILICHAO','Santander de Quilichao',
        SANTA_ROSA ='SANTA ROSA','Santa Rosa',
        SILVIA = 'SILVIA','Silvia',
        SOTARA_PAISPAMBA = 'SOTARA (PAISPAMBA)','Sotará (Paispamba)',
        SUCRE = 'SUCRE','Sucre',
        SUAREZ = 'SUAREZ','Suarez',
        TIMBIO = 'TIMBIO','Timbío',
        TIMBIQUI = 'TIMBIQUI','Timbiquí',
        TOTORO = 'TOTORO','Totoró',
        VILLA_RICA = 'VILLA RICA','Villa Rica' 

    
    nombre = models.CharField(max_length=150, choices=Municipio.choices)