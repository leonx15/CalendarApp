document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth', // Sets the initial view to month grid
            events: '../api/events_for_calendar',
            locale: 'pl'
            // Add other options here
        });
        calendar.render();
});