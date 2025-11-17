````markdown
<div align="center">
  
# 🛒 Opera Home Store – Quiet Luxury Django E-commerce Template ✨
  
***

[![Tech: Django](https://img.shields.io/badge/Backend-Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Language: Python](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Frontend: HTML/CSS](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Status: Portfolio Template](https://img.shields.io/badge/Status-Portfolio%20Piece-1abc9c?style=for-the-badge)](#)
  
***
</div>

<br>

## 🎯 About This Project: A Quiet-Luxury Storefront

**Opera Home Store** is a Django-based e-commerce template for home décor and lifestyle brands that want a **minimal, quiet-luxury UI** instead of a noisy, overloaded catalogue.

The goal is to provide:

- A realistic storefront you can plug real products into  
- Clean, semantic Django templates ready to extend to production  
- A strong portfolio project showing **CBV usage, template inheritance and custom styling**

<br>

### 📬 Author & Project Links

| Type | Link |
| :--- | :--- |
| 👤 **Author** | [Sina Jokar – Backend Developer](https://www.linkedin.com/in/sinajokar/) |
| 📦 **Repository** | `storedjango-main` on GitHub |
| 📧 **Contact** | [cnajokar11@yahoo.com](mailto:cnajokar11@yahoo.com) |

---

## 🛠️ Tech Stack: What Powers Opera Home

A compact overview of the technologies behind the storefront.

### 🌐 Backend & Templates

| Category | Stack |
| :--- | :--- |
| **Language** | `Python 3.x` |
| **Framework** | `Django 5.x` (Class-Based Views) |
| **Templating** | Django Template Language (DTL) with `_base.html` layout |
| **Auth** | `django.contrib.auth` + `LoginView` at `/accounts/login/` |

<p align="center">
  <img src="https://img.shields.io/badge/Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge">
</p>

### 💾 Data, Static Files & Tooling

| Category | Stack |
| :--- | :--- |
| **Database (dev)** | `SQLite` (`db.sqlite3`) |
| **Static Assets** | Custom CSS theme `static/css/opera.css` |
| **Views** | CBVs for product list/detail/cart/about/contact |
| **Runtime** | `python manage.py runserver` local dev |

---

## 💻 Opera Home Store: Features & UX

A breakdown of what this template demonstrates.

### 🏬 Storefront & Cart

* Product listing with grid layout and category support  
* Product detail page (image, title, description, price, category)  
* Cart page for adding/removing items and reviewing selections  
* Empty states that keep the UI clean when there is no data yet  

### 🧭 Brand Pages

* **About** page explaining the Opera Home philosophy (Quiet Luxury / Craft / Experience)  
* **Contact** page with structured sections for client messages and brand information  
* All pages extend `_base.html` to reuse header, footer and navigation  

### 🔐 Auth: “Welcome Back”

* Custom-styled Django `LoginView` rendered via `templates/registration/login.html`  
* Navigation bar reacts to auth state (Log in / future Log out)  
* URL: `/accounts/login/` (ready to extend with registration / password reset flows)  

---

## 🧱 Project Structure (Simplified)

```bash
storedjango-main/
├── accounts/
│   └── urls.py                 # Login route (Django LoginView)
├── config/
│   ├── settings.py             # INSTALLED_APPS, TEMPLATES, STATIC/MEDIA
│   └── urls.py                 # include store + accounts urls
├── store/
│   ├── models.py               # Product, Category, Cart models (portfolio-ready)
│   ├── views.py                # CBVs for list/detail/cart/about/contact
│   ├── urls.py                 # namespaced 'store:' urls
│   └── templates/
│       └── store/
│           ├── product_list.html
│           ├── product_detail.html
│           ├── cart_detail.html
│           ├── product_form.html / ProductCreate.html
│           ├── delete_product.html
│           ├── about.html
│           └── contact.html
├── templates/
│   ├── _base.html              # main layout (header/nav/footer)
│   └── registration/
│       └── login.html          # custom login page
└── static/
    └── css/
        └── opera.css           # Opera Home visual theme (black–gold, quiet luxury)
````

---

## ⚙️ Installation & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/sinajokarr/storedjango-main.git
cd storedjango-main

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. (Optional) Create admin user
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open in browser:

* Storefront: `http://127.0.0.1:8000/`
* About: `http://127.0.0.1:8000/about/`
* Contact: `http://127.0.0.1:8000/contact/`
* Cart: `http://127.0.0.1:8000/cart/`
* Login: `http://127.0.0.1:8000/accounts/login/`

---

## 📊 What This Project Shows in a Portfolio

* Clean **Django 5** setup with clear `config/` and app separation
* Use of **Class-Based Views** for typical e-commerce flows
* Professional template inheritance and a **custom design system** in `opera.css`
* A realistic base that can be extended to a full production shop (checkout, discounts, DRF API, analytics, etc.)

---

## 🙏 Feedback & Next Steps

<div align="center">

---

### This repository is both a **Django store starter** and a **showcase project** for Opera Home’s quiet-luxury brand.

If you have ideas for improvements (checkout flow, DRF API, better analytics), feel free to open an issue or a pull request.

---

</div>
```
