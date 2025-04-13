# 🎉 EventEase

**EventEase** is a full-featured event management web application built using Django and PostgreSQL. It allows users to explore and interact with upcoming events, feature highlights, and secure authentication.

---

## 🚀 Features

- 🔐 User Authentication (Login/Register)
- 🏠 Home page with dynamic features list
- 📅 Event browsing and event detail pages
- 📂 Modular Django apps: `web`, `events`, `authentication`, and `main`
- 🖼 Media and static file support
- 🧾 Admin panel to manage event data and features

---

## 🛠 Tech Stack

- Python 3
- Django
- PostgreSQL
- HTML, CSS, JavaScript
- Bootstrap

---

## 📁 Project Structure

```
EventEase/
├── authentication/
├── events/
├── main/
├── web/
│   └── fixtures/
│       └── features.json
├── templates/
├── static/
├── media/
├── event_ease/
│   └── settings.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/mohd-yaseen-official/event-ease.git
cd EventEase
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory and add:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DB_NAME=event_ease
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Load initial data (features for the homepage)

```bash
python manage.py loaddata web/fixtures/features.json
```

### 7. Create a superuser (optional but recommended)

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## ✨ Credits

Developed with 💙 by [Mohamed Yaseen](https://github.com/mohd-yaseen-official)
