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

//funcionalidad de eliminar meta formacion
function Delete_meta_formacion(button) {
  console.log(button)
      
  document.getElementById('deleteForm').action = `/meta_formacion/delete/${button}`;
}
//funcionalidad de editar meta formacion

function Editar_meta_formacion(button){
  

  const pk = button.getAttribute('data-id');
  const met_formacion_auxiliar = button.getAttribute('data-nombre')
  
  
  document.getElementById('editarForm').action = `/modalidad/edit/${pk}`;
  var res = document.getElementById('id_met_formacion_auxiliar').value = met_formacion_auxiliar
  
  console.log(res)
  
}

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


