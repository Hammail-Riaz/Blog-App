# Flask Blog App

A simple blogging web application built with **Flask** for practice and learning purposes.  
This project demonstrates how to create, read, update, and delete blog posts, manage users, and work with databases in a Flask-based web app.

---

## 🌐 What is Blogging?
Blogging is the practice of writing and publishing content (called *posts* or *articles*) on the internet.  
A blog serves as a personal journal, a news platform, or a place to share knowledge and ideas with readers.  
This project recreates the core functionality of a blogging platform on a smaller scale to help understand how such systems work under the hood.

---

## ⚙️ Features
- **User Authentication**
  - Sign up, log in, and log out.
- **Blog Post Management**
  - Create new blog posts.
  - Edit and update existing posts.
  - Delete posts.
  - View all posts in a feed-like style.
- **Database Integration**
  - SQLite database used for simplicity.
- **Flash Messages**
  - Success/error feedback for user actions.
- **Basic Form Validation**
  - Ensures required fields are filled before submitting.

---

## 🔒 Security & Limitations
This is a **practice project**, not production-ready.  
Some current limitations include:
- Passwords may not be encrypted securely (basic hashing/bcrypt used if enabled).
- No CSRF (Cross-Site Request Forgery) protection on forms (unless Flask-WTF is configured).
- Limited form validation (does not cover all edge cases).
- No admin dashboard or user role management.
- SQLite database is not scalable for production use.

⚠️ **Do not use this app as-is for real-purpose-world deployment. (only for fun and learning)**  
It’s intended for learning the basics of Flask web development.

---

## 📝 App Pages & Flow
1. **Home Page (`/`)**
   - Shows the latest blog posts.
   - Visitors can read without logging in.
2. **Register Page (`/register`)**
   - New users can create an account.
3. **Login Page (`/login`)**
   - Existing users log in to create or manage posts.
4. **Dashboard / Profile**
   - Users see their own posts.
   - Option to create new posts.
5. **Create Post Page (`/create`)**
   - Authenticated users can write and publish posts.
6. **Edit Post Page (`/edit/<id>`)**
   - Authors can edit their own posts.
7. **Delete Post**
   - Option to remove a post.
8. **Logout**
   - Ends the session and redirects to home.

---

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/Hammail-Riaz/flask-blog-app.git
   cd flask-blog-app

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Creating database
   ```bash
   flask db init
   ```
   This will initialize the db

   ```bash
   flask db migrate
   ```
   Make the schema changes 

   ```bash
   flask db upgrade
   ```
   Finalizes the schema changes


4. Run the Flask app:
   ```bash
   python run.py
   ```

5. Then open in browser:

   - http://127.0.0.1:5000

## 🌐 Visiting Live:
   - This app is live at https://hammailriaz.pythonanywhere.com . 

   - Only for fun use.