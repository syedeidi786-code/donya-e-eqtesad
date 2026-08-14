# Donya-e-Eqtesad 📰

A modern Django-based news website where users can read, publish, edit, and interact with articles from different categories.

## 🌐 Live Website

👉 **[Visit Donya-e-Eqtesad](https://donya-e-eqtesad-3.onrender.com)**

Replace `YOUR_LIVE_WEBSITE_LINK_HERE` with your actual Render URL.

---

## 📌 About the Project

**Donya-e-Eqtesad** is a full-stack news publishing platform built with Django.

The website allows visitors to explore news articles while registered users can create and manage their own articles.

The project was created to practice and demonstrate real-world web development concepts including authentication, database management, media storage, CRUD operations, and deployment.

---

## ✨ Features

- 📰 Browse news articles
- 🔎 Search articles
- 👤 User registration and login
- 🔐 Password reset functionality
- ✍️ Create articles
- 📝 Edit your own articles
- 🗑️ Delete your own articles
- ❤️ Like articles
- 💬 Comment on articles
- 🖼️ Upload article images
- 📊 User dashboard
- 🛠️ Django admin panel
- 📱 Responsive design
- ☁️ Cloudinary image storage
- 🗄️ PostgreSQL database
- 🚀 Deployed on Render

---

## 🛠️ Technologies Used

### Backend
- Python
- Django
- Django Authentication
- Django ORM

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Database
- PostgreSQL
- SQLite for local development

### Deployment & Storage
- Render
- Cloudinary
- WhiteNoise

### Development Tools
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```text
news_land/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── articles/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── news_land/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
