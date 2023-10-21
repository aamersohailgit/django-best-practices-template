---
title: My Django Project Documentation
---

# My Django Project

## Overview

This Django project is geared towards delivering an impeccable user management system with some added flair in features.

## Project Structure

project/
│
├── manage.py
│
├── apps/
│ ├── users/
│ │ ├── migrations/
│ │ ├── templates/
│ │ ├── init.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── urls.py
│ │ └── views.py
│ └── ... (other app directories with a similar structure)
│
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yaml
│
├── static/
│ └── ... (static files: CSS, JS, images, etc.)
│
├── templates/
│ └── ... (global template files)
│
├── media/
│ └── ... (uploaded media files)
│
├── main/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── requirements.txt
│
└── README.md

## Features

### 1. **User Authentication**

- **Registration**: Users can sign up by furnishing necessary details. During the registration process, the user's first name and last name are automatically derived from the provided full name and family name.
- **Login**: Those who've already registered can smoothly log in with their set credentials.

### 2. **User Profile Management**

- **Profile Creation**: A profile gets auto-generated once a user registers.
- **Profile Update**: Users can conveniently change their profile pictures and elaborate a little about themselves in the bio section.
- **Addresses**: Users can add multiple addresses to their profile, making it easier for service deliveries or mailings.

### 3. **User Types**

The user gets a type label which will determine the services and functionalities accessible to them. The following are the types of users:

- **Customer**: These are the everyday users scouting for services the platform offers.
- **Chef**: These users proffer culinary skills as a service on the platform.

An added advantage is the admin's power to alter, add, or delete user types, ensuring adaptability to any changes in roles in the future.

### 4. **Admin Privileges**

Users crowned with admin rights can:

- Play around with user types — assign or modify.
- View user profiles and make necessary tweaks.

## Technical Details

### 1. **Django Version**

The backbone of the project, Django, is of version 4.1.1.


### 2. **Database**

SQLite stands as the project's cornerstone, ensuring data storage is both light and efficient.

### 3. **Dependencies**

- **Django Rest Framework (DRF)**: A lifesaver for constructing APIs.
- **DRF Spectacular**: Enhances the API documentation by making it interactive using the Swagger UI.
- **Corsheaders**: Manages the server headers, essential for CORS.

## Getting Started

### 1. **Installation**

Kick things off by cloning the repository and head straight to the root directory.

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
