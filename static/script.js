// Datos para el gráfico (pueden venir de PHP con AJAX o directamente como aquí)
const ctx = document.getElementById('ventasChart').getContext('2d');

const ventasChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Ventas por mes',
            data: [12, 19, 3, 5, 2],
            backgroundColor: '#3498db'
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
        }
    }
});