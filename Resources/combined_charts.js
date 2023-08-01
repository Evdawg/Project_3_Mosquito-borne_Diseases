// Function to fetch the CSV data and create the multi-line chart for temperature
async function createTemperatureChart() {
    // Fetch the CSV data using fetch API
    const response = await fetch('Data/temp_data.csv');
    const csvData = await response.text();

    // Parse the CSV data into an array of objects
    const dataArray = csvData.split('\n').map(row => row.split(','));
    const headers = dataArray.shift();
    const data = dataArray.map(row => {
        const county = row[0];
        const state = row[1];
        const values = row.slice(2, 23).map(val => parseFloat(val));
        return { county, state, values };
    });

    // Get years from headers
    const years = headers.slice(2, 23);

    // Group data by state
    const groupedData = data.reduce((acc, entry) => {
        if (!acc[entry.state]) {
            acc[entry.state] = [];
        }
        acc[entry.state].push(entry);
        return acc;
    }, {});

    // Create separate datasets for each state
    const datasets = Object.entries(groupedData).map(([state, counties]) => {
        return {
            label: state,
            data: counties.map(entry => entry.values),
            borderColor: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 1)`,
            fill: false,
            lineTension: 0,
        };
    });

    // Create the multi-line chart using Chart.js
    const ctx = document.getElementById('temperatureChart').getContext('2d');
    const lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: years,
            datasets: datasets,
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Year',
                    },
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Temperature (F) 3 Month Summer Average',
                    },
                },
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Temperature by County Grouped by State',
                },
            },
        },
    });
}

// Function to fetch the CSV data and create the multi-line chart for West Nile Virus
async function createWestNileChart() {
    // Fetch the CSV data using fetch API
    const response = await fetch('Data/WN_data_vis.csv');
    const csvData = await response.text();

    // Parse the CSV data into an array of objects
    const dataArray = csvData.split('\n').map(row => row.split(','));
    const headers = dataArray.shift();
    const data = dataArray.map(row => {
        const county = row[0];
        const state = row[1];
        const values = row.slice(2, 22).map(val => parseInt(val));
        return { county, state, values };
    });

    // Get years from headers
    const years = headers.slice(2, 22);

    // Group data by state
    const groupedData = data.reduce((acc, entry) => {
        if (!acc[entry.state]) {
            acc[entry.state] = [];
        }
        acc[entry.state].push(entry);
        return acc;
    }, {});

    // Create separate datasets for each state
    const datasets = Object.entries(groupedData).map(([state, counties]) => {
        return {
            label: state,
            data: counties.map(entry => entry.values),
            borderColor: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 1)`,
            fill: false,
            lineTension: 0,
        };
    });

    // Create the multi-line chart using Chart.js
    const ctx = document.getElementById('westNileChart').getContext('2d');
    const lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: years,
            datasets: datasets,
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Year',
                    },
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'West Nile Virus Cases',
                    },
                },
            },
            plugins: {
                title: {
                    display: true,
                    text: 'West Nile Virus Cases by County Grouped by State',
                },
            },
        },
    });
}

// Function to fetch the CSV data and create the multi-line chart for Lyme Disease
async function createLymeDiseaseChart() {
    // Fetch the CSV data using fetch API
    const response = await fetch('Data/LD_data.csv');
    const csvData = await response.text();

    // Parse the CSV data into an array of objects
    const dataArray = csvData.split('\n').map(row => row.split(','));
    const headers = dataArray.shift();
    const data = dataArray.map(row => {
        const county = row[0];
        const state = row[1];
        const values = row.slice(4, 24).map(val => parseInt(val));
        return { county, state, values };
    });

    // Get years from headers
    const years = headers.slice(4, 24);

    // Group data by state
    const groupedData = data.reduce((acc, entry) => {
        if (!acc[entry.state]) {
            acc[entry.state] = [];
        }
        acc[entry.state].push(entry);
        return acc;
    }, {});

    // Create separate datasets for each state
    const datasets = Object.entries(groupedData).map(([state, counties]) => {
        return {
            label: state,
            data: counties.map(entry => entry.values),
            borderColor: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 1)`,
            fill: false,
            lineTension: 0,
        };
    });

    // Create the multi-line chart using Chart.js
    const ctx = document.getElementById('lymeDiseaseChart').getContext('2d');
    const lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: years,
            datasets: datasets,
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Year',
                    },
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Lyme Disease Cases',
                    },
                },
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Lyme Disease Cases by County Grouped by State',
                },
            },
        },
    });
}

// Function to fetch the CSV data and create the multi-line chart for Precipitation
async function createPrecipitationChart() {
    // Fetch the CSV data using fetch API
    const response = await fetch('Data/precip_data.csv');
    const csvData = await response.text();

    // Parse the CSV data into an array of objects
    const dataArray = csvData.split('\n').map(row => row.split(','));
    const headers = dataArray.shift();
    const data = dataArray.map(row => {
        const county = row[0];
        const state = row[1];
        const values = row.slice(2, 22).map(val => parseFloat(val));
        return { county, state, values };
    });

    // Get years from headers
    const years = headers.slice(2, 22);

    // Group data by state and calculate the average precipitation for each state
    const groupedData = data.reduce((acc, entry) => {
        if (!acc[entry.state]) {
            acc[entry.state] = {
                state: entry.state,
                values: Array(years.length).fill(0),
                count: 0,
            };
        }
        entry.values.forEach((val, index) => {
            acc[entry.state].values[index] += val;
        });
        acc[entry.state].count++;
        return acc;
    }, {});

    // Calculate the average precipitation for each state
    Object.values(groupedData).forEach(stateData => {
        stateData.values = stateData.values.map(val => val / stateData.count);
        delete stateData.count;
    });

    // Create a single dataset for each state
    const datasets = Object.values(groupedData).map(stateData => {
        return {
            label: stateData.state,
            data: stateData.values,
            borderColor: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 1)`,
            fill: false,
            lineTension: 0,
        };
    });

    // Create the multi-line chart using Chart.js

    const ctx = document.getElementById('precipitationChart').getContext('2d');
    const lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: years,
            datasets: datasets,
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Year',
                    },
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Precipitation (in) 3 Month Summer Average',
                    },
                },
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Precipitation by County Grouped by State',
                },
            },
        },
    });
}

// Call the functions to fetch data and create the multi-line charts
createTemperatureChart();
createWestNileChart();
createLymeDiseaseChart();
createPrecipitationChart();
createTemperatureChart();