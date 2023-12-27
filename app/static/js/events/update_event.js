document.addEventListener('DOMContentLoaded', function() {
    // Fetch workplaces and populate the dropdown
    fetch('/api/workplaces')
        .then(response => response.json())
        .then(workplaces => {
            const dropdown = document.getElementById('workplaceDropdown');
            workplaces.forEach(workplace => {
                const option = document.createElement('option');
                option.value = workplace.id;
                option.textContent = workplace.name;
                dropdown.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching workplaces:', error);
            // Handle errors in fetching workplaces
        });

    // Handle event form submission
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
});