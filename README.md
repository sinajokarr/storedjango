````markdown
<div align="center">

<!-- Optional: change path to your real logo -->
<img src="./static/img/opera-home-logo.png" alt="Opera Home Logo" width="120"/>

# 🛍 Opera Home Store – Quiet Luxury E-commerce Template

***

[![Tech: Django](https://img.shields.io/badge/Backend-Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Language: Python](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Frontend: HTML/CSS](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS-f5b400?style=for-the-badge&logo=html5&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Portfolio%20Template-1abc9c?style=for-the-badge)]()

</div>

<br>

## ✨ Project Overview

**Opera Home Store** is a modern e-commerce template built with **Django 5** and a custom black-and-gold “quiet luxury” visual theme.  
It is designed as a realistic storefront for home décor / lifestyle brands and as a strong portfolio project.

Main ideas:

- Clean, curated product grid instead of a noisy catalogue  
- Story-driven content pages (About, Contact, brand philosophy)  
- Django architecture ready to extend into a full production shop  

---

## 💎 Core Features

### 🛒 Storefront

- Product list with category sidebar, search and pagination  
- Search products by keyword (name/title)  
- Product detail page (image, description, category, price)  
- Cart page for managing selected items  
- Helpful empty states when there are no products yet  

### 🎨 UX & Design

- Opera Home theme: warm neutrals + subtle black-and-gold accents  
- Responsive layout with semantic HTML + modern CSS (`opera.css`)  
- Template inheritance via `_base.html` and page blocks  
- Strong marketing copy on Products, About & Contact pages  

### 🔐 Auth & Account

- Custom-styled Django `LoginView` at `/accounts/login/`  
- Auth-aware header (username + Log in / Log out buttons)  
- Staff-only CTA when the catalogue is empty: “Add your first product”  

---

## 🧰 Tech Stack

| Layer          | Tools / Libraries                                  |
|----------------|----------------------------------------------------|
| Backend        | Python 3.x, Django 5.x                             |
| Templates      | Django Template Language (DTL)                     |
| Frontend       | HTML5, custom CSS (`static/css/opera.css`)         |
| Database (dev) | SQLite (`db.sqlite3`)                              |
| Auth           | `django.contrib.auth` (LoginView)                  |
| Static & Media | Django static/media configuration                  |

---

## 📁 Project Structure (simplified)

```bash
storedjango-main/
├── accounts/
│   └── urls.py                 # login route (Django LoginView)
│
├── config/
│   ├── settings.py             # INSTALLED_APPS, TEMPLATES, STATIC/MEDIA
│   └── urls.py                 # include store + accounts urls
│
├── store/
│   ├── models.py               # Product, Category, Cart, etc.
│   ├── views.py                # CBVs for list/detail/cart/about/contact
│   ├── urls.py                 # namespaced `store:` urls
│   └── templates/
│       └── store/
│           ├── product_list.html
│           ├── product_detail.html
│           ├── cart_detail.html
│           ├── product_form.html / ProductCreate.html
│           ├── delete_product.html
│           ├── about.html
│           └── contact.html
│
├── templates/
│   ├── _base.html              # main layout (header/nav/footer)
│   └── registration/
│       └── login.html          # custom login page
│
└── static/
    └── css/
        └── opera.css           # Opera Home visual theme
````

---

## ⚙️ Installation & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd storedjango-main

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. (Optional) Create admin user
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver
```

Open in browser:

* Storefront: `http://127.0.0.1:8000/`
* About: `http://127.0.0.1:8000/about/`
* Contact: `http://127.0.0.1:8000/contact/`
* Cart: `http://127.0.0.1:8000/cart/`
* Login: `http://127.0.0.1:8000/accounts/login/`

---

## 🧭 Key Pages & UX Flow

### 🛍 Products – “Signature Collection”

* Hero section with brand tagline and search bar
* Category navigation in sidebar
* Responsive product cards (image, category, price)
* Empty-state “gallery is almost ready” message with tips

### 📖 About – Brand Story

* Narrative layout explaining **Philosophy / Craft / Experience**
* Boxed cards and sections telling the origin story of Opera Home
* Focus on quiet luxury, real-life durability and design guidance

### 📬 Contact – “Let’s Design Your Next Space”

* Contact form (name, email, topic, message)
* Client care info + trade / project section
* FAQ-style quick questions block

### 🔐 Auth – “Welcome Back”

* Clean login screen integrated with Opera Home branding
* Ready for future Registration / Password reset flows

---

## 🚀 Roadmap

* [ ] Complete checkout flow (addresses, orders, order history)
* [ ] Discount codes / promotions
* [ ] Wishlist & “save for later”
* [ ] Public REST API using Django REST Framework
* [ ] Basic analytics (top products, most viewed, simple funnels)

---

## 💬 Feedback & Collaboration

This project is a **Django store starter** and a **portfolio piece** for e-commerce backends and frontends.
Suggestions, issues and ideas are welcome—feel free to open an issue or fork the repo and experiment.

```
```
