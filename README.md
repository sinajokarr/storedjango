````markdown
<div align="center">
  
# 🛒 Opera Home Store – Quiet Luxury Django E-commerce Template ✨
  
***

[![Tech: Django](https://img.shields.io/badge/Backend-Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Language: Python](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Frontend: HTML/CSS](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Auth: Custom User](https://img.shields.io/badge/Auth-Custom%20User%20Model-6366f1?style=for-the-badge)](#)
[![API: Cart Endpoint](https://img.shields.io/badge/API-DRF%20Cart%20Summary-10b981?style=for-the-badge)](#)
  
***
</div>

<br>

## 🎯 About This Project: A Quiet-Luxury Storefront

**Opera Home Store** is a Django-based e-commerce template for home décor and lifestyle brands that want a **minimal, quiet-luxury UI** instead of a noisy, overloaded catalogue.

The project now includes a **custom user system, polished auth pages (Sign up / Log in / Log out)** and a **contact form with backend validation**, so it behaves like a realistic small store you can extend to production.

The goal is to provide:

- A realistic storefront you can plug real products and customers into  
- Clean, semantic Django templates ready to extend to production  
- A strong portfolio project showing **CBVs, custom user model, template inheritance, forms and a small DRF endpoint**

<br>

### 📬 Author & Project Links

| Type | Link |
| :--- | :--- |
| 👤 **Author** | [Sina Jokar – Backend Developer](https://www.linkedin.com/in/sinajokar/) |
| 📦 **Repository** | [`storedjango`](https://github.com/sinajokarr/storedjango) on GitHub |
| 📧 **Contact** | [cnajokar11@yahoo.com](mailto:cnajokar11@yahoo.com) |

---

## 🛠️ Tech Stack: What Powers Opera Home

A compact overview of the technologies behind the storefront.

### 🌐 Backend, Auth & Templates

| Category | Stack |
| :--- | :--- |
| **Language** | `Python 3.x` |
| **Framework** | `Django 5.x` (Class-Based Views) |
| **Templating** | Django Template Language (DTL) with `_base.html` layout |
| **Auth** | Custom user model `accounts.CustomUser` + Django auth views (`LoginView`, `LogoutView`, password change) |
| **Forms** | `CustomUserCreationForm`, `CustomAuthenticationForm`, and `ContactForm` (FormView-based contact page) |

<p align="center">
  <img src="https://img.shields.io/badge/Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge">
</p>

### 💾 Data, Static Files & Tooling

| Category | Stack |
| :--- | :--- |
| **Database (dev)** | `SQLite` (`db.sqlite3`) |
| **Static Assets** | Custom CSS theme `static/css/opera.css` (quiet-luxury, soft neutral palette) |
| **Views** | CBVs for product list/detail/cart/about + FormView for contact |
| **API** | Lightweight DRF endpoint for cart summary (`/api/cart/retrieve_cart/`) used in the header cart counter |
| **Runtime** | `python manage.py runserver` local dev |

---

## 💻 Opera Home Store: Features & UX

A breakdown of what this template demonstrates.

### 🏬 Storefront & Cart

* Product listing with grid layout and category filtering  
* Product detail page (image, title, description, price, category)  
* Cart page for adding/removing items and reviewing selections  
* Empty states that keep the UI clean when there is no data yet  
* Header cart counter powered by a small DRF endpoint (`retrieve_cart`)  

### 👥 Accounts & Auth (Custom User)

* Custom user model with fields like **username, email, phone** (and extensible for avatar / agency info)  
* Clean, luxury-style **Sign up** page (`accounts/templates/accounts/signup.html`)  
* Custom-styled **Log in** page (`templates/registration/login.html`) using `CustomAuthenticationForm`  
* Simple **Log out** flow with `logged_out.html` template and redirect to product list  
* Auth-aware navigation in `_base.html` (shows “Sign In / Sign Up” or “Hello, {{ user }} / Log out / Cart”)  

### 🧭 Brand Pages & Contact

* **About** page explaining Opera Home’s “Quiet Luxury” philosophy  
* **Contact** page wired to a real `ContactForm` + `FormView`:
  - Validates input server-side  
  - Uses Django messages framework to show success alerts  
  - Keeps the premium layout with client-care info and FAQ sections  
* All pages extend `_base.html` to reuse header, footer and navigation  

---

## 🧱 Project Structure (Simplified)

```bash
storedjango/
├── accounts/
│   ├── models.py                 # CustomUser model
│   ├── forms.py                  # CustomUserCreationForm, CustomAuthenticationForm
│   ├── views.py                  # SignUpView + custom_logout
│   ├── urls.py                   # login / logout / signup / password-change urls
│   └── templates/
│       ├── accounts/
│       │   └── signup.html       # Sign up page (quiet-luxury card)
│       └── registration/
│           ├── login.html        # Custom login page
│           └── logged_out.html   # Logged-out screen
├── config/
│   ├── settings.py               # INSTALLED_APPS, AUTH_USER_MODEL, STATIC/MEDIA, templates
│   └── urls.py                   # include store + accounts urls
├── store/
│   ├── models.py                 # Product, Category, Customer, Cart
│   ├── forms.py                  # ContactForm for contact page
│   ├── views.py                  # CBVs for list/detail/cart/about/contact (FormView)
│   ├── urls.py                   # namespaced 'store:' urls
│   └── templates/
│       └── store/
│           ├── product_list.html
│           ├── product_detail.html
│           ├── cart_detail.html
│           ├── product_form.html
│           ├── delete_product.html
│           ├── about.html
│           └── contact.html
├── templates/
│   └── _base.html                # main layout (header/nav/footer + cart counter)
└── static/
    └── css/
        └── opera.css             # Opera Home visual theme (quiet luxury)
````

---

## ⚙️ Installation & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/sinajokarr/storedjango.git
cd storedjango

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
* Contact (FormView + success message): `http://127.0.0.1:8000/contact/`
* Cart: `http://127.0.0.1:8000/cart/`
* Login: `http://127.0.0.1:8000/accounts/login/`
* Sign up: `http://127.0.0.1:8000/accounts/signup/`

---

## 📊 What This Project Shows in a Portfolio

* Clean **Django 5** setup with clear `config/` and app separation
* Use of **Class-Based Views + FormView** for typical e-commerce flows
* A proper **custom user model** with custom forms and templates
* Professional template inheritance and a **custom design system** in `opera.css`
* A realistic base that can be extended to a full production shop (checkout, discounts, more DRF APIs, analytics, etc.)

---

## 🙏 Feedback & Next Steps

<div align="center">

---

### This repository is both a **Django store starter** and a **showcase project** for Opera Home’s quiet-luxury brand.

If you have ideas for improvements (checkout flow, richer DRF API, better analytics), feel free to open an issue or a pull request.

</div>
```
