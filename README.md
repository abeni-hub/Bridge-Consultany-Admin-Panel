# Bridge Consulting Admin Panel

A professional and scalable **Django-based Admin Panel** built for managing the frontend content of the **Bridge Consulting corporate website**.

This system enables administrators to dynamically manage all website sections including hero content, about us, services, workflow steps, testimonials, blog stories, feedback, and comments through the Django Admin Dashboard.

---

## 🚀 Features

### 📌 Dynamic Website Content Management
The admin panel allows full control over frontend sections:

- Hero Section
- About Us Section
- Services Section
- How It Works Section
- Testimonials Section
- Feedback Management
- Comment Moderation
- Blog Stories Management

---

## 🏗 Modules Included

### 1. Hero Section
Manage the landing page hero content:
- Title
- Subtitle
- Primary CTA Button
- Secondary CTA Button
- Background Image URL
- Dynamic Statistics (JSON format)

Example Stats JSON:
```json
[
  {
    "number": "500+",
    "label": "Projects Completed"
  },
  {
    "number": "98%",
    "label": "Client Satisfaction"
  },
  {
    "number": "50+",
    "label": "Industry Experts"
  }
]
```

---

### 2. About Us Section
Manage company information:
- Subtitle
- Description
- Mission Title & Content
- Vision Title & Content
- Years of Excellence
- Companies Count
- Image URL
- CTA Title & Content

---

### 3. Services Section
Create and manage multiple services:
- Section Subtitle
- Section Title
- Description
- Add Unlimited Services

Each service includes:
- Title
- Description
- Icon
- Gradient Theme
- Features

---

### 4. How It Works Section
Manage process workflow steps:
- Section Subtitle
- Section Title
- Description
- CTA Button

Steps include:
- Step Number
- Title
- Description
- Icon
- Deliverables

---

### 5. Testimonials Section
Manage client testimonials:
- Name
- Role
- Company
- Image URL
- Testimonial Content
- Rating (1–5)
- Gradient Theme

---

### 6. Feedback System
Store customer feedback messages:
- Name
- Email
- Rating
- Status
- Message

Statuses:
- New
- Read
- Replied

---

### 7. Comment Moderation
Manage blog or website comments:
- User
- Post
- Comment
- Status

Statuses:
- Pending
- Approved
- Rejected

---

### 8. Blog Stories
Manage blog content:
- Title
- Category
- Status
- Image URL
- Expert / Author
- Content

Categories:
- Business
- Finance
- Analysis
- Strategy
- Consulting

---

## 🛠 Tech Stack

- **Backend:** Django
- **Admin Dashboard:** Django Admin
- **Database:** PostgreSQL / SQLite
- **API Ready:** Django REST Framework Compatible
- **Version Control:** Git + GitHub

---

## 📁 Project Structure

```bash
bridge_consulting/
│
├── core/
│   ├── models.py
│   ├── admin.py
│
├── services/
│   ├── models.py
│   ├── admin.py
│
├── testimonials/
│   ├── models.py
│   ├── admin.py
│
├── feedback/
│   ├── models.py
│   ├── admin.py
│
├── blog/
│   ├── models.py
│   ├── admin.py
│
├── bridge_consulting/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## ⚙ Installation

### Clone Repository
```bash
git clone https://github.com/your-username/bridge-consulting-admin.git
cd bridge-consulting-admin
```

---

### Create Virtual Environment
```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

---

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Create Superuser
```bash
python manage.py createsuperuser
```

---

### Start Development Server
```bash
python manage.py runserver
```

---

## 🔑 Admin Login

Open:
```bash
http://127.0.0.1:8000/admin/
```

Login using your superuser credentials.

---

## 📈 Future Improvements

Planned upgrades:
- Django REST Framework APIs
- React Frontend Integration
- Image Upload Support
- Rich Text Editor for Blogs
- Analytics Dashboard
- Role-Based Permissions
- Email Notifications

---

## 🎯 Use Case

This admin panel is designed for:

- Consulting firms
- Corporate websites
- Service-based businesses
- Agencies
- Enterprise CMS systems

---

## 👨‍💻 Author

Developed by **Abeni / abeni-hub**  
Full Stack Web Developer | Data Analyst | AI & ML Engineer

---

## 📄 License

This project is open-source and available for professional and commercial use.
