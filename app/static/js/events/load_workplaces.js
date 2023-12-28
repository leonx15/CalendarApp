document.addEventListener('DOMContentLoaded', function() {
    // Fetch workplaces and populate the dropdown
    fetch('/api/workplaces')
        .then(response => response.json())
        .then(workplaces => {
            const dropdown = document.getElementById('workplaceDropdown');
            workplaces.forEach(workplace => {
                if (workplace.active) {
                    const option = document.createElement('option');
                    option.value = workplace.id;
                    option.textContent = workplace.name;
                    dropdown.appendChild(option);
                }
            });
        })
        .catch(error => {
            console.error('Error fetching workplaces:', error);
            // Handle errors in fetching workplaces
        });
});