Project Documentation: Flask Blog (In Development)
Project Overview

This project is a blogging platform built using Flask (backend) with a frontend developed using HTML, CSS, and JavaScript. Users can create, read, update, and delete (CRUD) blog posts. The blog aims to have user authentication and search functionality in later stages. The project is currently in development, with core features being implemented incrementally.
Tech Stack

    Backend: Flask (Python)
    Frontend: HTML, CSS, JavaScript
    Database: SQL/apache
    Hosting: Planned for deployment on Heroku or Render
    Version Control: GitHub (for collaboration and tracking)

Features (Planned & In Progress or Done)

    User Authentication (Signup, Login, Logout) – In Progress(currently only handels single user session)
    Comment System – Done
    Search Functionality – Planned
    Pagination for Blog Posts – In Progress
    Responsive Frontend UI – In Development

Project Setup
Prerequisites

    Python 3.x installed.
    pip (Python package installer).
    Virtual environment (optional but recommended).
    Git (for version control).
    Basic knowledge of Flask, HTML, CSS, and JavaScript.

Step-by-Step Installation

    Clone the repository:

    bash

git clone <repository-url>
cd flask-blog

Create and activate a virtual environment:

bash

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

Install dependencies:

bash

pip install -r requirements.txt

Set up the SQLite database:

bash

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Run the development server:

bash

    flask run

    Open http://127.0.0.1:5000 in your browser to see the blog running.

Folder Structure

php

flask-blog/
│
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css        # Custom styles
│   ├── js/
│   │   └── scripts.js        # Custom JavaScript
│   └── images/
│       └── logo.png          # Logo for the blog and other pictures
│
├── templates/                # HTML templates
│   ├── layout.html             # Base template with common layout
│   ├── index.html            # Homepage showing blog posts
│   └── post.html             # Individual blog post page
│
├── app.py                    # Main Flask application
├── config.json               # Configuration settings
└── README.md                 # Project overview
