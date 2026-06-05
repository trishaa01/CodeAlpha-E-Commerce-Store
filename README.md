# ShopNova — Improved Django E-Commerce

A modern, fully-featured e-commerce application built with Django.

## Features
- 🎨 Beautiful modern UI with Tailwind CSS, animations, gradients
- 🔍 Product search and category filtering
- 🛒 Fully functional shopping cart (session-based, AJAX)
- 📦 Product detail pages with related products
- ⭐ Ratings, reviews count, discount badges
- 📱 Fully responsive mobile-first design
- 🔥 Hero banner with featured products
- 🗂️ Category navigation pills
- 🔃 Sorting (price, rating, newest)

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data        # Load 12 sample products
python manage.py createsuperuser  # Optional: for admin panel
python manage.py runserver
```

Then visit: http://127.0.0.1:8000/

## Models
- **Category**: name, slug, icon emoji
- **Product**: name, description, price, original_price, category, image_url, stock, rating, review_count, is_featured

## Admin
Visit `/admin/` to manage products and categories.
