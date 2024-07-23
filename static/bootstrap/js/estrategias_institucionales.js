//Seleccionar año 
function Ano(){
    var n = (new Date()).getFullYear()
    var select = document.getElementById("ano");
    for(var i = n; i>=1900; i--)select.options.add(new Option(i,i));

};
window.onload = Ano;





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
        const metaSelect = document.querySelector('select[name="met_id"]');
        const totalMetaField = document.querySelector('input[name="est_total_meta"]');
    
        metaSelect.addEventListener('change', function() {
            const selectedMetaId = metaSelect.value;
            fetchMetaValues(selectedMetaId);
        });
    
        function fetchMetaValues(metaId) {
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
    const estrategiaField = document.querySelector('select[name="est_id"]');
    const modalidadField = document.querySelector('input[name="estd_modalidad"]');
    const metaField = document.querySelector('input[name="estd_meta"]');

    estrategiaField.addEventListener('change', function () {
       
        const est_id = estrategiaField.value;
        fetch(`/get_estrategia_data/${est_id}/`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                modalidadField.value = data.est_modalidad || '';
                metaField.value = data.met_id || '';
            });
    });
});