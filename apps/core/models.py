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
    
    
    
class Programas_formacion(models.Model):
    
    
    class Programas_formacion_choices(models.TextChoices):
    
    
        ATENCION_INTEGRAL_A_LA_PRIMERA_INFANCIA = '.ATENCION INTEGRAL A LA PRIMERA INFANCIA','.ATENCION INTEGRAL A LA PRIMERA INFANCIA',
        ABORDAJE_DE_PERSONAS_CON_DISCAPACIDAD = 'ABORDAJE DE PERSONAS CON DISCAPACIDAD','ABORDAJE DE PERSONAS CON DISCAPACIDAD',
        ACCIONES_DE_PREVENCION_EN_SALUD_MENTAL = 'ACCIONES DE PREVENCION EN SALUD MENTAL','ACCIONES DE PREVENCION EN SALUD MENTAL',
        ADMINISTRACION_DE_RECURSOS_HUMANOS = 'ADMINISTRACION DE RECURSOS HUMANOS','ADMINISTRACION DE RECURSOS HUMANOS',
        ADMINISTRACION_DOCUMENTAL_EN_EL_ENTORNO_LABORAL = 'ADMINISTRACION DOCUMENTAL EN EL ENTORNO LABORAL','ADMINISTRACION DOCUMENTAL EN EL ENTORNO LABORAL',
        ADMINISTRACION_Y_CONTROL_DE_INVENTARIOS = 'ADMINISTRACION Y CONTROL DE INVENTARIOS','ADMINISTRACION Y CONTROL DE INVENTARIOS',
        AGENTE_DE_TRANSITO_Y_TRANSPORTE = 'AGENTE DE TRANSITO Y TRANSPORTE','AGENTE DE TRANSITO Y TRANSPORTE',
        ANALISIS_FINANCIERO = 'ANALISIS FINANCIERO.','ANALISIS FINANCIERO.',
        ANALISIS_Y_DESARROLLO_DE_SOFTWARE = 'ANALISIS Y DESARROLLO DE SOFTWARE.','ANALISIS Y DESARROLLO DE SOFTWARE.',
        ANIMACION_3D = 'ANIMACION 3D.','ANIMACION 3D.',
        ANIMACION_DIGITAL = 'ANIMACION DIGITAL','ANIMACION DIGITAL',
        APLICACION_DE_LA_ELECTRONICA_EN_PROYECTOS_DE_CIENCIA_TECNOLOGIA_E_INNOVACION_CON_ENFOQUE_RURAL = 'APLICACION DE LA ELECTRONICA EN PROYECTOS DE CIENCIA, TECNOLOGIA E INNOVACION CON ENFOQUE RURAL','APLICACION DE LA ELECTRONICA EN PROYECTOS DE CIENCIA, TECNOLOGIA E INNOVACION CON ENFOQUE RURAL',
        APLICACION_DEL_ENFOQUE_DIFERENCIAL_EN_LA_GESTION_DE_LOS_PROCESOS_MISIONALES_ESTRATEGICOS_Y_DE_SOPORTE_DEL_SENA = 'APLICACION DEL ENFOQUE DIFERENCIAL EN LA GESTION DE LOS PROCESOS MISIONALES, ESTRATEGICOS Y DE SOPORTE DEL SENA.','APLICACION DEL ENFOQUE DIFERENCIAL EN LA GESTION DE LOS PROCESOS MISIONALES, ESTRATEGICOS Y DE SOPORTE DEL SENA.'
        APOYO_ADMINISTRATIVO_EN_SALUD = 'APOYO ADMINISTRATIVO EN SALUD.','APOYO ADMINISTRATIVO EN SALUD.',
        APRENDIZ_DIGITAL = 'APRENDIZ DIGITAL','APRENDIZ DIGITAL',
        ASISTENCIA_ADMINISTRATIVA = 'ASISTENCIA ADMINISTRATIVA .','ASISTENCIA ADMINISTRATIVA .',
        ASISTENCIA_EN_ORGANIZACION_DE_ARCHIVOS= 'ASISTENCIA EN ORGANIZACION DE ARCHIVOS .','ASISTENCIA EN ORGANIZACION DE ARCHIVOS .',
        ATENCION_AL_CLIENTE_EN_LOS_PROCESOS_ADMINISTRATIVOS = 'ATENCION AL CLIENTE EN LOS PROCESOS ADMINISTRATIVOS','ATENCION AL CLIENTE EN LOS PROCESOS ADMINISTRATIVOS',
        BIOSEGURIDAD_APLICADA_A_LA_ESTETICA_Y_BELLEZA = 'BIOSEGURIDAD APLICADA A LA ESTETICA Y BELLEZA','BIOSEGURIDAD APLICADA A LA ESTETICA Y BELLEZA',
        CIUDADANIA_DIGITAL_PARA_LA_PAZ = 'CIUDADANIA DIGITAL PARA LA PAZ','CIUDADANIA DIGITAL PARA LA PAZ',
        COCINA_BÁSICA = 'COCINA BÁSICA','COCINA BÁSICA',
        COCINA = 'COCINA.','COCINA.',
        COMPETENCIAS_CIUDADANAS_EN_LA_SEGURIDAD_VIAL = 'COMPETENCIAS CIUDADANAS EN LA SEGURIDAD VIAL.','COMPETENCIAS CIUDADANAS EN LA SEGURIDAD VIAL.',
        COMPORTAMIENTO_EMPRENDEDOR = 'COMPORTAMIENTO EMPRENDEDOR','COMPORTAMIENTO EMPRENDEDOR',
        CONFECCION_DE_MUÑECAS_DE_TRAPO = 'CONFECCION DE MUÑECAS DE TRAPO.','CONFECCION DE MUÑECAS DE TRAPO.',
        CONTABILIDAD_EN_LAS_ORGANIZACIONES= 'CONTABILIDAD EN LAS ORGANIZACIONES.','CONTABILIDAD EN LAS ORGANIZACIONES.',
        CONTABILIZACION_DE_OPERACIONES_COMERCIALES_Y_FINANCIERAS = 'CONTABILIZACION DE OPERACIONES COMERCIALES Y FINANCIERAS.','CONTABILIZACION DE OPERACIONES COMERCIALES Y FINANCIERAS.',
        CONTROL_DE_LA_SEGURIDAD_DIGITAL = 'CONTROL DE LA SEGURIDAD DIGITAL.','CONTROL DE LA SEGURIDAD DIGITAL.',
        COORDINACION_DE_PROCESOS_LOGISTICOS = 'COORDINACION DE PROCESOS LOGISTICOS','COORDINACION DE PROCESOS LOGISTICOS',
        CREACION_DE_FUNCIONES_Y_GRAFICOS_USANDO_MICROSOFT_EXCEL = 'CREACION DE  FUNCIONES Y GRAFICOS USANDO MICROSOFT EXCEL','CREACION DE  FUNCIONES Y GRAFICOS USANDO MICROSOFT EXCEL',
        CUIDADO_ESTETICO_DE_MANOS_Y_PIES = 'CUIDADO ESTETICO DE MANOS Y PIES..','CUIDADO ESTETICO DE MANOS Y PIES..',
        CUIDADOS_BASICOS_A_PERSONAS_MAYORES = 'CUIDADOS BASICOS A PERSONAS MAYORES','CUIDADOS BASICOS A PERSONAS MAYORES',
        DECORACION_DE_OBJETOS_ARTESALES_EN_MADERA ='DECORACION DE OBJETOS ARTESALES EN MADERA','DECORACION DE OBJETOS ARTESALES EN MADERA',
        DESARROLLO_DE_PROCESOS_DE_MERCADEO = 'DESARROLLO DE PROCESOS DE MERCADEO','DESARROLLO DE PROCESOS DE MERCADEO',
        DESARROLLO_DE_PROYECTOS_DECORATIVOS_Y_UTILITARIOS_CON_MATERIALES_RECICLABLES = 'DESARROLLO DE PROYECTOS DECORATIVOS Y UTILITARIOS CON MATERIALES RECICLABLES','DESARROLLO DE PROYECTOS DECORATIVOS Y UTILITARIOS CON MATERIALES RECICLABLES',
        DESARROLLO_DE_PROYECTOS_EMPRENDEDORES_EN_PROCESAMIENTO_DE_ALIMENTOS = 'DESARROLLO DE PROYECTOS EMPRENDEDORES EN PROCESAMIENTO DE ALIMENTOS','DESARROLLO DE PROYECTOS EMPRENDEDORES EN PROCESAMIENTO DE ALIMENTOS',
        DESARROLLO_PUBLICITARIO = 'DESARROLLO PUBLICITARIO','DESARROLLO PUBLICITARIO',
        ECONOMIA_SOLIDARIA_FINANCIACION_Y_COMERCIALIZACION = 'ECONOMIA SOLIDARIA FINANCIACION Y COMERCIALIZACION','ECONOMIA SOLIDARIA FINANCIACION Y COMERCIALIZACION',
        EDT_NEUROMARKETING_ESTRATÉGICO_EN_PROCESOS_EDUCATIVOS_Y_DESARROLLO_DE_MERCADOS = 'EDT- NEUROMARKETING ESTRATÉGICO EN PROCESOS EDUCATIVOS Y DESARROLLO DE MERCADOS','EDT- NEUROMARKETING ESTRATÉGICO EN PROCESOS EDUCATIVOS Y DESARROLLO DE MERCADOS',
        EDT_TRANSFERENCIA_TECNOLÓGICA_PARA_EL_USO_DE_EQUIPOS_LABORATORIO_DE_NEUROMARKETING_CENTRO_DE_COMERCIO_Y_SERVICIOS = 'EDT- TRANSFERENCIA TECNOLÓGICA PARA EL USO DE EQUIPOS LABORATORIO DE NEUROMARKETING CENTRO DE COMERCIO Y SERVICIOS','EDT- TRANSFERENCIA TECNOLÓGICA PARA EL USO DE EQUIPOS LABORATORIO DE NEUROMARKETING CENTRO DE COMERCIO Y SERVICIOS',
        EJERCICIO_DERECHOS_FUNDAMENTALES_EN_EL_TRABAJO = 'EJERCICIO DERECHOS FUNDAMENTALES EN EL TRABAJO','EJERCICIO DERECHOS FUNDAMENTALES EN EL TRABAJO',
        ELABORACION_ARTESANAL_DE_PRODUCTOS_DE_PANIFICACION = 'ELABORACION ARTESANAL DE PRODUCTOS DE PANIFICACION.','ELABORACION ARTESANAL DE PRODUCTOS DE PANIFICACION.',
        ELABORACIÓN_BÁSICA_DE_TORTAS_Y_GALLETAS = 'ELABORACIÓN BÁSICA DE TORTAS Y GALLETAS','ELABORACIÓN BÁSICA DE TORTAS Y GALLETAS',
        ELABORACION_DE_ACCESORIOS_EN_BISUTERIA_CON_IDENTIDAD_REGIONAL = 'ELABORACION DE ACCESORIOS EN BISUTERIA CON IDENTIDAD REGIONAL','ELABORACION DE ACCESORIOS EN BISUTERIA CON IDENTIDAD REGIONAL',
        ELABORACION_DE_BORDADO_A_MANO_TRADICIONAL = 'ELABORACION DE BORDADO A MANO TRADICIONAL','ELABORACION DE BORDADO A MANO TRADICIONAL',
        ELABORACION_DE_COMPLEMENTOS_EN_BISUTERIA_CON_TECNICA_DE_ENSARTADO = 'ELABORACION DE COMPLEMENTOS EN BISUTERIA CON TECNICA DE ENSARTADO','ELABORACION DE COMPLEMENTOS EN BISUTERIA CON TECNICA DE ENSARTADO',
        ELABORACION_DE_HELADOS_Y_POSTRES_LACTEOS = 'ELABORACION DE HELADOS Y POSTRES LACTEOS','ELABORACION DE HELADOS Y POSTRES LACTEOS',
        ELABORACION_DE_NUDOS_EN_MACRAME = 'ELABORACION DE NUDOS EN MACRAME','ELABORACION DE NUDOS EN MACRAME',
        ELABORACIÓN_DE_PANES_ARTESANALES = 'ELABORACIÓN DE PANES ARTESANALES','ELABORACIÓN DE PANES ARTESANALES',
        ELABORACIÓN_DE_PRODUCTOS_ARTESANALES_EN_CROCHET = 'ELABORACIÓN DE PRODUCTOS ARTESANALES EN CROCHET','ELABORACIÓN DE PRODUCTOS ARTESANALES EN CROCHET',
        ELABORACION_DE_PRODUCTOS_CARNICOS_EMULSIONADOS = 'ELABORACION DE PRODUCTOS CARNICOS EMULSIONADOS','ELABORACION DE PRODUCTOS CARNICOS EMULSIONADOS',
        ELABORACION_DE_TEJIDOS_EN_TECNICA_DE_CROCHET ='ELABORACION DE TEJIDOS EN TECNICA DE CROCHET','ELABORACION DE TEJIDOS EN TECNICA DE CROCHET',
        ELABORACION_PRODUCTOS_QUIMICOS_PARA_PROCEDIMIENTOS_DE_LIMPIEZA_Y_DESINFECCION = 'ELABORACION PRODUCTOS QUIMICOS PARA PROCEDIMIENTOS DE LIMPIEZA Y DESINFECCION','ELABORACION PRODUCTOS QUIMICOS PARA PROCEDIMIENTOS DE LIMPIEZA Y DESINFECCION',
        EMPRENDEDOR_EN_DESARROLLO_DE_ACTIVIDADES_TURISTICAS_EN_ESPACIOS_NATURALES ='EMPRENDEDOR EN DESARROLLO DE ACTIVIDADES TURISTICAS EN ESPACIOS NATURALES','EMPRENDEDOR EN DESARROLLO DE ACTIVIDADES TURISTICAS EN ESPACIOS NATURALES',
        EMPRENDEDOR_EN_ELABORACION_DE_ARTESANIAS_CON_TEJIDO_ETNICO ='EMPRENDEDOR EN ELABORACION DE ARTESANIAS CON TEJIDO ETNICO','EMPRENDEDOR EN ELABORACION DE ARTESANIAS CON TEJIDO ETNICO',
        EMPRENDEDOR_EN_GASTRONOMIA_IPICA_RURAL ='EMPRENDEDOR EN GASTRONOMIA TIPICA RURAL','EMPRENDEDOR EN GASTRONOMIA TIPICA RURAL',
        EMPRENDIMIENTO_EN_EL_PROCESAMIENTO_DE_PRODUCTOS_DE_CHOCOLATERIA ='EMPRENDIMIENTO EN EL PROCESAMIENTO DE PRODUCTOS  DE CHOCOLATERIA','EMPRENDIMIENTO EN EL PROCESAMIENTO DE PRODUCTOS  DE CHOCOLATERIA',
        EMPRENDIMIENTO_EN_EL_PROCESAMIENTO_DE_PRODUCTOS_DE_PANIFICACION ='EMPRENDIMIENTO EN EL PROCESAMIENTO DE PRODUCTOS DE PANIFICACION','EMPRENDIMIENTO EN EL PROCESAMIENTO DE PRODUCTOS DE PANIFICACION',
        EMPRENDIMIENTO_INNOVADOR ='EMPRENDIMIENTO INNOVADOR','EMPRENDIMIENTO INNOVADOR',
        ENFERMERIA ='ENFERMERIA.','ENFERMERIA.',
        ENGLISH_DOES_WORK_LEVEL_1 ='ENGLISH DOES WORK - LEVEL 1','ENGLISH DOES WORK - LEVEL 1',
        ENGLISH_DOES_WORK_LEVEL_5 ='ENGLISH DOES WORK - LEVEL 5','ENGLISH DOES WORK - LEVEL 5',
        ENGLISH_DOES_WORK_LEVEL_6 ='ENGLISH DOES WORK - LEVEL 6','ENGLISH DOES WORK - LEVEL 6',
        ENGLISH_DOES_WORK_LEVEL_7 ='ENGLISH DOES WORK - LEVEL 7','ENGLISH DOES WORK - LEVEL 7',
        FACTURACION_DE_LOS_SERVICIOS_EN_SALUD ='FACTURACION DE LOS SERVICIOS EN  SALUD','FACTURACION DE LOS SERVICIOS EN  SALUD',
        FOTOGRAFIA_BASICA_DE_PRODUCTOS_PARA_REDES_SOCIALES ='FOTOGRAFIA BASICA DE PRODUCTOS PARA REDES SOCIALES','FOTOGRAFIA BASICA DE PRODUCTOS PARA REDES SOCIALES',
        GENERACION_DE_IDEAS_PARA_UN_NEGOCIO_INNOVADOR ='GENERACION DE IDEAS PARA UN NEGOCIO INNOVADOR','GENERACION DE IDEAS PARA UN NEGOCIO INNOVADOR',
        GESTION_ADMINISTRATIVA_DEL_SECTOR_SALUD ='GESTION ADMINISTRATIVA DEL SECTOR SALUD.','GESTION ADMINISTRATIVA DEL SECTOR SALUD.',
        GESTIÓN_BANCARIA_Y_DE_ENTIDADES_FINANCIERAS ='GESTIÓN BANCARIA Y DE ENTIDADES FINANCIERAS','GESTIÓN BANCARIA Y DE ENTIDADES FINANCIERAS',
        GESTION_CONTABLE_Y_DE_INFORMACION_FINANCIERA ='GESTION CONTABLE Y DE INFORMACION FINANCIERA','GESTION CONTABLE Y DE INFORMACION FINANCIERA',
        GESTION_CONTABLE_Y_FINANCIERA ='GESTION CONTABLE Y FINANCIERA','GESTION CONTABLE Y FINANCIERA',
        GESTIÓN_DE_MERCADOS ='GESTIÓN DE MERCADOS','GESTIÓN DE MERCADOS',
        GESTION_DE_PROYECTOS_COMUNITARIOS ='GESTION DE PROYECTOS COMUNITARIOS','GESTION DE PROYECTOS COMUNITARIOS',
        GESTIÓN_DEL_TALENTO_HUMANO ='GESTIÓN DEL TALENTO HUMANO','GESTIÓN DEL TALENTO HUMANO',
        GESTION_DOCUMENTAL = 'GESTION DOCUMENTAL .','GESTION DOCUMENTAL .',
        GESTIÓN_EMPRESARIAL ='GESTIÓN EMPRESARIAL','GESTIÓN EMPRESARIAL',
        GESTION_INTEGRAL_DEL_TRANSPORTE ='GESTION INTEGRAL DEL TRANSPORTE','GESTION INTEGRAL DEL TRANSPORTE',
        HABILIDADES_PARA_ENFRENTAR_RETOS_EN_EL_NUEVO_ENTORNO_LABORAL ='HABILIDADES PARA ENFRENTAR RETOS EN EL NUEVO ENTORNO LABORAL','HABILIDADES PARA ENFRENTAR RETOS EN EL NUEVO ENTORNO LABORAL',
        HIGIENE_Y_MANIPULACION_DE_ALIMENTOS = 'HIGIENE Y MANIPULACION DE ALIMENTOS.','HIGIENE Y MANIPULACION DE ALIMENTOS.',
        HUMANIZACION_DE_LA_ATENCION_EN_SALUD ='HUMANIZACION DE LA ATENCION EN SALUD.','HUMANIZACION DE LA ATENCION EN SALUD.',
        IDENTIFICACION_DE_LAS_GENERALIDADES_DE_LOS_EMPAQUES ='IDENTIFICACION DE LAS GENERALIDADES DE LOS EMPAQUES.','IDENTIFICACION DE LAS GENERALIDADES DE LOS EMPAQUES.',
        INFORMATICA_MICROSOFT_WORD_EXCEL_E_INTERNET = 'INFORMATICA: MICROSOFT WORD, EXCEL E INTERNET','INFORMATICA: MICROSOFT WORD, EXCEL E INTERNET',
        INGLES_BASICO_NIVEL_1 ='INGLES BASICO - NIVEL 1','INGLES BASICO - NIVEL 1',
        INGLES_BASICO_NIVEL_3 ='INGLES BASICO - NIVEL 3','INGLES BASICO - NIVEL 3',
        INGLES_BASICO_NIVEL_4 ='INGLES BASICO - NIVEL 4','INGLES BASICO - NIVEL 4',
        INTERVENCION_PARA_LA_PREVENCION_Y_SEGURIDAD_VIAL ='INTERVENCION PARA LA PREVENCION Y SEGURIDAD VIAL','INTERVENCION PARA LA PREVENCION Y SEGURIDAD VIAL',
        LENCERIA_HOGAR ='LENCERIA HOGAR','LENCERIA HOGAR',
        LIDERAZGO_EFECTIVO ='LIDERAZGO EFECTIVO','LIDERAZGO EFECTIVO',
        LIMPIEZA_DE_AREAS_Y_SUPERFICIES ='LIMPIEZA DE AREAS Y SUPERFICIES','LIMPIEZA DE AREAS Y SUPERFICIES',
        LIMPIEZA_DESINFECCION_Y_ESTERILIZACION_DE_ARTICULOS_Y_EQUIPOS_HOSPITALARIOS ='LIMPIEZA, DESINFECCION Y ESTERILIZACION DE ARTICULOS Y EQUIPOS HOSPITALARIOS','LIMPIEZA, DESINFECCION Y ESTERILIZACION DE ARTICULOS Y EQUIPOS HOSPITALARIOS',
        MANEJO_DE_HERRAMIENTAS_MICROSOFT_OFFICE_2016_EXCEL ='MANEJO DE HERRAMIENTAS MICROSOFT OFFICE 2016: EXCEL','MANEJO DE HERRAMIENTAS MICROSOFT OFFICE 2016: EXCEL',
        MANEJO_DE_LA_INFORMACION_EN_RECORRIDOS_DE_OBSERVACION_DE_AVES_PARA_EL_TURISMO ='MANEJO DE LA INFORMACION EN RECORRIDOS DE OBSERVACION DE AVES PARA EL TURISMO','MANEJO DE LA INFORMACION EN RECORRIDOS DE OBSERVACION DE AVES PARA EL TURISMO',
        MANEJO_DE_LA_INFORMACION_TURISTICA_REGIONAL ='MANEJO DE LA INFORMACION TURISTICA REGIONAL','MANEJO DE LA INFORMACION TURISTICA REGIONAL',
        MANIPULACION_DE_ALIMENTOS ='MANIPULACION DE ALIMENTOS','MANIPULACION DE ALIMENTOS',
        MANTENIMIENTO_DE_COMPUTADORES_NIVEL_I ='MANTENIMIENTO DE COMPUTADORES NIVEL I','MANTENIMIENTO DE COMPUTADORES NIVEL I',
        MARKETING_DIGITAL ='MARKETING DIGITAL','MARKETING DIGITAL',
        MERCADEO_Y_VENTAS ='MERCADEO Y VENTAS','MERCADEO Y VENTAS',
        MODELAJE_MANUAL_DE_BILLETERAS ='MODELAJE MANUAL DE BILLETERAS','MODELAJE MANUAL DE BILLETERAS',
        NEGOCIACIÓN_INTERNACIONAL ='NEGOCIACIÓN INTERNACIONAL','NEGOCIACIÓN INTERNACIONAL',
        OPERACION_TURISTICA_LOCAL ='OPERACION TURISTICA LOCAL','OPERACION TURISTICA LOCAL',
        OPERACIONES_COMERCIALES_EN_RETAIL ='OPERACIONES COMERCIALES EN RETAIL','OPERACIONES COMERCIALES EN RETAIL',
        OPERACIONES_DE_COMERCIO_EXTERIOR ='OPERACIONES DE COMERCIO EXTERIOR','OPERACIONES DE COMERCIO EXTERIOR',
        ORGANIZACION_DE_ARCHIVOS_DE_GESTION ='ORGANIZACION DE ARCHIVOS DE GESTION.','ORGANIZACION DE ARCHIVOS DE GESTION.',
        ORGANIZACION_DOCUMENTAL_EN_EL_ENTORNO_LABORAL ='ORGANIZACION DOCUMENTAL EN EL ENTORNO LABORAL','ORGANIZACION DOCUMENTAL EN EL ENTORNO LABORAL',
        PANADERIA ='PANADERIA','PANADERIA',
        PANIFICACION ='PANIFICACION.','PANIFICACION.',
        PELUQUERIA ='PELUQUERIA.','PELUQUERIA.',
        PLANEACION_DE_LA_ESTRATEGIA_DE_COMERCIO_ELECTRONICO ='PLANEACION DE LA ESTRATEGIA DE COMERCIO ELECTRONICO','PLANEACION DE LA ESTRATEGIA DE COMERCIO ELECTRONICO',
        PRESELECCION_DE_TALENTO_HUMANO_MEDIADO_POR_HERRAMIENTAS_TIC ='PRESELECCION DE TALENTO HUMANO MEDIADO POR HERRAMIENTAS TIC','PRESELECCION DE TALENTO HUMANO MEDIADO POR HERRAMIENTAS TIC',
        PRESERVACIÓN_DE_LA_INFORMACIÓN ='PRESERVACIÓN DE LA INFORMACIÓN.','PRESERVACIÓN DE LA INFORMACIÓN.',
        PRIMEROS_AUXILIOS ='PRIMEROS  AUXILIOS','PRIMEROS  AUXILIOS',
        PROCESAMIENTO_DE_PRODUCTOS_CARNICOS_CRUDOS ='PROCESAMIENTO DE PRODUCTOS CARNICOS CRUDOS','PROCESAMIENTO DE PRODUCTOS CARNICOS CRUDOS',
        PROGRAMACION_PARA_ANALITICA_DE_DATOS ='PROGRAMACION PARA ANALITICA DE DATOS.','PROGRAMACION PARA ANALITICA DE DATOS.',
        PROGRAMAR_SENSORES_Y_ACTUADORES_EN_LA_RURALIDAD ='PROGRAMAR SENSORES Y ACTUADORES EN LA RURALIDAD','PROGRAMAR SENSORES Y ACTUADORES EN LA RURALIDAD',
        RECURSOS_HUMANOS ='RECURSOS HUMANOS .','RECURSOS HUMANOS .',
        SALUD_PUBLICA ='SALUD PUBLICA','SALUD PUBLICA',
        SERVICIO_AL_CLIENTE ='SERVICIO AL CLIENTE','SERVICIO AL CLIENTE',
        SERVICIO_DE_RESTAURANTE_Y_BAR ='SERVICIO DE RESTAURANTE Y BAR','SERVICIO DE RESTAURANTE Y BAR',
        SERVICIOS_DE_BARISMO ='SERVICIOS DE BARISMO','SERVICIOS DE BARISMO',
        SERVICIOS_DE_BARTENDER ='SERVICIOS DE BARTENDER','SERVICIOS DE BARTENDER',
        SERVICIOS_FARMACEUTICOS ='SERVICIOS FARMACEUTICOS','SERVICIOS FARMACEUTICOS',
        SERVICIOS_Y_OPERACIONES_MICROFINANCIERAS ='SERVICIOS Y OPERACIONES MICROFINANCIERAS','SERVICIOS Y OPERACIONES MICROFINANCIERAS',
        SISTEMAS ='SISTEMAS.','SISTEMAS.',
        SOPORTE_VITAL_BASICO ='SOPORTE VITAL BASICO.','SOPORTE VITAL BASICO.',
        SUMINISTRO_DE_INFORMACION_Y_ASESORIA_PARA_EL_CONSUMIDOR_FINANCIERO ='SUMINISTRO DE INFORMACION Y ASESORIA PARA EL CONSUMIDOR FINANCIERO','SUMINISTRO DE INFORMACION Y ASESORIA PARA EL CONSUMIDOR FINANCIERO',
        TECNICAS_EN_VENTAS ='TECNICAS  EN VENTAS','TECNICAS  EN VENTAS',
        TÉCNICAS_BÁSICAS_DE_PINTURA_SOBRE_MADERA ='TÉCNICAS BÁSICAS DE PINTURA SOBRE MADERA','TÉCNICAS BÁSICAS DE PINTURA SOBRE MADERA',
        VENTA_DE_PRODUCTOS_EN_LINEA ='VENTA DE PRODUCTOS EN LINEA','VENTA DE PRODUCTOS EN LINEA',
        

    programa_formacion = models.CharField(max_length=150, choices=Programas_formacion_choices.choices)  
     
        
        
        
        
class Nivel_formacion(models.Model):
    
    class Nivel_formacion_choices(models.TextChoices):
        
        AUXILIAR = 'AUXILIAR','Auxiliar',
        CURSO_ESPECIAL ='CURSO ESPECIAL','Curso especial',
        EVENTO ='EVENTO','Evento',
        OPERARIO ='OPERARIO','Operario',
        TECNICO ='TÉCNICO','Técnico',
        TECNOLOGO ='TECNÓLOGO','Tecnólogo'
        
    
    nivel_formacion = models.CharField(max_length=150, choices=Nivel_formacion_choices.choices)
   