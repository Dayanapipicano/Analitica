const total_tecnologo_activos = JSON.parse(document.getElementById('total_tecnologo_activos').textContent)

const tecnologo = document.getElementById('tecnologo').getContext('2d');

new Chart(tecnologo, {
    type: 'bar',
    data: {
        labels: ['Presencial', 'Virtual'],
        datasets: [{
            data: total_tecnologo_activos,
            borderWidth: 1,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
             'rgba(75, 192, 192, 1)',
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
                text: 'Tecnólogo', // Título de la gráfica
                font: {
                    size: 14 // Tamaño de la fuente del título
                }
            }
        }
    }
});



