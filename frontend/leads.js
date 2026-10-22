
const API_URL = "http://127.0.0.1:8000/leads";

const tableBody = document.getElementById("tableBody");
const status = document.getElementById("status");

// Create a table cell and add it to a row.
function addCell(row, text) {
    const cell = document.createElement("td");
    cell.textContent = text;
    row.appendChild(cell);
}

// Fetch enquiries from the FastAPI backend.
async function loadLeads() {
    status.textContent = "Loading...";

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            status.textContent = "Problem loading enquiries";
            return;
        }

        const leads = await response.json();

        tableBody.innerHTML = "";

        for (const lead of leads) {
            const row = document.createElement("tr");

            addCell(row, lead.id);
            addCell(row, lead.name);
            addCell(row, lead.email);
            addCell(row, lead.goal);
            addCell(row, lead.created_at);

            tableBody.appendChild(row);
        }

        status.textContent = leads.length + " enquiries";

    } catch (error) {
        console.error(error);
        status.textContent =
            "Could not reach the server. Is the backend running?";
    }
}

// Reload enquiries when the refresh button is clicked.
document
    .getElementById("refreshBtn")
    .addEventListener("click", loadLeads);

// Load enquiries automatically when this script runs.
loadLeads();
