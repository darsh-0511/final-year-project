if (typeof L === 'undefined') {
    console.error('Leaflet library is not loaded. Ensure the Leaflet script is included before map.js.');
} else {
    // Initialize the map with Bengaluru, Karnataka, India
    const map = L.map('map').setView([12.9716, 77.5946], 13); // Center on Bengaluru

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Custom icons for working and not working street lights
    const workingIcon = L.divIcon({
        className: 'working-icon',
        html: '<div style="background-color: green; width: 10px; height: 10px; border-radius: 50%;"></div>',
        iconSize: [10, 10]
    });

    const notWorkingIcon = L.divIcon({
        className: 'not-working-icon',
        html: '<div style="background-color: red; width: 10px; height: 10px; border-radius: 50%;"></div>',
        iconSize: [10, 10]
    });

    // Function to add markers
    function addMarkers(streetLights) {
        streetLights.forEach(light => {
            const icon = light.status === 'working' ? workingIcon : notWorkingIcon;
            L.marker([light.lat, light.lng], { icon: icon })
                .addTo(map)
                .bindPopup(`Street Light ID: ${light.id}<br>Status: ${light.status}`);
        });
    }

    // Function to fetch street light data from server
    async function fetchStreetLightData() {
        try {
            // Fetch from Flask server
            const response = await fetch('http://localhost:5000/streetlights', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const streetLights = await response.json();
            console.log('Street Lights Data:', streetLights);

            // Validate data format
            if (!Array.isArray(streetLights) || !streetLights.every(light => 
                'id' in light && 'lat' in light && 'lng' in light && 'status' in light)) {
                throw new Error('Invalid data format received from server');
            }

            addMarkers(streetLights);
        } catch (error) {
            console.error('Fetch failed');
        }
    }

    // Call the fetch function to load data
    fetchStreetLightData();
}