function generateGraph() {
    const arraySize = parseInt(document.getElementById('array-size').value);
    const threshold = parseInt(document.getElementById('threshold').value);

    const data = generateDummyData(arraySize);

    const ctx = document.getElementById('myChart').getContext('2d');
    if (window.myChart) {
        window.myChart.destroy(); // Destroy previous chart to avoid overlap
    }
    
    window.myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'MergeSort',
                    data: data.mergeSortData,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    fill: false
                },
                {
                    label: 'Insertion Sort',
                    data: data.insertionSortData,
                    borderColor: 'rgba(54, 162, 235, 1)',
                    fill: false
                },
                {
                    label: 'Hybrid Sort',
                    data: data.hybridSortData,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    beginAtZero: true,
                    max: arraySize + arraySize * 0.1 // 10% more than input value
                },
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                tooltip: {
                    mode: 'index',
                    intersect: false
                },
                zoom: {
                    pan: {
                        enabled: true,
                        mode: 'x'
                    },
                    zoom: {
                        enabled: true,
                        mode: 'x',
                        sensitivity: 3
                    }
                }
            },
            hover: {
                mode: 'nearest',
                intersect: true
            }
        }
    });
}

function generateDummyData(arraySize) {
    const labels = [];
    const mergeSortData = [];
    const insertionSortData = [];
    const hybridSortData = [];

    for (let i = 0; i < arraySize; i += Math.floor(arraySize / 100)) {
        labels.push(i);
        mergeSortData.push(Math.log(i + 1) * i); // Dummy data for merge sort
        insertionSortData.push(i * i); // Dummy data for insertion sort
        hybridSortData.push((Math.log(i + 1) * i) + i); // Dummy data for hybrid sort
    }

    return {
        labels,
        mergeSortData,
        insertionSortData,
        hybridSortData
    };
}
