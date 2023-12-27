document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/events')
        .then(response => response.json())
        .then(events => {
            const listContainer = document.getElementById('events-list');
            events.forEach(event => {
                const item = document.createElement('div');
                const editUrl = `/event/update/${event.id}`;
                item.innerHTML = `<a href="${editUrl}"><strong>${event.name}</strong></a> - ${event.start_date}, ${event.end_date}`;
                listContainer.appendChild(item);
            });
        })
        .catch(error => console.error('Error:', error));
});