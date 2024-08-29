


// funcion de modales 

document.addEventListener('DOMContentLoaded', function() {

        document. metaField =  document.getElements
        document.querySelector('#submit-second-modal_meta').addEventListener('click', function(event) {
            event.preventDefault(); // Evita el comportamiento por defecto del botón
    
            // Selecciona el formulario en el segundo modal
            var form = document.querySelector('#second-modal-form_meta');
            var formData = new FormData(form);
    
            // Envía los datos del formulario usando fetch
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': form.querySelector('[name="csrfmiddlewaretoken"]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Simula el clic en el botón de cerrar para cerrar el segundo modal
                    document.querySelector('#close-second-modal').click();
    
                    // Limpia el formulario después de cerrar el modal
                    form.reset();
                    
                } else {
                    // Muestra errores si la respuesta es fallida
                    console.log('Error:', data.errors);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

// suma de los datos para total meta
document.addEventListener('DOMContentLoaded', function() {
        const metaSelects = document.querySelectorAll('select[name="met_id"]');
        const totalMetaFields = document.querySelectorAll('input[name="est_total_meta"]');
    
        metaSelects.forEach((metaSelect, index) => {
            const totalMetaField = totalMetaFields[index]; // Campo total correspondiente
    
            metaSelect.addEventListener('change', function() {
                const selectedMetaId = metaSelect.value;
                fetchMetaValues(selectedMetaId, totalMetaField);
            });
        });
        function fetchMetaValues(metaId, totalMetaField) {
            fetch(`/estrategias/est_total_meta/${metaId}/`)
                .then(response => response.json())
                .then(data => {
                    let total = 0;
                   
                    if (data) {
                        let met_total_otras_poblaciones = parseFloat(data.met_total_otras_poblaciones) || 0;
                        let met_total_victimas = parseFloat(data.met_total_victimas) || 0;
                        let met_total_hechos_victimizantes = parseFloat(data.met_total_hechos_victimizantes) || 0;
                        let met_total_desplazados_violencia = parseFloat(data.met_total_desplazados_violencia) || 0;
                        let met_total_titulada = parseFloat(data.met_total_titulada) || 0;
                        let met_total_complementaria = parseFloat(data.met_total_complementaria) || 0;
                        let met_total_poblacion_vulnerable = parseFloat(data.met_total_poblacion_vulnerable) || 0;
                        total = met_total_otras_poblaciones + met_total_victimas + met_total_hechos_victimizantes+met_total_desplazados_violencia + met_total_titulada+met_total_complementaria+met_total_poblacion_vulnerable;
                    }
                    totalMetaField.value = total;
                })
                .catch(error => console.error('Error fetching meta values:', error));
        }
    });


//maneja filtros dentro del formulario metas formacion (est_id)
document.addEventListener('DOMContentLoaded', function () {
    
    const estrategiaField = document.querySelector('#id_est_id');
    const metaField = document.querySelector('#id_estd_meta');


    estrategiaField.addEventListener('change', function(){
        const id_estrategia = this.value;

        fetch(`/meta_data/${id_estrategia}`)
        .then(response => response.json())
        .then(data =>{
            console.log(data);

            metaField.innerHTML = '<option value="">Seleccionar</option>';
            

            
            if(data.meta){
                    const meta = data.meta;
                    const option = document.createElement('option');
                    option.value = meta.met_id;
                    option.textContent = meta.met_año;
                    metaField.appendChild(option)


            }
        })
    })
});




  //alaertas para el formulario de meta create
document.getElementById('id_met_año').addEventListener('input',function(){
    const id_met_año = this.value
    console.log(id_met_año)
    console.log(id_met_año)

    fetch('/verificar-año/',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
        },
        body: JSON.stringify({ id_met_año: id_met_año })
    })
    .then(response => response.json())
    .then(data => {
        const errorAño = document.getElementById('errorDocumentoExists');
        const botonBloqueado = document.getElementById('submit-second-modal_meta');
        
        if(data.existe){
            errorAño.style.display = 'block';
            botonBloqueado.disabled = true;
        }else{
            errorAño.style.display = 'none';
            botonBloqueado.disabled = false;
        }
    });
});

//verificacion de formulario metas formacion 

$(document).ready(function() {
    $('#id_met_id').change(function() {
        
        var id_met_id = $(this).val();
        console.log('hola',id_met_id)
        if (id_met_id) {
            $.ajax({
                url: url_meta_formacion,
                method: 'GET',
                data: { id_met_id: id_met_id },
                success: function(data) {
                    var select = $('#id_metd_modalidad');
                    select.empty();
                    select.append('<option value="">Selecciona modalidad</option>');
                    $.each(data, function(index, modalidad) {
                        select.append('<option value="' + modalidad.id + '">' + modalidad.modalidad + '</option>');
                    });
                },
                error: function() {
                    alert('Error al cargar las modalidades.');
                }
            });
        } else {
            $('#id_metd_modalidad').empty().append('<option value="">Selecciona modalidad</option>');
        }
    });
});

//fechas inicio y fin 
document.getElementById('id_met_fecha_inicio').addEventListener('change', validateDates);
document.getElementById('id_met_fecha_fin').addEventListener('change', validateDates);

function validateDates() {
    const startDateInput = document.getElementById('id_met_fecha_inicio');
    const endDateInput = document.getElementById('id_met_fecha_fin');
    const errorDiv = document.getElementById('dateErrorMeta');
    const submitButton = document.getElementById('submit-second-modal_meta');

    const startDate = new Date(startDateInput.value);
    const endDate = new Date(endDateInput.value);

    if (startDate && endDate && startDate >= endDate) {
        errorDiv.style.display = 'block';  // Mostrar mensaje de error
        submitButton.disabled = true;      // Desactivar el botón
    } else {
        errorDiv.style.display = 'none';   // Ocultar mensaje de error
        submitButton.disabled = false;     // Activar el botón
    }
}



function Delete_estrategia(button) {
    const pk = button.getAttribute('data-id');
    document.getElementById('deleteForm').action = `/estrategia_institucional/delete/${pk}`;
}
function Editar_estrategia(button){
    const pk = button.getAttribute('data-id');
    const id_est_nombre = button.getAttribute('data-nombre')
    const id_met_id = button.getAttribute('data-meta')
    const id_est_total_meta = button.getAttribute('data-total-meta')

    document.getElementById('editarForm').action = `/estrategia_institucional/edit/${pk}`;
    document.getElementById('id_est_nombre').value = id_est_nombre
    document.getElementById('id_met_id').value = id_met_id
    document.getElementById('id_est_total_meta').value = id_est_total_meta
}

function Delete_meta_estrategia(button) {
    const pk = button.getAttribute('data-id');
    document.getElementById('deleteFormMetaEstrategia').action = `/meta_estrategias_intitucionales/delete/${pk}`;
}
function Editar_meta_estrategia(button){
    const pk = button.getAttribute('data-id');
    const id_est_nombre = button.getAttribute('data-nombre')
    const id_met_id = button.getAttribute('data-meta')
    const id_est_total_meta = button.getAttribute('data-total-meta')

    document.getElementById('editarForm').action = `/estrategia_institucional/edit/${pk}`;
    document.getElementById('id_est_nombre').value = id_est_nombre
    document.getElementById('id_met_id').value = id_met_id
    document.getElementById('id_est_total_meta').value = id_est_total_meta
}
