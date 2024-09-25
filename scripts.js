document.getElementById("arrayForm").onsubmit = function (e) {
    e.preventDefault();
    let size = document.getElementById("arraySize").value;
    generateGraph(size);
};

function generateGraph(size) {
    let mergeSortData = [], hybridSortData = [];
    for (let i = 1000; i <= size; i += 1000) {
        let comparisons = Math.floor(Math.random() * 10000);  // Mock data
        mergeSortData.push({ x: i, y: comparisons });
        hybridSortData.push({ x: i, y: comparisons * 0.9 });  // Hybrid sort performs better
    }

    let data = [
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
