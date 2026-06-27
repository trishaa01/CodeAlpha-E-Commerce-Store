# 🛒 CodeAlpha E-Commerce Store

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat&logo=django)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38bdf8?style=flat&logo=tailwindcss)
![Status](https://img.shields.io/badge/Status-Live-success?style=flat)
![Internship](https://img.shields.io/badge/CodeAlpha-Internship-orange?style=flat)

A modern, fully-featured e-commerce web application built with **Django** and **Tailwind CSS**, developed as **Task 1** of the **CodeAlpha Internship Program**.

🌐 **Live Demo:** [Click here to view](https://shopnova-tx0g.onrender.com)

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
- 💰 Discount percentage and original price display
- 📱 Fully responsive mobile-friendly design
- 🎨 Modern UI with animations and gradients
- 🧾 Full checkout form with delivery address
- 💳 Payment method selection (COD, UPI, Card)
- ✅ Order confirmation page with delivery steps
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
| Gunicorn | Production server |
| Whitenoise | Static files serving |
| Render | Cloud deployment |

---

## 🚀 Getting Started

### 1. Clone the repository
```text
git clone https://github.com/trishaa01/CodeAlpha-E-Commerce-Store.git
cd CodeAlpha-E-Commerce-Store
```

### 2. Install dependencies
```text
pip install -r requirements.txt
```

### 3. Run migrations
```text
python manage.py migrate
```

### 4. Load sample products
```text
python manage.py seed_data
```

### 5. Create admin account (optional)
```text
python manage.py createsuperuser
```

### 6. Start the server
```text
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## 📁 Project Structure

```text
CodeAlpha-E-Commerce-Store/
├── ecommerce/               # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                   # Main app
│   ├── models.py            # Product & Category models
│   ├── views.py             # All views
│   ├── urls.py              # URL routes
│   ├── admin.py             # Admin configuration
│   ├── templates/           # HTML templates
│   │   └── store/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       └── order_success.html
│   └── management/          # Custom commands
│       └── commands/
│           └── seed_data.py
├── build.sh                 # Render build script
├── manage.py
└── requirements.txt
```

---

## 🔮 Future Improvements

- 💳 **Real Payment Integration** — Connect Razorpay or PayU for actual UPI, card and net banking payments
- 📧 **Email Notifications** — Send order confirmation emails to customers automatically
- 👤 **User Authentication** — Register, login and view past orders
- 📦 **Order Tracking** — Real-time order status tracking page
- ❤️ **Wishlist** — Save products for later
- 🌟 **Product Reviews** — Let users write and submit reviews
- 🔎 **Advanced Filters** — Filter by price range, brand, rating
- 📊 **Admin Dashboard** — Sales charts and analytics for admin
- 🖼️ **Image Upload** — Upload product images instead of using URLs
- 🌍 **Multi-language Support** — Hindi and regional language support
- 📱 **PWA Support** — Make it installable as a mobile app

---

## 👩‍💻 Author

**Trisha** — CodeAlpha Internship Task 1

[![GitHub](https://img.shields.io/badge/GitHub-trishaa01-black?style=flat&logo=github)](https://github.com/trishaa01)

