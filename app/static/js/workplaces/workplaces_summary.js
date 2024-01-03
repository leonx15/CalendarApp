document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('workplaceSummaryForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevents the default form submission behavior

            const month = document.getElementById('month').value;
            const year = document.getElementById('year').value;
            const tableBody = document.getElementById('workplaceSummaryTableBody');

            // Clear previous table content
            while (tableBody.firstChild) {
                tableBody.removeChild(tableBody.firstChild);
            }

            // Fetch data from the API
            fetch('/api/workplace-summary?month=' + month + '&year=' + year)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.workplace_summaries.length === 0) {
                        const row = tableBody.insertRow();
                        const cell = row.insertCell(0);
                        cell.textContent = 'No data available for this period.';
                        cell.colSpan = 2;
                    } else {
                        data.workplace_summaries.forEach(summary => {
                            const row = tableBody.insertRow();
                            const nameCell = row.insertCell(0);
                            nameCell.textContent = summary.name;

                            const durationCell = row.insertCell(1);
                            durationCell.textContent = summary.total_duration_hours.toFixed(2);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    const row = tableBody.insertRow();
                    const cell = row.insertCell(0);
                    cell.textContent = 'Error loading data.';
                    cell.colSpan = 2;
                });
        });
    } else {
        console.error('Form not found');
    }
});
