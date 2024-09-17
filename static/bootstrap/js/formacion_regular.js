  //funcionalidad para tabla, modales y filtros
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#submit-second-modal').addEventListener('click', function(event) {
        event.preventDefault(); // Evita el comportamiento por defecto del botón

        // Selecciona el formulario en el segundo modal
        var form = document.querySelector('#second-modal-form');
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
                document.querySelector('#submit-second-modal').click();

                // Limpia el formulario después de cerrar el modal
                form.reset();
                updateFirstModal(data.meta_id)
            } else {
                // Muestra errores si la respuesta es fallida
                console.log('Error:', data.errors);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

   // Función para actualizar el primer modal
function updateFirstModal(metaId) {
    fetch(`/get_meta/${metaId}/`) // Asegúrate de que la URL coincide con la ruta en tu servidor
        .then(response => response.json())
        .then(data => {
            // Aquí actualizas los campos del primer modal con los datos recibidos
            document.querySelector('#id_met_id').textContent = data.meta_id;
            // Agrega más actualizaciones según sea necesario
        })
        .catch(error => {
            console.error('Error al obtener datos de la meta:', error);
        });
}



});



  //alaertas para el formulario de meta create
  document.getElementById('id_met_año').addEventListener('input',function(){
    const id_met_año = this.value
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
        const botonBloqueado = document.getElementById('submit-second-modal');
        
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
    $(document).on('change','#id_met_id',function() {
        
        
        var id_met_id = $(this).val();
        var $modal = $(this).closest('.modal');


        if (id_met_id) {
            $.ajax({
                url: url_meta_formacion,
                method: 'GET',
                data: { id_met_id: id_met_id },
                success: function(data) {

                    var select = $modal.find('#id_metd_modalidad');
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
    const submitButton = document.getElementById('submit-second-modal');

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


//funcionalidad de eliminar meta formacion
function Delete_meta_formacion(button) {
    console.log(button)
        
    document.getElementById('deleteForm').action = `/meta_formacion/delete/${button}`;
  }
  //funcionalidad de editar meta formacion
  
  function Editar_meta_formacion(button){
    
  
    const pk = button.getAttribute('data-id');
    const id_met_formacion_operario = button.getAttribute('data-operario')
    const id_met_formacion_auxiliar = button.getAttribute('data-auxiliar')
    const id_met_formacion_tecnico = button.getAttribute('data-tecnico')
    const id_met_formacion_profundizacion_tecnica = button.getAttribute('data-profundizacion')
    const id_met_formacion_tecnologo = button.getAttribute('data-tecnologo')
    const id_met_formacion_evento = button.getAttribute('data-evento')
    const id_met_formacion_curso_especial = button.getAttribute('data-curso-especial')
    const id_met_formacion_bilinguismo = button.getAttribute('data-bilinguismo')
    const id_met_formacion_sin_bilinguismo = button.getAttribute('data-sin-bilinguismo')
    const id_met_id = button.getAttribute('data-meta')
    const id_metd_modalidad = button.getAttribute('data-modalidad')
    

    
    document.getElementById('editarFormMetaFormacion').action = `/meta_formacion/edit/${pk}`;
    document.getElementById('id_met_formacion_operario').value = id_met_formacion_operario
    document.getElementById('id_met_formacion_auxiliar').value = id_met_formacion_auxiliar
    document.getElementById('id_met_formacion_tecnico').value = id_met_formacion_tecnico
    document.getElementById('id_met_formacion_profundizacion_tecnica').value = id_met_formacion_profundizacion_tecnica
    document.getElementById('id_met_formacion_tecnologo').value = id_met_formacion_tecnologo
    document.getElementById('id_met_formacion_evento').value = id_met_formacion_evento
    document.getElementById('id_met_formacion_curso_especial').value = id_met_formacion_curso_especial
    document.getElementById('id_met_formacion_bilinguismo').value = id_met_formacion_bilinguismo
    document.getElementById('id_met_formacion_sin_bilinguismo').value = id_met_formacion_sin_bilinguismo
    document.getElementById('id_met_id').value = id_met_id
    document.getElementById('id_metd_modalidad').value = id_metd_modalidad
    
    

    
  }