function filtros_desercion(){
    const modalidad = document.getElementById('id_modalidad').value
    const municipio = document.getElementById('id_municipio').value
    const regional = document.getElementById('id_regional').value
    const centro_de_formacion = document.getElementById('id_centro_de_formacion').value
    const fecha_inicio_ficha = document.getElementById('filtroFechaInicio').value
  
    if (modalidad){
        url_filtro += `modalidad=${modalidad}&`;
    }
    if (municipio){
        url_filtro += `municipio=${municipio}&`;
    }
    if (regional){
        url_filtro += `regional=${regional}&`;
    }
    if (centro_de_formacion){
        url_filtro += `centro_de_formacion=${centro_de_formacion}`;
    }
    if (fecha_inicio_ficha){

        const fecha_inicio = new Date(fecha_inicio_ficha)

        const fecha_formato = fecha_inicio.toISOString().split('T')[0]
        url_filtro += `fecha_inicio_ficha=${fecha_formato}`
    }
    window.location.href = url_filtro;
}