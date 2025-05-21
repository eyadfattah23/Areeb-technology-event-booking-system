# EventHub – Event Booking System

![EventHub Dashboard](/static/images/screenshot.png)
![EventHub Event Page](/static/images/image.png)
![EventHub Booking Page](/static/images/image1.png)

## 📌 Overview

EventHub is a full-stack event booking platform that lets users discover, book, and manage events, while administrators get a robust dashboard for managing events and users. It’s powered by Django REST Framework (DRF) on the backend and vanilla JavaScript on the frontend.

- **Secure JWT authentication** (Djoser + Simple JWT)  
- **Responsive event listings** with filtering, search, and sorting  
- **One-click booking engine** for attendees  
- **Admin panel** with full CRUD for events and user management  
- **RESTful JSON API** for future integrations

## ✨ Key Features

### 🔐 Authentication
- User registration with email, password + password re-type  
- JWT-based login, refresh & verify  
- Role-based access control (User vs. Admin)  
- `HIDE_USERS = True`: non-admins can only see their own user record

### 🎪 Event Management
- **Listing**: filter by category, date range, price; search by title/description; sort by price, date or popularity  
- **Creation & Editing**: admin (or event creator) can create, update, or delete events  
- **Annotations**: each event shows `number_of_bookings` and `is_booked` (for the current user)

### 🎟 Booking Engine
- **Book / unbook** events with a single POST/DELETE  
- **My Bookings** endpoint for users to view their bookings  
- **Event-specific bookings** list for admins or the event’s creator

### 🛠 Admin Panel
- Full CRUD on events  
- View and manage user list (all users if admin)  
- Handle booking records

## 🚀 Tech Stack

| Layer       | Technologies                  |
| ----------- | ----------------------------- |
| **Backend** | Django 5.2, DRF 3.16, MySQL   |
| **Auth**    | Djoser, Simple JWT            |
| **Frontend**| Vanilla JavaScript, HTML5, CSS3 |
| **DevTools**| django-debug-toolbar, django-filter |

---

## ⚙️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/eyadfattah23/Areeb-technology-event-booking-system.git
   cd Areeb-technology-event-booking-system
    ```
2. **install python3 and pip3 if not already installed** (Ubuntu example)
    ```bash
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y python3.10 python3.10-venv python3.10-dev

    python3 --version
    ```


3. **install mysql**
Follow instructions at: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04


4. **Set up database**

* Create a user & database matching `setupDB.sql`
* Run:
    ```bash
    cat setupDB.sql | sudo mysql -u root -p
    ```

* (Optional) Load mock data:

    ```bash
    unzip areeb_event_sys_dev_db.zip
    mysql -u areeb_event_sys_dev -p areeb_event_sys_dev_db < load.sql
    # or use root user
    ```

5. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source env/bin/activate
   ```

6. **Install the required packages**:
   ```bash
   pip3 install -r requirements.txt
   ```


7. **Run migrations**:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```


8. **Create a superuser**
   ```bash
   python3 manage.py createsuperuser
   ```
9. **Start the server**
   ```bash
   python3 manage.py runserver
   ```
10. **Access**
    * Admin panel: http://localhost:8000/admin/

    * API root: http://localhost:8000/api/

    * Auth root: http://localhost:8000/auth/


> **Tip:** Open your web browser and navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) then login using the credentials you used with the command `python3.10 manage.py createsuperuser`
> **Note:** Use Postman or the DRF web UI rather than raw curl commands for easier testing.


### 11. Run the application


### Steps after Running the Application
#### a. send a POST request to **`POST http://localhost:8000/auth/users/`**.
example:

```bash
    curl -H "Content-Type: application/json" -X POST -d '{"username": "tester_user", "email": "tester@gmail.com", "password": "Pass#test123", "re_password": "Pass#test123", "first_name": "Test", "last_name": "User"}' http://localhost:8000/auth/users/
```


#### b. Login and save the access token:

now send a POST request to `http://localhost:8000/auth/jwt/create` with the email and password.
example:
```bash
curl -H "Content-Type: application/json" -X POST -d '{ "email": "tester@gmail.com", "password": "Pass#test123"}' http://localhost:8000/auth/jwt/create/
```
which will result in a response like this:
```bash
{
"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzk4NzQ2NywiaWF0IjoxNzM3OTAxMDY3LCJqdGkiOiIxMTM3Yjg4MWRjYWM0MzhjOTI5YmQzOTNkM2E1YjBhYSIsInVzZXJfaWQiOjExfQ.2jy_R9-CNJAtx2SU8N4CFdHxjz-5C4hI3_T-CNzmiYI",

"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3OTg3NDY3LCJpYXQiOjE3Mzc5MDEwNjcsImp0aSI6IjhkNTkxYzNiN2YxMTQyYWNiOWM2M2Y4YzNkYmU3MjZiIiwidXNlcl9pZCI6MTF9.DOqizcVDmlYcWb2efSZJUmOHazoaV9GTVeNMq1wtad0"
}
```
this access token will be used to access all the routes of the application.

#### c. Adding the access token to all your requests.
any request from here on out must have the header:
```json
"Authorization": "JWT {ACCESS_TOKEN}"
```
- If in browser, download an extension that passes headers like [**Mod Header**](https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en) and [**Header Editor**](https://chromewebstore.google.com/detail/header-editor/eningockdidmgiojffjmkdblpjocbhgh?hl=en).

- If in postman, navigate to the `headers` tab and add a new header with the key `Authorization` and the value `"JWT {ACCESS_TOKEN}"`


- If using curl command:
    ```bash
    curl -H curl -H "Content-Type: application/json" -X GET -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3OTg3NDY3LCJpYXQiOjE3Mzc5MDEwNjcsImp0aSI6IjhkNTkxYzNiN2YxMTQyYWNiOWM2M2Y4YzNkYmU3MjZiIiwidXNlcl9pZCI6MTF9.DOqizcVDmlYcWb2efSZJUmOHazoaV9GTVeNMq1wtad0" http://localhost:8000/auth/users/me/


### **IMPORTANT NOTE**: most of the app won't work and you will get `401 Unauthorized` error  without using it.


Again!! I recommend using the django rest-framework webpage (http://localhost:8000/api/{ROUTE}/ or http://localhost:8000/auth/{ROUTE}/) in your browser with a header extension as mentioned above or postman instead of the curl command in the terminal for ease of use.


## API Reference:



> **Base URL:** `http://localhost:8000/`
> All protected endpoints require:
>
> ```
> Authorization: JWT <access_token>
> ```

---

## 🚩 API Root

```
GET /api/
```

Returns top-level resource links.

---

## 🔐 Authentication (Djoser)

All paths are under `/auth/`.

### 1. List Users

```
GET /auth/users/
```

* **Admin users** → returns a list of **all** users
* **Non-admin** → returns a list containing only the current user

**Response (200 OK)**

```
[
  {
    "id": 1,
    "email": "admin@example.com",
    "username": "admin"
  },
  {
    "id": 2,
    "email": "user@example.com",
    "username": "user123"
  }
]
```

---

### 2. Register New User

```
POST /auth/users/
```

Request body:

```
{
  "email": "user@example.com",
  "username": "user123",
  "password": "Pass123!",
  "re_password": "Pass123!"
}
```

Response (201 Created):

```
{
  "id": 3,
  "email": "user@example.com",
  "username": "user123"
}
```

---

### 3. Get Current User

```
GET /auth/users/me/
```

Response (200 OK):

```
{
  "id": 3,
  "email": "user@example.com",
  "username": "user123"
}
```

---

### 4. Obtain JWT Tokens

```
POST /auth/jwt/create/
```

Request body:

```
{
  "email": "user@example.com",
  "password": "Pass123!"
}
```

Response (200 OK):

```
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

---

### 5. Refresh Access Token

```
POST /auth/jwt/refresh/
```

Request body:

```
{
  "refresh": "REFRESH_TOKEN"
}
```

Response (200 OK):

```
{
  "access": "NEW_ACCESS_TOKEN"
}
```

---

### 6. Verify Token

```
POST /auth/jwt/verify/
```

Request body:

```
{
  "token": "ACCESS_OR_REFRESH_TOKEN"
}
```

Response (200 OK)
(empty body if valid)

---

## 👥 Users & Bookings

All paths are under `/api/`.

### 7. List My Bookings

```
GET /api/users/me/bookings/
```

Response (200 OK):

```
[
  {
    "id": 4,
    "event": 7,
    "booking_date": "2025-05-21T10:15:00Z"
  },
  {
    "id": 5,
    "event": 9,
    "booking_date": "2025-05-22T08:30:00Z"
  }
]
```

---

### 8. Retrieve or Cancel a Booking

```
GET    /api/bookings/{booking_id}/
DELETE /api/bookings/{booking_id}/
```

* Only the booking owner or admin may access.

Response (GET 200 OK):

```
{
  "user": 3,
  "event": "http://localhost:8000/api/events/7/",
  "booking_date": "2025-05-22T13:45:30Z"
}
```

---

## 🎉 Events

### 9. List & Create Events

```
GET  /api/events/         → list (all authenticated users)
POST /api/events/         → create (admin only)
```

#### GET /api/events/

Supports query parameters:

* `search=<keyword>`
* `ordering=<field>` (e.g. `price`, `-date`)
* any filters from your `EventFilter`, e.g. `category=TEC`, `date_after=2025-06-01`
* pagination: `?page=<n>`

Response (200 OK):

```
[
  {
    "id": 7,
    "title": "Music Festival",
    "category": "FST",
    "custom_category": "",
    "description": "A day of fun and music!",
    "date": "2025-06-10",
    "time": "15:00:00",
    "price": "20.00",
    "venue": "Central Park",
    "location": "https://maps.google.com/...",
    "img": "/media/event_images/musicfest.jpg",
    "number_of_bookings": 10,
    "creator": "admin",
    "is_booked": true,
    "date_added": "2025-05-20T12:00:00Z",
    "last_modified": "2025-05-21T18:33:00Z"
  }
]
```

#### POST /api/events/  (admin only)

Request (multipart/form-data):

```
title=Art Workshop
category=ART
description=Learn painting
date=2025-07-01
time=10:00:00
price=15.00
venue=Community Hall
location=https://maps.example.com/...
img=<file>
```

Response (201 Created):

```
{
  "id": 12,
  "title": "Art Workshop",
  "category": "ART",
  "custom_category": "",
  "description": "Learn painting",
  "date": "2025-07-01",
  "time": "10:00:00",
  "price": "15.00",
  "venue": "Community Hall",
  "location": "https://maps.example.com/...",
  "img": "http://localhost:8000/media/event_images/xyz.jpg",
  "number_of_bookings": 0,
  "creator": "admin",
  "is_booked": false,
  "date_added": "2025-05-22T12:00:00Z",
  "last_modified": "2025-05-22T12:00:00Z"
}
```

---

### 10. Retrieve, Update, Delete Event

```
GET    /api/events/{id}/     → retrieve (any authenticated user)
PUT    /api/events/{id}/     → full update (admin or the event creator only)
PATCH  /api/events/{id}/     → partial update (admin or the event creator only)
DELETE /api/events/{id}/     → delete (admin or the event creator only)
```

#### Example PATCH

Request:

```
PATCH /api/events/12/
Authorization: JWT <admin_token>
Content-Type: application/json
```

Body:

```
{
  "price": 19.99,
  "description": "Updated description"
}
```

Response (200 OK):

```
{
  "id": 12,
  "title": "Art Workshop",
  "price": "19.99",
  "description": "Updated description",
  "last_modified": "2025-05-22T13:00:00Z",
  ... other fields ...
}
```

---

### 11. Event-Specific Bookings

```
GET  /api/events/{id}/bookings/   → list bookings for event
POST /api/events/{id}/bookings/   → create booking for current user
```

* **GET Response** (200 OK):

  ```
  [
    {
      "user": "user123",
      "booking_date": "2025-05-21T10:15:00Z"
    }
  ]
  ```
* **POST Request Body**:

  ```
  {}
  ```
* **POST Response** (201 Created):

  ```
  {
    "user": "user123",
    "booking_date": "2025-05-21T10:15:00Z"
  }
  ```

---
---
## 🖥 Frontend (WIP)

**Status:** 70% complete overall.

* The Events page and minor JavaScript edits on the Login/Signup page (~35% of frontend) were generated with AI assistance (DeepSeek)

* No AI was used in the backend — all server-side code is hand-authored.

**Available Routes:**

* `/` : Login / Signup page. After successful login, users are redirected to /events.

* `/events` : EventHub main interface listing all events. (can only be accessed by a logged-in users)

* **Admin panel** (`/admin/`) is fully implemented without AI assistance.
---
Final note: playground app is just a playground for testing and not part of the project, use it wisely.
