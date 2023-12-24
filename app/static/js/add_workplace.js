document.getElementById('addWorkplaceForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const jsonData = Object.fromEntries(formData.entries());

    fetch('../api/add_workplace', {
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
        console.log(data);
        // Handle success
        window.location.href = '../workplace/';
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors
    });
});