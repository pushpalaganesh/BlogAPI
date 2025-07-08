# 📝 Django BlogApp API 

Welcome to **Django BlogApp**, a powerful and scalable REST API for a blogging platform built using **Django** and **Django REST Framework (DRF)**.

This project showcases real-world implementations of:
- Django Models & Relationships
- REST API endpoints with generic views
- Filtering, Searching, and Pagination
- Best coding practices and modular architecture

---

## 📌 Project Overview

The BlogApp API allows users to:
- View, search, and filter blogs
- Create new blog posts 
- Update or delete their own blog posts
- Add comments to blog posts
- View, edit, or delete their own comments

It’s ideal for:
- Learning Django REST Framework
- Building real-world CRUD APIs
- Extending into a full-stack blog app

---

## 🔧 Key Features
 
✅ **CRUD for Blogs and Comments**  
✅ **Filtering using django-filter**  
✅ **Search support with DRF filters**  
✅ **Pagination using PageNumberPagination**  
✅ **Generic API Views for clean structure**  
✅ **Supports future extensions like JWT, file uploads, categories, and tagging**

---

## 🛠️ Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- django-filter
- SQLite (can be switched to PostgreSQL/MySQL)
- DRF Browsable API interface


---

## 🔄 Models Overview

### 🧾 Blog Model
| Field       | Type             | Description                           |
|-------------|------------------|---------------------------------------|
| `title`     | CharField        | Title of the blog                     |
| `content`   | TextField        | Main blog content                     |
| `category`  | CharField        | Blog category (e.g. Python, API)      |
| `author`    | ForeignKey(User) | Who wrote the blog                    |
| `created_at`| DateTimeField    | Auto timestamp when blog is created   |

### 💬 Comment Model
| Field       | Type             | Description                           |
|-------------|------------------|---------------------------------------|
| `blog`      | ForeignKey(Blog) | Related blog post                     |
| `author`    | ForeignKey(User) | Who made the comment                  |
| `content`   | TextField        | Comment text                          |
| `created_at`| DateTimeField    | Auto timestamp                        |

---


## 📋 API Endpoints

### 🔹 Blog

| Method | Endpoint         | Description                       |
|--------|------------------|-----------------------------------|
| GET    | `api/v1/blogs/`        | List all blogs                    |
| POST   | `api/v1/blogs/`        | Create blog  |
| GET    | `api/v1/blogs/<id>/`   | Retrieve blog by ID               |
| PUT    | `/blogs/<id>/`   | Update blog          |
| DELETE | `/blogs/<id>/`   | Delete blog         |

### 🔹 Comments

| Method | Endpoint           | Description                          |
|--------|--------------------|--------------------------------------|
| GET    | `api/v1/comments/`       | List all comments                    |
| POST   | `api/v1/comments/`       | Create comment   |
| GET    | `api/v1/comments/<id>/`  | Retrieve comment by ID               |
| PUT    | `api/v1/comments/<id>/`  | Update comment         |
| DELETE | `api/v1/comments/<id>/`  | Delete comment          |

---

## 🔍 Filtering & Search

### Filtering (via `django-filter`)

/blogs/?author__username=ganesh
/blogs/?created_at_after=2025-07-01&created_at_before=2025-07-07
---
### Pagination

/blogs/?page=2


## 🚀 Setup Instructions

### 1. Clone the repo
- git clone https://github.com/pushpalaganesh/BlogAPI.git
- cd MyBlogPro

### 2. Create a virtual environment

- python -m venv venv
- source venv/bin/activate  # Windows: venv\Scripts\activate
### 3. Install dependencies

- pip install -r requirements.txt
### 4. Run migrations

- python manage.py makemigrations
- python manage.py migrate
### 5. Create superuser

- python manage.py createsuperuser
### 6. Run server

- python manage.py runserver
Then open: http://127.0.0.1:8000/

## Screenshots of Project
### Admin

![Screenshot (31)](https://github.com/user-attachments/assets/bc529649-f59f-4066-bc60-c456734d1f90)
![Screenshot (32)](https://github.com/user-attachments/assets/183b7948-384b-4043-95c7-a9d89cbb794e)

### Blog [GET]
![Screenshot (27)](https://github.com/user-attachments/assets/1dfd9c32-0775-4e3d-82ac-36a4f75c11b8)

### BLOG [POST]
![Screenshot 2025-07-08 155142](https://github.com/user-attachments/assets/766ed39c-6483-4e7b-9058-8330d1fb8491)
![Screenshot (28)](https://github.com/user-attachments/assets/0ce54a02-7d66-43ec-8d94-8eba42f0fa5a)

### BLOG [PUT]
![Screenshot 2025-07-08 155232](https://github.com/user-attachments/assets/7673b7cc-abab-4188-8a39-51ea5556b247)

### BLOG [DELETE]
![Screenshot (29)](https://github.com/user-attachments/assets/8a7c5292-f12b-4c23-baab-f916c78e3945)

### BLOG [FILTER]
![Screenshot (30)](https://github.com/user-attachments/assets/2c0f6da0-7021-476c-abf4-d00edcf29af1)

### COMMENT [GET]
![Screenshot (23)](https://github.com/user-attachments/assets/eb35482e-c703-4d98-bf56-10f592b87119)

### COMMENT [POST]
![Screenshot 2025-07-08 154751](https://github.com/user-attachments/assets/733c83f9-f61f-49bd-92a4-35ebea3f72f9)
![Screenshot (24)](https://github.com/user-attachments/assets/46fda3d2-4f4f-4f19-9f70-dda417ec9434)

### COMMENT [PUT]
![Screenshot 2025-07-08 154907](https://github.com/user-attachments/assets/6bce5996-a970-446a-9b89-bce931662189)

### COMMENT [DELETE]
![Screenshot (25)](https://github.com/user-attachments/assets/249548f9-8ad9-4691-a46e-1f4882a46f2a)

### COMMENT [FILTER]
![Screenshot (26)](https://github.com/user-attachments/assets/e68f6263-3119-4a3c-ae59-2429442288b8)
