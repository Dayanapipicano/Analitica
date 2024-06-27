from django.db import models
class Estrategia_detalle(models.Model):
    estd_formacion = models.CharField(max_length=100)
    estd_meta = models.CharField(max_length=100)
    

class Estrategia(models.Model):
    est_nombre = models.CharField(max_length=100)
    est_modalidad = models.CharField(max_length=100)
    est_total_meta = models.CharField(max_length=100)
    estrategia_detalle = models.ForeignKey(Estrategia_detalle, on_delete=models.CASCADE)


class Metas_formacion(models.Model):
    metd_modalidad =  models.CharField(max_length=100)
    metf_formacion = models.CharField(max_length=100)
    metf_meta = models.CharField(max_length=100)
    

class Metas_poblacion_vulnerable(models.Model):
    metpv_poblacion = models.CharField(max_length=100)
    metpv_tipo_poblacion = models.CharField(max_length=100)
    
    
class P04(models.Model):
    fecha_p04 = models.DateField()
    codigo_regional = models.CharField(max_length=150)
    nombre_regional = models.CharField(max_length=150)
    codigo_centro = models.CharField(max_length=150)
    nombre_centro = models.CharField(max_length=150)
    identificador_ficha = models.CharField(max_length=150)
    estado_curso = models.CharField(max_length=150)
    codigo_nivel_formacion = models.CharField(max_length=150)
    nivel_formacion = models.CharField(max_length=150)
    codigo_jornada = models.CharField(max_length=150)
    nombre_jornada = models.CharField(max_length=150)
    tipo_de_formacion = models.CharField(max_length=150)
    fecha_inicio_ficha = models.DateField()
    fecha_terminacion_ficha = models.DateField()
    etapa_ficha = models.CharField(max_length=150)
    modalidad_formacion = models.CharField(max_length=150)
    codigo_sector_programa = models.CharField(max_length=150)
    nombre_sector_programa = models.CharField(max_length=150)
    codigo_ocupacion = models.CharField(max_length=150)
    nombre_ocupacion = models.CharField(max_length=150)
    codigo_programa = models.CharField(max_length=150)
    version_programa = models.CharField(max_length=150)
    nombre_programa_formacion = models.CharField(max_length=150)
    red = models.CharField(max_length=150)
    codigo_pais_curso = models.CharField(max_length=150)
    nombre_pais_curso = models.CharField(max_length=150)
    codigo_departamento_curso = models.CharField(max_length=150)
    nombre_departamento_curso = models.CharField(max_length=150)
    codigo_municipio_curso = models.CharField(max_length=150)
    nombre_municipio_curso = models.CharField(max_length=150)
    codigo_convenio = models.CharField(max_length=150)
    nombre_convenio = models.CharField(max_length=150)
    ampliacion_covetura = models.CharField(max_length=150)
    codigo_programa_especial = models.CharField(max_length=150)
    nombre_programa_espcial = models.CharField(max_length=150)
    numero_curso = models.CharField(max_length=150)
    total_aprendices_masculinos = models.CharField(max_length=150)
    total_aprendices_femeninos = models.CharField(max_length=150)
    total_aprendices_nobinario = models.CharField(max_length=150)
    total_aprendices = models.CharField(max_length=150)
    total_aprendices_activos = models.CharField(max_length=150)
    duracion_programa = models.CharField(max_length=150)
    nombre_nuevo_sector = models.CharField(max_length=150)
    
    
class Poblacion(models.Model):
    fecha_poblacion = models.DateField()
    

class   Rol(models.Model):
    rol_nombre = models.CharField(max_length=100)
    rol_descripcion = models.CharField(max_length=200)


class Persona(models.Model):
    per_documento = models.AutoField(primary_key=True)
    per_tipo_documento = models.CharField(max_length=100)
    per_correo = models.EmailField(unique=True)
    per_nombres = models.CharField(max_length=60)
    per_apellidos = models.CharField(max_length=60)
    per_telefono = models.CharField(max_length=10)
    rol = models.ManyToManyField(Rol)
    p04 = models.ForeignKey(P04, on_delete=models.CASCADE)
    poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)
    

class Meta(models.Model):
    met_centro_formacion = models.CharField(max_length=150)
    met_codigo = models.CharField(max_length=150)
    met_fecha_inicio = models.DateField()
    met_fecha_fin = models.DateField()
    met_año = models.CharField(max_length=4)
    met_total_otras_poblaciones = models.CharField(max_length=100)
    met_total_victimas = models.CharField(max_length=100)
    met_total_hechos_victimizantes = models.CharField(max_length=100)
    met_total_desplazados_violencia = models.CharField(max_length=100)
    met_total_titulada = models.CharField(max_length=100)
    met_total_complementaria = models.CharField(max_length=100)
    met_total_poblacion_vulnerable = models.CharField(max_length=100)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    metas_formacion = models.ForeignKey(Metas_formacion, on_delete=models.CASCADE)
    metas_poblacion_vulnerable = models.ForeignKey(Metas_poblacion_vulnerable, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    
    
