// Performance data
const mergeSortData = [300, 500, 700, 900, 1100];
const insertionSortData = [200, 400, 600, 800, 1000];
const hybridSortData = [150, 350, 550, 750, 950];

const ctx = document.getElementById('comparisonChart').getContext('2d');
const comparisonChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['1000', '2000', '3000', '4000', '5000'],
        datasets: [
            {
                label: 'Merge Sort',
                data: mergeSortData,
                borderColor: '#f54242',
                fill: false,
                tension: 0.1,
            },
            {
                label: 'Insertion Sort',
                data: insertionSortData,
                borderColor: '#4287f5',
                fill: false,
                tension: 0.1,
            },
            {
                label: 'Hybrid Sort',
                data: hybridSortData,
                borderColor: '#42f57d',
                fill: false,
                tension: 0.1,
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            tooltip: {
                enabled: true,
                callbacks: {
                    label: function(tooltipItem) {
                        return `Key Comparisons: ${tooltipItem.raw}`;
                    }
                }
            }
        },
        interaction: {
            mode: 'nearest',
            axis: 'x',
            intersect: false,
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Array Size',
                    color: '#c5c6c7',
                    font: {
                        size: 16,
                    }
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Key Comparisons',
                    color: '#c5c6c7',
                    font: {
                        size: 16,
                    }
                }
            }
        }
    }
});
