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
    const modalidadField = document.querySelector('#id_estd_modalidad');
    const estrategiaField = document.querySelector('#id_est_id');
    const metaField = document.querySelector('#id_estd_meta');

    modalidadField.addEventListener('change', function () {
        const id_estd_modalidad = this.value;

        fetch(`/get_estrategia_data/${id_estd_modalidad}/`)
            .then(response => response.json())
            .then(data => {
                console.log(data); 
                estrategiaField.innerHTML = '<option value"">selecionar</option>'

            
                data.estrategia.forEach(estrategia => {
                    const option = document.createElement('option');
                    option.value = estrategia.estrategia_id;
                    option.textContent = estrategia.estrategia_nombre;
                    estrategiaField.appendChild(option);

                    // Selecciona la opción recién añadida
                    estrategiaField.value = data.estrategia_id;
                })
                  
            
                
                

            });
    });

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
                    option.textContent = meta.met_codigo;
                    metaField.appendChild(option)


            }
            
      
            

        })
    })
});


//detalle de metas para cada registro de estrategias detalle
document.addEventListener('DOMContentLoaded', function () {
    const boton = document.querySelectorAll('[data-toggle="modal"');
    boton.forEach(boton =>{
        boton.addEventListener("click", () => {
            const estd_meta = this.getAttribute('data-id');
            fetch(`/meta_detalle/${estd_meta}/`)
            .then(response => response.json())
            .then(data =>{
                document.getElementById('fiel_codigo').textContent = data.met_codigo
            })
        })

    })
    
})