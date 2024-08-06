# Generated by Django 5.0.5 on 2024-08-05 22:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estrategia',
            fields=[
                ('est_id', models.AutoField(primary_key=True, serialize=False)),
                ('est_nombre', models.CharField(max_length=100)),
                ('est_total_meta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacion', models.CharField(choices=[('TITULADA', 'titulada'), ('COMPLEMENTARIA', 'Complementaria')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Formacion_profesional_integral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_ejecucion', models.CharField(max_length=150)),
                ('buena', models.DecimalField(decimal_places=15, max_digits=50)),
                ('vulnerable', models.DecimalField(decimal_places=15, max_digits=50)),
                ('baja', models.DecimalField(decimal_places=15, max_digits=50)),
                ('sobreejecucion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_nombre', models.CharField(max_length=100)),
                ('rol_descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('per_documento', models.IntegerField(primary_key=True, serialize=False)),
                ('per_tipo_documento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('TI', 'Tarjeta de identidad'), ('CE', ' Cedula extranjera'), ('PA', 'Pasaporte')], max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('per_nombres', models.CharField(max_length=60)),
                ('per_apellidos', models.CharField(max_length=60)),
                ('per_telefono', models.CharField(max_length=10)),
                ('per_image', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Documento_vulnerables_poblaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicadores_poblaciones', models.CharField(max_length=150)),
                ('grupos_poblaciones', models.CharField(max_length=150)),
                ('meta_2024_poblaciones', models.CharField(max_length=150)),
                ('ejecucion_poblaciones', models.CharField(max_length=150)),
                ('porcentaje_ejecucion_poblaciones', models.DecimalField(decimal_places=15, max_digits=50)),
                ('fecha_de_carga_poblaciones', models.DateTimeField(auto_now_add=True)),
                ('per_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documento_vulnerables_tipo_poblaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicadores', models.CharField(max_length=250)),
                ('grupo', models.CharField(max_length=250)),
                ('meta_2024', models.CharField(max_length=150)),
                ('ejecucion', models.CharField(max_length=150)),
                ('porcentaje_ejecucion', models.DecimalField(decimal_places=2, max_digits=50)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('per_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estrategia_detalle',
            fields=[
                ('estd_id', models.AutoField(primary_key=True, serialize=False)),
                ('estd_modalidad', models.IntegerField()),
                ('estd_operario_meta', models.CharField(max_length=150)),
                ('estd_auxiliar_meta', models.CharField(max_length=150)),
                ('estd_tecnico_meta', models.CharField(max_length=150)),
                ('estd_profundizacion_tecnica_meta', models.CharField(max_length=150)),
                ('estd_tecnologo', models.CharField(max_length=150)),
                ('estd_evento', models.CharField(max_length=150)),
                ('estd_curso_especial', models.CharField(max_length=150)),
                ('estd_bilinguismo', models.CharField(max_length=150)),
                ('estd_sin_bilinguismo', models.CharField(max_length=150)),
                ('estd_meta', models.IntegerField()),
                ('est_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.estrategia')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('pobl_id', models.AutoField(primary_key=True, serialize=False)),
                ('pobl_fecha_poblacion', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('indigenas_cupos_meta', models.IntegerField()),
                ('indigenas_aprendices_meta', models.IntegerField()),
                ('inpec_cupos_meta', models.IntegerField()),
                ('inpec_aprendices_meta', models.IntegerField()),
                ('jovenes_cupos_meta', models.IntegerField()),
                ('jovenes_aprendices_meta', models.IntegerField()),
                ('adolescente_cupos_meta', models.IntegerField()),
                ('adolescente_aprendices_meta', models.IntegerField()),
                ('mujer_cupos_meta', models.IntegerField()),
                ('mujer_aprendices_meta', models.IntegerField()),
                ('indigenas_cupos_ejecucion', models.IntegerField()),
                ('indigenas_aprendices_ejecucion', models.IntegerField()),
                ('inpec_cupos_ejecucion', models.IntegerField()),
                ('inpec_aprendices_ejecucion', models.IntegerField()),
                ('jovenes_cupos_ejecucion', models.IntegerField()),
                ('jovenes_aprendices_ejecucion', models.IntegerField()),
                ('adolescente_cupos_ejecucion', models.IntegerField()),
                ('adolescente_aprendices_ejecucion', models.IntegerField()),
                ('mujer_cupos_ejecucion', models.IntegerField()),
                ('mujer_aprendices_ejecucion', models.IntegerField()),
                ('per_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('met_id', models.AutoField(primary_key=True, serialize=False)),
                ('met_centro_formacion', models.CharField(max_length=150)),
                ('met_codigo', models.CharField(max_length=150)),
                ('met_fecha_inicio', models.DateField()),
                ('met_fecha_fin', models.DateField()),
                ('met_año', models.CharField(max_length=4)),
                ('met_total_otras_poblaciones', models.CharField(max_length=100)),
                ('met_total_victimas', models.CharField(max_length=100)),
                ('met_total_hechos_victimizantes', models.CharField(max_length=100)),
                ('met_total_desplazados_violencia', models.CharField(max_length=100)),
                ('met_total_titulada', models.CharField(max_length=100)),
                ('met_total_complementaria', models.CharField(max_length=100)),
                ('met_total_poblacion_vulnerable', models.CharField(max_length=100)),
                ('per_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='estrategia',
            name='met_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.meta'),
        ),
        migrations.CreateModel(
            name='Metas_poblacion_vulnerable',
            fields=[
                ('metpv_id', models.AutoField(primary_key=True, serialize=False)),
                ('metpv_poblacion', models.CharField(choices=[('desplazados_por_violencia', 'Desplazados_por_violencia'), ('hechos_victimizantes', 'Hechos_victimizantes'), ('victimas', 'Victimas'), ('otras_poblaciones_vulnerables', 'Otras_poblaciones_vulnerables'), ('total_poblaciones_vulnerables', 'Total_poblaciones_vulnerables')], max_length=100)),
                ('metpv_tipo_poblacion', models.CharField(choices=[('indigenas', 'Indigenas'), ('inpec', 'inpec'), ('jovenes_vulnerables', 'Jovenes_vulnerables'), ('adolescentes_en_conflicto_con_la_ley_penal', 'Adolescentes_en_conflicto_con_la_ley_penal'), ('mujer_cabeza_de_hogar', 'Mujer_cabeza_de_hogar'), ('personas_con_discapacidad', 'Personas_con_discapacidad'), ('negritudes', 'Negritudes'), ('afrocolombianos', 'Afrocolombianos'), ('raizales', 'Raizales'), ('palenqueros', 'Palenqueros'), ('narp', 'Narp'), ('reintegracion_adolescentes', 'reintegracion_adolescentes'), ('tercera_edad', 'Tercera_edad'), ('adolescente_trabajador', 'adolescente_trabajador'), ('rroom', 'Rroom')], max_length=50)),
                ('metpv_total', models.CharField(max_length=100)),
                ('met_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.meta')),
            ],
        ),
        migrations.CreateModel(
            name='Metas_formacion',
            fields=[
                ('metd_id', models.AutoField(primary_key=True, serialize=False)),
                ('met_formacion_operario', models.CharField(max_length=150)),
                ('met_formacion_auxiliar', models.CharField(max_length=150)),
                ('met_formacion_tecnico', models.CharField(max_length=150)),
                ('met_formacion_profundizacion_tecnica', models.CharField(max_length=150)),
                ('met_formacion_tecnologo', models.CharField(max_length=150)),
                ('met_formacion_evento', models.CharField(max_length=150)),
                ('met_formacion_curso_especial', models.CharField(max_length=150)),
                ('met_formacion_bilinguismo', models.CharField(max_length=150)),
                ('met_formacion_sin_bilinguismo', models.CharField(max_length=150)),
                ('met_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.meta')),
                ('metd_modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.modalidad')),
            ],
        ),
        migrations.AddField(
            model_name='estrategia',
            name='est_modalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.modalidad'),
        ),
        migrations.CreateModel(
            name='P04',
            fields=[
                ('p04_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_p04', models.DateField()),
                ('codigo_regional', models.CharField(max_length=150)),
                ('nombre_regional', models.CharField(max_length=150)),
                ('codigo_centro', models.CharField(max_length=150)),
                ('nombre_centro', models.CharField(max_length=150)),
                ('identificador_ficha', models.CharField(max_length=150)),
                ('identificador_unico_ficha', models.CharField(max_length=150)),
                ('estado_curso', models.CharField(max_length=150)),
                ('codigo_nivel_formacion', models.CharField(max_length=150)),
                ('nivel_formacion', models.CharField(max_length=150)),
                ('fecha_inicio_ficha', models.DateField()),
                ('fecha_terminacion_ficha', models.DateField()),
                ('codigo_jornada', models.CharField(max_length=150)),
                ('nombre_jornada', models.CharField(max_length=150)),
                ('tipo_de_formacion', models.CharField(max_length=150)),
                ('etapa_ficha', models.CharField(max_length=150)),
                ('modalidad_formacion', models.CharField(max_length=150)),
                ('codigo_sector_programa', models.CharField(max_length=150)),
                ('nombre_sector_programa', models.CharField(max_length=150)),
                ('codigo_ocupacion', models.CharField(max_length=150)),
                ('nombre_ocupacion', models.CharField(max_length=150)),
                ('codigo_programa', models.CharField(max_length=150)),
                ('version_programa', models.CharField(max_length=150)),
                ('nombre_programa_formacion', models.CharField(max_length=150)),
                ('red', models.CharField(max_length=150)),
                ('codigo_pais_curso', models.CharField(max_length=150)),
                ('nombre_pais_curso', models.CharField(max_length=150)),
                ('codigo_departamento_curso', models.CharField(max_length=150)),
                ('nombre_departamento_curso', models.CharField(max_length=150)),
                ('codigo_municipio_curso', models.CharField(max_length=150)),
                ('nombre_municipio_curso', models.CharField(max_length=150)),
                ('codigo_convenio', models.CharField(max_length=225)),
                ('nombre_convenio', models.CharField(max_length=225)),
                ('ampliacion_cobertura', models.CharField(max_length=150)),
                ('codigo_programa_especial', models.CharField(max_length=150)),
                ('nombre_programa_especial', models.CharField(max_length=150)),
                ('numero_cursos', models.CharField(max_length=150)),
                ('total_aprendices_masculinos', models.CharField(max_length=150)),
                ('total_aprendices_femeninos', models.CharField(max_length=150)),
                ('total_aprendices_nobinario', models.CharField(max_length=150)),
                ('total_aprendices', models.CharField(max_length=150)),
                ('total_aprendices_activos', models.CharField(max_length=150)),
                ('duracion_programa', models.CharField(max_length=150)),
                ('nombre_nuevo_sector', models.CharField(max_length=150)),
                ('per_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('pob_id', models.AutoField(primary_key=True, serialize=False)),
                ('pob_fecha_poblacion', models.DateField()),
                ('pob_total_cupos', models.CharField(max_length=150)),
                ('indicador', models.CharField(max_length=100)),
                ('desplazamiento_por_violencia', models.CharField(max_length=100)),
                ('hechos_victimizantes', models.CharField(max_length=100)),
                ('victimas', models.CharField(max_length=100)),
                ('otras_poblaciones_vulnerables', models.CharField(max_length=150)),
                ('total_poblaciones_vulnerables', models.CharField(max_length=150)),
                ('indigenas', models.CharField(max_length=100)),
                ('inpec', models.CharField(max_length=100)),
                ('jovenes_vulnerables', models.CharField(max_length=150)),
                ('adolescente_en_conflicto_con_la_ley_penal', models.CharField(max_length=100)),
                ('mujer_casa_de_hogar', models.CharField(max_length=100)),
                ('persona_con_discapacidad', models.CharField(max_length=100)),
                ('negritudes', models.CharField(max_length=100)),
                ('afrocolombianos', models.CharField(max_length=100)),
                ('raizales', models.CharField(max_length=100)),
                ('palenqueros', models.CharField(max_length=100)),
                ('narp', models.CharField(max_length=100)),
                ('reintegracion_y_adolescentes', models.CharField(max_length=100)),
                ('tercera_edad', models.CharField(max_length=100)),
                ('adolescente_trabajador', models.CharField(max_length=100)),
                ('rroom', models.CharField(max_length=100)),
                ('per_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Persona_rol',
            fields=[
                ('rolp_id', models.AutoField(primary_key=True, serialize=False)),
                ('rolp_fecha_inicio', models.DateField()),
                ('rolp_fecha_fin', models.DateField()),
                ('rolp_estado', models.BooleanField(default=True)),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.rol')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ManyToManyField(through='personas.Persona_rol', to='personas.rol'),
        ),
    ]
