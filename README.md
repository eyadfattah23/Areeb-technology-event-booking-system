# Event booking system 
# EventHub - Event Booking System

![EventHub Screenshot](/static/images/screenshot.png)
![EventHub Screenshot2](/static/images/image.png)
![EventHub Screenshot2](/static/images/image1.png)
## 📌 Overview

EventHub is a full-stack event booking platform that enables users to discover, book, and manage events while providing administrators with powerful event management tools. Built with Django REST Framework (DRF) for the backend and vanilla JavaScript for the frontend, this system offers:

- **Secure JWT-based authentication** for users and admins
- **Responsive event browsing interface** with real-time availability
- **Intuitive booking management** for attendees
- **Comprehensive admin dashboard** for event organizers
- **RESTful API architecture** for future scalability

## ✨ Key Features

### 🔐 Authentication System
- User registration with email
- JWT-based login/logout flows
- Password reset functionality
- Role-based access control (User/Admin)

### 🎪 Event Management
- **Public Event Listings**:
  - Filter events by category, date, price range
  - Search events by title/description
  - Sort by popularity, date, or price
- **Event Details**:
  - High-resolution event images
  - Interactive venue maps
  - Social sharing options

### 🎟 Booking Engine
- One-click booking system
- Booking confirmation emails
- Personalized "My Bookings" dashboard
- Cancellation with refund processing

### 🛠 Admin Panel
- **CRUD Operations**:
  - Create/Edit/Delete events
  - Manage event categories
  - Handle user submissions
- **Analytics Dashboard**:
  - Real-time attendance tracking
  - Revenue reports
  - Popular event metrics

### 🚀 Technical Highlights
| Component        | Technology Stack |
|-----------------|------------------|
| **Frontend**    | Vanilla JS, CSS3, HTML5 |
| **Backend**     | Django 4.2, DRF 3.14 |
| **Database**    | MySQL/PostgreSQL |
| **Auth**        | JWT, Djoser |
| **API**         | RESTful JSON API |

## 📋 Additional Features

### For Users
- Personalized event recommendations
- Waitlist for sold-out events

### For Administrators
- Custom reporting tools
- User management console
- Automated email notifications

## 🏆 Competitive Advantages
- **Lightweight**: No heavy frontend frameworks (~50% faster load times)
- **Customizable**: Modular architecture for easy feature additions
- **Secure**: Industry-standard authentication practices
- **Scalable**: Optimized for high-traffic event launches

---


## Installation
* ### 1. **Clone the repository**:
   ```bash
   git clone https://github.com/eyadfattah23/Areeb-technology-event-booking-system.git
   cd Areeb-technology-event-booking-system
   ```

* ### 2. **install python3 and pip3 if not already installed**:
    ```bash
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y python3.10 python3.10-venv python3.10-dev

    python3 --version
    ```


### 3. **install mysql**
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04



### 4. **prepare the databases by using setupDB.sql**


### 5. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source env/bin/activate
   ```

### 6. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```


### 7. migrate the database:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```


* ### 9. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```
    and enter your credentials for this superuser/admin account.


* ### 10. Open your web browser and navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) then login using the credentials you used with the command `python3.10 manage.py createsuperuser`
