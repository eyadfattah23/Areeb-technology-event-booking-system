document.addEventListener("DOMContentLoaded", async () => {
    const token = localStorage.getItem("access");

    if (!token) {
        alert("You must be logged in to view events.");
        window.location.href = "/";
        return;
    }

    const headers = {
        "Content-Type": "application/json",
        "Authorization": `JWT ${token}`
    };

    const bookingMap = {};

    try {

        const bookingRes = await fetch("http://127.0.0.1:8000/api/users/me/bookings/", { headers });
        if (!bookingRes.ok) throw new Error("Failed to fetch user bookings");
        const bookings = await bookingRes.json();
        bookings.forEach(b => {
            bookingMap[b.event] = b.id;
        });


        const eventRes = await fetch("http://127.0.0.1:8000/api/events/", { headers });
        if (!eventRes.ok) throw new Error("Failed to fetch events");
        const data = await eventRes.json();
        const events = await getAllEvents(headers);

        const container = document.getElementById("events-container");
        container.innerHTML = "";


        events.forEach(event => {
            const card = document.createElement("div");
            card.className = "event-card";

            const isBooked = bookingMap.hasOwnProperty(event.id);
            const bookingId = bookingMap[event.id];

            const imageHtml = event.img
                ? `<img src="${event.img}" alt="${event.title} image" class="event-image">`
                : `<div class="event-image-placeholder"><i class="fas fa-calendar-alt fa-3x"></i></div>`;

            const categoryLabel = event.category !== "OTH" ? event.category : event.custom_category;
            const priceLabel = event.price > 0 ? `$${event.price}` : "FREE";
            const eventTime = event.time ? ` at ${event.time}` : "";

            card.innerHTML = `
                ${imageHtml}
                <div class="event-content">
                    <h3>${event.title}</h3>
                    <span class="event-category">${categoryLabel}</span>
                    <div class="event-meta">
                        <span class="event-date"><i class="fas fa-calendar"></i> ${event.date}${eventTime}</span>
                        <span class="event-venue"><i class="fas fa-map-marker-alt"></i> ${event.venue}</span>
                    </div>
                    <p class="event-description">${event.description.split(" ").slice(0, 25).join(" ")}...</p>
                    <div class="event-footer">
                        <span class="event-price">${priceLabel}</span>
                        <a href="/events/${event.id}" class="btn-details">View Details</a>
                        <button class="btn-book ${isBooked ? 'booked' : 'book-now'}" 
                                data-event-id="${event.id}" 
                                data-booking-id="${bookingId || ''}">
                            ${isBooked ? 'Booked' : 'Book Now'}
                        </button>
                    </div>
                </div>
            `;

            container.appendChild(card);
        });


        container.addEventListener("click", async (e) => {
            if (!e.target.classList.contains("btn-book")) return;

            const btn = e.target;
            const eventId = btn.dataset.eventId;
            const isBooked = btn.classList.contains("booked");
            const bookingId = btn.dataset.bookingId;

            if (isBooked) {

                const confirmCancel = confirm("Cancel booking?");
                if (!confirmCancel) return;

                const res = await fetch(`http://127.0.0.1:8000/api/bookings/${bookingId}/`, {
                    method: "DELETE",
                    headers
                });

                if (res.ok) {
                    btn.textContent = "Book Now";
                    btn.classList.remove("booked");
                    btn.classList.add("book-now");
                    delete bookingMap[eventId];
                    btn.dataset.bookingId = "";
                } else {
                    alert("Failed to cancel booking.");
                }
            } else {

                const res = await fetch(`http://127.0.0.1:8000/api/events/${eventId}/bookings/`, {
                    method: "POST",
                    headers,
                    body: JSON.stringify({})
                });

                if (res.ok) {
                    const booking = await res.json();
                    btn.textContent = "Booked";
                    btn.classList.remove("book-now");
                    btn.classList.add("booked");
                    bookingMap[eventId] = booking.id;
                    btn.dataset.bookingId = booking.id;
                } else {
                    alert("Failed to book event.");
                }
            }
        });

    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong. Please try again later.");
    }
});


async function getAllEvents(headers) {
    let allEvents = [];
    let nextUrl = "http://127.0.0.1:8000/api/events/";

    while (nextUrl) {
        const response = await fetch(nextUrl, { headers });
        if (!response.ok) throw new Error("Failed to fetch events");

        const data = await response.json();
        allEvents = [...allEvents, ...data.results];
        nextUrl = data.next;
    }

    return allEvents;
}
