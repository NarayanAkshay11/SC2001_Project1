function generateGraph() {
    const arraySize = document.getElementById('array-size').value;
    const data = generateDummyData(arraySize);

    const ctx = document.getElementById('comparisonChart').getContext('2d');
    new Chart(ctx, {
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
            plugins: {
                tooltip: {
                    mode: 'index',
                    intersect: false
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
        mergeSortData.push(Math.log(i + 1) * 100);  // Simulated data
        insertionSortData.push(i * i / 1000);       // Simulated data
        hybridSortData.push(Math.sqrt(i) * 100);    // Simulated data
    }

    return {
        labels,
        mergeSortData,
        insertionSortData,
        hybridSortData
    };
}

