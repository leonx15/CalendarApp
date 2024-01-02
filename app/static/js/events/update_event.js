document.getElementById('updateEventForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const eventId = document.getElementById('updateEventForm').getAttribute('data-event-id');
    const formData = new FormData(this);
    const jsonData = Object.fromEntries(formData.entries());
    const url = `/api/edit_event/${eventId}`;
    const urlBack = `/event`;

    fetch(url, {
        method: 'PUT',
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
        console.log(data);
        // Handle success
        window.location.href = urlBack;
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors
    });
});

//DELETE EVENT
document.getElementById('deleteEventButton').addEventListener('click', function() {
    const eventId = this.getAttribute('data-event-id');
    if (confirm('Jesteś pewien że chcesz usunąć to wydarzenie? Operacja jest nieodwracalna.')) {
        fetch("/api/delete_event/" + eventId, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '/event'; // Redirect to the events list
            } else {
                alert('Error deleting event');
            }
        })
        .catch(error => console.error('Error:', error));
    }
});