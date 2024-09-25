document.getElementById("arrayForm").onsubmit = function (e) {
    e.preventDefault();
    let size = document.getElementById("arraySize").value;
    generateGraph(size);
};

function generateGraph(size) {
    let mergeSortData = [], hybridSortData = [], insertionSortData = [];

    for (let i = 1000; i <= size; i += 100000) {  // Adjust step to avoid too many points
        let insertionComparisons = Math.floor(Math.pow(i, 2) * 0.0001);  // Mock Insertion Sort
        let mergeComparisons = Math.floor(i * Math.log2(i));  // Mock Merge Sort
        let hybridComparisons = Math.floor(mergeComparisons * 0.9);  // Hybrid sort improves on merge

        insertionSortData.push({ x: i, y: insertionComparisons });
        mergeSortData.push({ x: i, y: mergeComparisons });
        hybridSortData.push({ x: i, y: hybridComparisons });
    }

    let data = [
        {
            x: insertionSortData.map(point => point.x),
            y: insertionSortData.map(point => point.y),
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Insertion Sort'
        },
        {
            x: mergeSortData.map(point => point.x),
            y: mergeSortData.map(point => point.y),
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Merge Sort'
        },
        {
            x: hybridSortData.map(point => point.x),
            y: hybridSortData.map(point => point.y),
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Hybrid Sort'
        }
    ];

    Plotly.newPlot('graph', data);
}
