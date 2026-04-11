# 📱 PhoneRadar Pro — Phone & Game Review Platform

[![Python Version](README.assets/python-3.10%2B-blue)](https://www.python.org/)
[![Django Version](README.assets/django-6.0.3-green)](https://www.djangoproject.com/)
[![License](README.assets/license-MIT-orange)](LICENSE)

**PhoneRadar Pro** is a Django-based content management system that integrates **phone reviews** and **game reviews**. It features user authentication, many-to-many relationships, dynamic front-end rendering, and a fully customized admin panel.

---

## 🚀 Key Features

### 📱 Phone Review Module (`PhoneReview`)
- Three‑layer data model: Brand, PhoneModel, Review
- **Many‑to‑many** relationship between reviews and phone models (one review can cover multiple phones)
- Auto‑generated SEO‑friendly slugs
- User registration / login / logout
- Only logged‑in users can **add phone models** and **write reviews**
- Review detail page supports **comments** and **like/dislike** buttons
- Fully English interface with a unified top bar (logo, login status)

### 🎮 Game Review Module (`games`)
- Game model: name, description, release date, rating (0.0–10.0), cover image URL
- Class‑based `ListView` to display the game list
- Shows cover images and rating badges

### 🔧 Highlights
- **Custom admin login page**: displays demo credentials (`admin` / `woc7014admin`) for easy presentation
- **Unified front‑end style**: all pages inherit `base.html` with the same top bar and CSS
- **Responsive design**: works on desktop and mobile
- **Full migration history**: supports PostgreSQL / SQLite

---

## 🛠️ Tech Stack

| Layer           | Technology                             |
| --------------- | -------------------------------------- |
| Backend         | Python 3.13, Django 6.0.3              |
| Database        | PostgreSQL (production) / SQLite (dev) |
| Frontend        | HTML5, CSS3 (custom styles)            |
| Static files    | WhiteNoise (production)                |
| Version control | Git / GitHub                           |

---

## 📦 Quick Start (Local)

### 1. Clone the repository
```bash
git clone https://github.com/Aurelianus-001/PhoneRadar-Pro.git
cd PhoneRadar-Pro
```



### 2. Create and activate a virtual environment

bash

```
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows
```



### 3. Install dependencies

bash

```
pip install -r requirements.txt
```



> If you don’t have a `requirements.txt`, at least install: `django`, `psycopg2-binary`, `dj-database-url`, `python-dotenv`, `whitenoise`

### 4. Run migrations

bash

```
python manage.py makemigrations
python manage.py migrate
```



### 5. Create a superuser (for admin access)

bash

```
python manage.py createsuperuser
```



Follow the prompts – you can use `admin` / `woc7014admin` as shown on the admin login page.

### 6. Start the development server

bash

```
python manage.py runserver
```



- Homepage (phone reviews): http://127.0.0.1:8000/
- Game reviews list: http://127.0.0.1:8000/games/
- Admin panel: http://127.0.0.1:8000/admin/ (credentials hint is displayed)

### 7. (Optional) Load sample game data

bash

```
python import_games.py
```



------

## 📂 Project Structure

text

```
phoneradar_pro/
├── phoneradar_pro/          # Project settings
│   ├── settings.py          # Global config (static, auth redirects)
│   ├── urls.py              # Main routing (admin, accounts, index, games, empty)
│   └── wsgi.py
├── PhoneReview/             # Phone reviews app
│   ├── models.py            # Brand, PhoneModel, Review, Comment
│   ├── views.py             # ListView, DetailView, CreateView, comment/like logic
│   ├── urls.py              # add-phone/, add-review/, <slug>/ etc.
│   ├── forms.py             # PhoneModelForm, ReviewForm
│   └── templates/reviews/   # review_list.html, review_detail.html, add_*.html
├── games/                   # Game reviews app
│   ├── models.py            # Game (name, description, release_date, rating, image_url)
│   ├── views.py             # GameReviewListView
│   ├── urls.py              # /games/ route
│   └── templates/games/     # game_list.html
├── main/                    # Welcome page (index/)
│   └── views.py             # Renders the welcome page
├── static/                  # Static files
│   ├── css/style.css        # Global styles (comments, game cards, etc.)
│   └── images/logo.png      # Site logo
├── templates/               # Global templates
│   ├── base.html            # Top bar (logo, login status)
│   ├── registration/        # login.html, register.html
│   └── main/index.html      # Welcome page template
├── staticfiles/             # collectstatic output (production)
├── manage.py
└── README.md
```



------

## 🔐 Admin Login Hint

To make grading easier, the `/admin` login page shows a custom notice:

> 🔑 Demo credentials:
> Username: `admin`
> Password: `woc7014admin`

This hint appears only when `DEBUG=True` and does not affect production security.

------

## 📸 Screenshots (for assignment submission)

- **Phone review homepage** – list of reviews with author, rating, related phones
- **Game list page** – covers, names, ratings, descriptions
- **Admin login page** – with credential hint

Please upload screenshots to Spectrum as required.

------

## 🤝 Contribution & License

Issues and pull requests are welcome. This project is open‑sourced under the MIT license.

**Author:** Aurelianus-001

**Contact:** 1807129991@qq.com

**Course:** WOC7014 FRAMEWORK-BASED SOFTWARE DESIGN AND DEVELOPMENT







