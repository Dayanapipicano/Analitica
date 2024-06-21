const ctx = document.getElementById('barchart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
        backgroundColor : [
            'rgba(255,99,132,0.2)',
            'rgba(54,162,235,0.2)',
            'rgba(255,99,132,0.2)',
            'rgba(255,99,132,0.2)',
            'rgba(255,99,132,0.2)',
        ],
        borderColor:[
            'rgba(255,99,132,0.2)',
        ]
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });