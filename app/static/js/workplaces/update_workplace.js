document.getElementById('updateWorkplaceForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const workplaceId = document.getElementById('updateWorkplaceForm').getAttribute('data-workplace-id');
    const formData = new FormData(this);
    const jsonData = Object.fromEntries(formData.entries());
    const url = `/api/edit_workplace/${workplaceId}`;
    const urlBack = `/workplace`;

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
