// Check if Leaflet is loaded
if (typeof L === 'undefined') {
    console.error('Leaflet library is not loaded. Ensure the Leaflet script is included before map.js.');
} else {
    // Initialize the map
    const map = L.map('map').setView([51.505, -0.09], 13); // Center on London for demo

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

    // Fallback data in case fetch fails
    const fallbackData = [
        { id: 1, lat: 51.505, lng: -0.09, status: 'working' },
        { id: 2, lat: 51.507, lng: -0.085, status: 'not working' },
        { id: 3, lat: 51.503, lng: -0.095, status: 'working' },
        { id: 4, lat: 51.506, lng: -0.088, status: 'not working' }
    ];

    // Function to add markers
    function addMarkers(streetLights) {
        streetLights.forEach(light => {
            const icon = light.status === 'working' ? workingIcon : notWorkingIcon;
            L.marker([light.lat, light.lng], { icon: icon })
                .addTo(map)
                .bindPopup(`Street Light ID: ${light.id}<br>Status: ${light.status}`);
        });
    }

    // Fetch street light data
    fetch('data/streetLights.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(streetLights => {
            console.log('Street Lights Data:', streetLights); // Debug log
            addMarkers(streetLights);
        })
        .catch(error => {
            console.error('Error loading street light data:', error);
            console.warn('Using fallback data due to fetch failure.');
            addMarkers(fallbackData); // Use fallback data if fetch fails
        });
}