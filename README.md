Bug Tracker

A Django-powered web application designed to efficiently manage and track bugs in software projects. This project simplifies bug logging, prioritization, and status management, providing an organized approach to software maintenance.

---

## ✨ Features

- **Add, List, and Track Bugs**: Log bugs with titles, descriptions, priorities, and statuses.
- **Set Priorities and Statuses**: Define the urgency and progress of each bug.
- **Secure Admin Panel**: Manage bugs efficiently through Django's robust admin interface.

---

## 🛠️ Technologies Used

- **Framework**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap (optional for styling)
- **Database**: SQLite (default Django database)
- **Deployment Tools**: Gunicorn, Heroku (optional)

---

## 🚀 Getting Started

### Prerequisites
Ensure the following are installed:
- Python (v3.8 or later)
- Django Framework (v4.x or later)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/khushisaini10/BugTrack.git
   ```
2. **Navigate into the Project Folder**:
   ```bash
   cd BugTrack
   ```
3. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Use venv\Scripts\activate for Windows
   ```
4. **Install Dependencies**:
   ```bash
   pip install django
   ```
5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## 📝 Usage

1. **Log in to the Admin Panel**:
   - Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```
   - Access the admin panel at `http://127.0.0.1:8000/admin`.

2. **Navigate to the Bug Tracker**:
   - Access the bug tracker homepage at `http://127.0.0.1:8000/`.

3. **Add and Manage Bugs**:
   - Add bugs using the frontend form.
   - View and update bug details via the admin panel.

---

## 🛠️ Future Improvements

- **User Authentication**: Restrict access to logged-in users only.
- **Advanced Filters**: Search and filter bugs by priority and status.
- **Dashboard Analytics**: Provide graphical insights into bug trends and resolution times.

---

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request describing your changes.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

If you have questions or want to collaborate, feel free to reach out:
- **GitHub**: [khushisaini10](https://github.com/khushisaini10)
```

