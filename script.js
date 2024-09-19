document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    const nextButtons = {
        'description': document.getElementById('next-to-team'),
        'team': document.getElementById('next-to-algorithms'),
        'algorithms': document.getElementById('next-to-graph'),
        'graph': document.getElementById('next-to-conclusion')
    };

    const showSection = (id) => {
        sections.forEach(section => section.classList.remove('active'));
        document.getElementById(id).classList.add('active');
    };

    Object.keys(nextButtons).forEach(key => {
        nextButtons[key].addEventListener('click', () => showSection(key === 'description' ? 'team' : key === 'team' ? 'algorithms' : key === 'algorithms' ? 'graph' : 'conclusion'));
    });

    const ctx = document.getElementById('graph-canvas').getContext('2d');
    let chart = null;

    document.getElementById('generate-graph').addEventListener('click', () => {
        const size = parseInt(document.getElementById('array-size').value, 10);
        const threshold = parseInt(document.getElementById('threshold').value, 10);

        if (!size || !threshold) {
            alert('Please enter valid values for array size and threshold.');
            return;
        }

        const data = generateGraphData(size, threshold);

        if (chart) chart.destroy();

        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.sizes,
                datasets: [{
                    label: 'Key Comparisons',
                    data: data.comparisons,
                    borderColor: '#3498db',
                    backgroundColor: 'rgba(52, 152, 219, 0.2)',
                    borderWidth: 2
                }]
            },
            options: {
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Array Size'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Key Comparisons'
                        },
                        suggestedMax: Math.max(...data.comparisons) * 1.1
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: (tooltipItem) => `Size: ${tooltipItem.label}, Comparisons: ${tooltipItem.raw}`
                        }
                    }
                }
            }
        });

        document.getElementById('conclusion-text').innerText = 
            `The graph above shows the number of key comparisons performed by the hybrid sorting algorithm for an array of size ${size} with a threshold of ${threshold}.`;
    });

    const generateGraphData = (size, threshold) => {
        // Simulate data generation for the graph
        // Replace this with actual algorithm data in a real-world scenario
        const sizes = [size];
        const comparisons = [Math.random() * 1000];
        return { sizes, comparisons };
    };
});
