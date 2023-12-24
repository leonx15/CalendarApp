document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/workplaces')
        .then(response => response.json())
        .then(workplaces => {
            const listContainer = document.getElementById('workplaces-list');
            workplaces.forEach(workplace => {
                const item = document.createElement('div');
                item.innerHTML = `<strong>${workplace.name}</strong> - ${workplace.street}, ${workplace.city}`;
                listContainer.appendChild(item);
            });
        })
        .catch(error => console.error('Error:', error));
});