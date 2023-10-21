---
title: My Django Project Documentation
---

# My Django Project

## Overview

This is a Django project that aims to provide user management functionalities with enhanced features.

## Features

### 1. **User Authentication**

- **Registration**: Users can register on the platform by providing their details.
- **Login**: Registered users can log in using their credentials.

### 2. **User Profile Management**

- **Profile Creation**: Upon registration, a profile is automatically created for the user.
- **Profile Update**: Users can update their avatars and bio information.

### 3. **User Types**

Users can be assigned specific types. These types dictate the functionalities and access levels they possess. Currently, the system supports the following user types:

- **Customer**: Regular users looking to utilize the platform's services.
- **Chef**: Users offering culinary services on the platform.

The admin has the privilege to dynamically add, update, read, or delete user types, making the system flexible to accommodate future roles.

### 4. **Admin Privileges**

Users with admin rights have the following capabilities:

- Assigning and modifying user types.
- Overseeing user profiles and making necessary adjustments.

## Technical Details

### 1. **Django Version**

The project is built using Django version 4.1.1.

### 2. **Database**

SQLite is the primary database for the project, providing lightweight and efficient data storage.

### 3. **Dependencies**

- **Django Rest Framework (DRF)**: Used for building APIs.
- **DRF Spectacular**: Provides an interactive API documentation using Swagger UI.
- **Corsheaders**: Handles the server headers required for CORS.

## Getting Started

### 1. **Installation**

Clone the repository and navigate to the root directory.

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
