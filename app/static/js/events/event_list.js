document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/events')
        .then(response => response.json())
        .then(workplaces => {
            const listContainer = document.getElementById('events-list');
            workplaces.forEach(workplace => {
                const item = document.createElement('div');
                item.innerHTML = `<strong>${event.name}</strong> - ${event.start_date}, ${event.end_date}`;
                listContainer.appendChild(item);
            });
        })
        .catch(error => console.error('Error:', error));
});