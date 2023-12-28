document.getElementById('addEventForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const jsonData = Object.fromEntries(formData.entries());

    fetch('/api/add_event', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Include other headers if necessary (e.g., for authentication)
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Event added:', data);
        window.location.href = '../event/';
        // Handle success, e.g., redirect to the events list or show a success message
    })
    .catch(error => {
        console.error('Error adding event:', error);
        // Handle errors in adding the event
    });
});