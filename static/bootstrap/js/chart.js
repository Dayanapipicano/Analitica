
//GRAFICA TITULADA
//datos del p04
const data = JSON.parse(document.getElementById('data').textContent)

const labels_virtuales = JSON.parse(document.getElementById('labels_virtuales').textContent)
const labels_presenciales = JSON.parse(document.getElementById('labels_presenciales').textContent)
// datos de las metas establecidas
const metas_valores = JSON.parse(document.getElementById('metas_valores').textContent)


//GRAFICA COMPLEMENTARIA 
const bilinguismo_activos_virtual = JSON.parse(document.getElementById('bilinguismo_activos_virtual').textContent)
const bilinguismo_activos_data_presencial = JSON.parse(document.getElementById('bilinguismo_activos_data_presencial').textContent)

const sin_bilinguismo_activos_data_virtual = JSON.parse(document.getElementById('sin_bilinguismo_activos_data_virtual').textContent)
const sin_bilinguismo_activos_data_presencial = JSON.parse(document.getElementById('sin_bilinguismo_activos_data_presencial').textContent)
//METAS



//funcion de cambiar las graficas
function showChart(chartId,tableId) {
    // Oculta todos los gráficos
    document.querySelectorAll('.chart').forEach(chart => {
        chart.style.display = 'none';
    });
    // Muestra el gráfico seleccionado
    document.getElementById(chartId).style.display = 'block';
    // Oculta todos las tablas
    document.querySelectorAll('.data-table').forEach(table => {
        table.style.display = 'none';
    });
    document.getElementById(tableId).style.display = 'block';

}

function Estado_de_color(value, max){
    const porcentaje = value / max;
    if(porcentaje <0.29) return 'rgba(255, 99, 132, 0.2)';
    if(porcentaje <0.49) return 'rgba(255, 159, 64, 0.2)';
    if(porcentaje <0.59) return 'rgba(255, 206, 86, 0.2)';
    return 'rgba(75, 192, 192, 0.2)';
}

//porcentajes metas titulada
const backgroundColors = metas_valores.map((meta, index) => {
    const resultado = data[index];
    return Estado_de_color(resultado, meta)
})
const borderColor = metas_valores.map((meta, index) => {
    const resultado = data[index];
    return Estado_de_color(resultado, meta).replace('0.2','1.0')
})

//porcentaje metas complementaria

const ctx_titulada = document.getElementById('barchart_titulada').getContext('2d');

new Chart(ctx_titulada, {
    type: 'bar',
    data: { 
        labels: [labels_presenciales[0],labels_presenciales[1],labels_presenciales[2],labels_presenciales[3],labels_presenciales[4],labels_presenciales[5],labels_virtuales[0],labels_virtuales[1],labels_virtuales[2],labels_virtuales[3],labels_virtuales[4],labels_virtuales[5],labels_virtuales[6]],
        datasets: [{
            label: '# de Aprendices',
            data: data,
            borderWidth: 1,
            backgroundColor: backgroundColors,
            borderColor:borderColor ,
        }
    ],
    },
    options: {
        scales: {
            x: {
                stacked: false,
                grid: {
                    display : false
                },
                sticks: {
                    autoSkip: false,
                    maxRotation: 90

                }

            },
            y: {
                beginAtZero: true,
                min:0,
                ticks: {
                    stepSize: 20,
                    callback: function(value){
                       
                        return value 
                    }
                }
            
            },
          
        },
        plugins: {
            legend: {
                display: false // Ocultar la leyenda
            },
            title: {
                display: true, // Mostrar el título
                text: 'Titulada', // Título de la gráfica
                font: {
                    size: 14 // Tamaño de la fuente del título
                }
            },
            
        }
    }
});





//COMPLEMENTARIA
const ctx_complementaria = document.getElementById('barchart_complementaria').getContext('2d');

new Chart(ctx_complementaria, {
    width: 100,
    type: 'bar',
    data:  {
    
        labels: ['Bilingüismo Presencial', 'Bilingüismo Virtual', 'Sin Bilingüismo Presencial', 'Sin Bilingüismo Virtual'],
     
        datasets: [{
            label: '# of Votes',
            data: [bilinguismo_activos_data_presencial, bilinguismo_activos_virtual, sin_bilinguismo_activos_data_presencial, sin_bilinguismo_activos_data_virtual],
            borderWidth: 1,
           
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ]
        }]
    },
    options: {
      
        scales: {
            
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                display: false // Ocultar la leyenda
            },
            title: {
                display: true, // Mostrar el título
                text: 'Complementaria', // Título de la gráfica
                font: {
                    size: 14 // Tamaño de la fuente del título
                }
            }
        }
    },
  
});