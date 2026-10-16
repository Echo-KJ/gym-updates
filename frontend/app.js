
const API_URL = "http://127.0.0.1:8000/leads";

const button = document.getElementById("sendBtn");
const message = document.getElementById("message");

button.addEventListener("click", sendEnquiry);

async function sendEnquiry() {
    const lead = {
        name: document.getElementById("name").value.trim(),
        email: document.getElementById("email").value.trim(),
        goal: document.getElementById("goal").value.trim()
    };

    // 1. Check for empty fields
    if (!lead.name || !lead.email || !lead.goal) {
        message.textContent = "Please fill in all fields.";
        return;
    }

    // 2. Prevent repeated submissions
    button.disabled = true;
    message.textContent = "Sending enquiry...";

    try {
        // 3. Send the request to the backend
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(lead)
        });

        // 4. Read the backend response
        const data = await response.json();

        // 5. Display the result
        if (response.ok) {
            message.textContent =
                "Success: " + (data.message || "Enquiry received");
        } else if (data.detail) {
            message.textContent = "Problem: " +
                (typeof data.detail === "string"
                    ? data.detail
                    : "Please check your submitted data.");
        } else {
            message.textContent =
                "Problem: Request failed with status " + response.status;
        }

    } catch (error) {
        message.textContent =
            "Could not reach the server. Is the backend running?";

    } finally {
        // 6. Re-enable the button
        button.disabled = false;
    }
}
