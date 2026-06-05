# 🛒 ShopNova E-Commerce Store

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat&logo=django)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38bdf8?style=flat&logo=tailwindcss)
![Status](https://img.shields.io/badge/Status-Complete-success?style=flat)

A modern, fully-featured e-commerce web application built with **Django** and **Tailwind CSS**, developed as **Task 1** of the **CodeAlpha Internship Program**.

---

## 🌟 Features

- 🏠 Hero banner with featured products and animations
- 📦 Product catalog with images, ratings and discount badges
- 🔍 Keyword search and category filtering
- 🔃 Sort by price, rating and newest
- 🛒 AJAX-powered shopping cart with no page reload
- ➕ Add, remove and update cart quantities live
- 📄 Product detail pages with related products
- ⭐ Star ratings and review counts
- 💰 Discount percentage display
- 📱 Fully responsive mobile-friendly design
- 🎨 Modern UI with animations and gradients
- 🔧 Django admin panel to manage products

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python & Django | Backend framework |
| SQLite | Database |
| Tailwind CSS | Styling & UI |
| HTML & JavaScript | Frontend |
| Font Awesome | Icons |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/trishaa01/CodeAlpha-E-Commerce-Store.git
cd CodeAlpha-E-Commerce-Store
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Load sample products
```bash
python manage.py seed_data
```

### 5. Create admin account (optional)
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## 📁 Project Structure

```text
CodeAlpha-E-Commerce-Store/
├── ecommerce/          # Project settings & URLs
├── store/              # Main app
│   ├── models.py       # Product & Category models
│   ├── views.py        # All views
│   ├── urls.py         # URL routes
│   ├── admin.py        # Admin configuration
│   ├── templates/      # HTML templates
│   └── management/     # Custom commands (seed_data)
├── manage.py
└── requirements.txt

```

---

## 👩‍💻 Author

**Trisha** — CodeAlpha Internship Task 1

[![GitHub](https://img.shields.io/badge/GitHub-trishaa01-black?style=flat&logo=github)](https://github.com/trishaa01)

---

## 📜 License

This project is developed for educational purposes as part of the **CodeAlpha Internship Program**.
