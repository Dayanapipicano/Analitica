
const data_values = JSON.parse(document.getElementById('data_values').textContent)


function showChart(chartId) {
    // Oculta todos los gráficos
    document.querySelectorAll('.chart').forEach(chart => {
        chart.style.display = 'none';
    });
    // Muestra el gráfico seleccionado
    document.getElementById(chartId).style.display = 'block';
}
const ctx_titulada = document.getElementById('barchart_titulada').getContext('2d');

new Chart(ctx_titulada, {
    type: 'bar',
    data: {
        labels: ['Curso especial/Presencial', 'Tecnologo/Presencial', 'Tecnico/Presencial', 'Auxiliar/Presencial', 'Operario/Presencial', 'Evento/Presencial', 'Virtual', 'Presencial', 'Virtual', 'Presencial', 'Virtual', 'Presencial', 'Virtual', 'Presencial'],
        datasets: [{
            label: '# de Aprendices',
            data: data_values,
            borderWidth: 1,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 159, 64, 0.2)'
              
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255, 159, 64, 1)'
             
              
            ]
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                min:0,
                ticks: {
                    stepSize: 20,
                    callback: function(value){
                       
                        return value 
                    }
                }
            
            }
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



const ctx_complementaria = document.getElementById('barchart_complementaria').getContext('2d');


const customPlugin = {
    id: 'customPlugin',
    
    afterDraw: (chart) => {
        const ctx = chart.ctx;
        ctx.save();
        const xAxis = chart.scales.x;
        const yAxis = chart.scales.y;

        // Set the font for the custom labels
        ctx.font = '14px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        
          

        // Define the custom labels and their positions
        const customLabels = ['Estrategia 1', 'Estrategia 2', 'Estrategia 3', 'Estrategia 4', 'Estrategia 5', 'Estrategia 6', 'Estrategia 7'];
        const labelPositions = xAxis.getPixelForTick(1); // Get position for the first pair

        // Loop through the labels and draw them at the correct positions
        customLabels.forEach((label, index) => {
            const posX = xAxis.getPixelForTick(index * 2 + 1);
            ctx.fillText(label, posX, yAxis.bottom + 25);
          
        });

        ctx.restore();
    }
};
new Chart(ctx_complementaria, {
    width: 100,
    type: 'bar',
    data:  {
    
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
     
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
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
    plugins: [customPlugin],
});

