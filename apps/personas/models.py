from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from apps.personas.manages import UsuarioManage
class Estd_formacion(models.TextChoices):
    OPERARIO = 'operario', 'Operario'
    AUXILIAR = 'auxiliar', 'Auxiliar'
    TECNICO = 'tecnico', 'Tecnico'
    PROFUNDIZACION = 'profundizacion', 'Profundizacion'
    TECNOLOGO = 'tecnologo', 'Tecnologo'
    EVENTO = 'evento','Evento'
    CURSO_ESPECIAL = 'curso_especial','Curso_especial'
    BILINGUISMO = 'bilinguismo', 'Bilinguismo'
    SIN_BILINGUISMO = 'sin_bilinguismo','Sin_bilinguismo'
    
class Modalidad(models.TextChoices):
    VIRTUAL = 'VIRT','Virtual'
    PRESENCIAL = 'PRE', 'Presencial'
    DISTANCIA = 'DIST', 'Distancia'

class Poblaciones(models.TextChoices):
    DESPLAZADOS_POR_VIOLENCIA = 'desplazados_por_violencia','Desplazados_por_violencia'
    HECHOS_VICTIMIZANTES = 'hechos_victimizantes','Hechos_victimizantes'
    VICTIMAS = 'victimas','Victimas'
    OTRAS_POBLACIONES_VULNERABLES = 'otras_poblaciones_vulnerables','Otras_poblaciones_vulnerables'
    TOTAL_POBLACIONES_VULNERABLES = 'total_poblaciones_vulnerables','Total_poblaciones_vulnerables'
    
class Tipo_poblaciones(models.TextChoices):
    INDIGENAS = 'indigenas','Indigenas'
    INPEC = 'inpec','inpec'
    JOVENES_VULNERABLE = 'jovenes_vulnerables','Jovenes_vulnerables'
    ADOLESCENTES_EN_CONFLICTO_CON_LA_LEY_PENAL = 'adolescentes_en_conflicto_con_la_ley_penal','Adolescentes_en_conflicto_con_la_ley_penal'
    MUJER_CABEZA_DE_HOGAR = 'mujer_cabeza_de_hogar','Mujer_cabeza_de_hogar'
    PERSONA_CON_DISCAPACIDAD = 'personas_con_discapacidad','Personas_con_discapacidad'
    NEGRITUDES = 'negritudes','Negritudes'
    AFROCOLOMBIANOS = 'afrocolombianos','Afrocolombianos'
    RAIZALES = 'raizales','Raizales'
    PALENQUEROS = 'palenqueros','Palenqueros'
    NARP = 'narp','Narp'
    REINTEGRACION_ADOLESCENTES = 'reintegracion_adolescentes','reintegracion_adolescentes'
    TERCERA_EDAD = 'tercera_edad','Tercera_edad'
    ADOLESCENTE_TRABAJADOR='adolescente_trabajador','adolescente_trabajador'
    RROOM = 'rroom','Rroom'
    
    

class   Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=100)
    rol_descripcion = models.CharField(max_length=200)


class Persona(AbstractBaseUser, PermissionsMixin):
    per_documento = models.IntegerField(primary_key=True)
    per_tipo_documento = models.CharField(max_length=100)
    per_correo = models.EmailField(unique=True)
    per_nombres = models.CharField(max_length=60)
    per_apellidos = models.CharField(max_length=60)
    per_telefono = models.CharField(max_length=10)
    rol = models.ManyToManyField(Rol, through='Persona_rol')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'per_correo'
    REQUIRED_FIELDS = ['per_documento', 'per_tipo_documento', 'per_nombres', 'per_apellidos', 'per_telefono']
    objects = UsuarioManage()
class P04(models.Model):
    p04_id = models.AutoField(primary_key=True)
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
    per_documento = models.ForeignKey(Persona, on_delete=models.CASCADE)


    
class Poblacion(models.Model):
    pob_id = models.AutoField(primary_key=True)
    pob_fecha_poblacion = models.DateField()
    pob_total_cupos = models.CharField(max_length=150)
    indicador = models.CharField(max_length=100)
    desplazamiento_por_violencia = models.CharField(max_length=100)
    hechos_victimizantes = models.CharField(max_length=100)
    victimas = models.CharField(max_length=100)
    otras_poblaciones_vulnerables = models.CharField(max_length=150)
    total_poblaciones_vulnerables = models.CharField(max_length=150)
    indigenas = models.CharField(max_length=100)
    inpec = models.CharField(max_length=100)
    jovenes_vulnerables = models.CharField(max_length=150)
    adolescente_en_conflicto_con_la_ley_penal = models.CharField(max_length=100)
    mujer_casa_de_hogar = models.CharField(max_length=100)
    persona_con_discapacidad = models.CharField(max_length=100)
    negritudes = models.CharField(max_length=100)
    afrocolombianos = models.CharField(max_length=100)
    raizales = models.CharField(max_length=100)
    palenqueros = models.CharField(max_length=100)
    narp = models.CharField(max_length=100)
    reintegracion_y_adolescentes = models.CharField(max_length=100)
    tercera_edad = models.CharField(max_length=100)
    adolescente_trabajador = models.CharField(max_length=100)
    rroom = models.CharField(max_length=100)
    per_documento = models.ForeignKey(Persona, on_delete=models.CASCADE)
    
    

class Persona_rol(models.Model):
    rolp_id = models.AutoField(primary_key=True)
    rolp_fecha_inicio = models.DateField()
    rolp_fecha_fin = models.DateField()
    rolp_estado = models.BooleanField(default=True)
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)
    

class Meta(models.Model):
    met_id = models.AutoField(primary_key=True)
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
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    
class Estrategia(models.Model):
    est_id = models.AutoField(primary_key=True)
    est_nombre = models.CharField(max_length=100)
    est_modalidad = models.CharField(max_length=50, choices=Modalidad.choices)
    est_total_meta = models.CharField(max_length=100)
    met_id = models.ForeignKey(Meta, on_delete=models.CASCADE)
    
 


class Estrategia_detalle(models.Model):
    estd_id = models.AutoField(primary_key=True)
    estd_formacion = models.CharField(max_length=100, choices=Estd_formacion.choices)
    estd_meta = models.CharField(max_length=100)
    est_id = models.ForeignKey(Estrategia, on_delete=models.CASCADE)


class Metas_formacion(models.Model):
    metd_id = models.AutoField(primary_key=True)
    metd_modalidad =  models.CharField(max_length=100,choices=Modalidad.choices)
    metf_formacion = models.CharField(max_length=100, choices=Estd_formacion.choices)
    metf_meta = models.CharField(max_length=100)
    met_id = models.ForeignKey(Meta, on_delete=models.CASCADE)


class Metas_poblacion_vulnerable(models.Model):
  
    
    metpv_id = models.AutoField(primary_key=True)
    metpv_poblacion = models.CharField(max_length=100, choices=Poblaciones.choices)
    metpv_tipo_poblacion = models.CharField(max_length=50, choices=Tipo_poblaciones.choices)
    metpv_total = models.CharField(max_length=100)
    met_id = models.ForeignKey(Meta, on_delete=models.CASCADE)
    