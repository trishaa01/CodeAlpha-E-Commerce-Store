from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds the database with sample products'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        electronics = Category.objects.create(name='Electronics', slug='electronics', icon='💻')
        fashion = Category.objects.create(name='Fashion', slug='fashion', icon='👗')
        home = Category.objects.create(name='Home & Living', slug='home-living', icon='🏡')
        sports = Category.objects.create(name='Sports', slug='sports', icon='⚽')

        products = [
            {'name': 'Wireless Noise-Cancelling Headphones', 'description': 'Premium audio with 40-hour battery life, deep bass, and foldable design for travel.', 'price': 3499, 'original_price': 5999, 'category': electronics, 'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400', 'stock': 25, 'rating': 4.7, 'review_count': 142, 'is_featured': True},
            {'name': 'Smart Fitness Watch', 'description': 'Track your health 24/7. Heart rate, SpO2, GPS, 7-day battery, 50m water resistance.', 'price': 4999, 'original_price': 7999, 'category': electronics, 'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400', 'stock': 18, 'rating': 4.5, 'review_count': 98, 'is_featured': True},
            {'name': 'Mechanical Keyboard', 'description': 'Tactile RGB mechanical keyboard with Cherry MX switches, full N-key rollover, aluminum frame.', 'price': 2799, 'original_price': None, 'category': electronics, 'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400', 'stock': 12, 'rating': 4.8, 'review_count': 67},
            {'name': 'Portable Bluetooth Speaker', 'description': '360° surround sound, 20-hour playtime, IPX7 waterproof. Perfect for outdoors.', 'price': 1999, 'original_price': 2999, 'category': electronics, 'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400', 'stock': 30, 'rating': 4.4, 'review_count': 211, 'is_featured': True},
            {'name': 'Men\'s Slim Fit Blazer', 'description': 'Premium cotton-blend blazer. Perfect for office or evening out. Available in 3 colors.', 'price': 2499, 'original_price': 3999, 'category': fashion, 'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400', 'stock': 20, 'rating': 4.3, 'review_count': 55},
            {'name': 'Women\'s Floral Sundress', 'description': 'Lightweight cotton sundress with floral print, adjustable straps, midi length. Summer essential.', 'price': 1299, 'original_price': 1899, 'category': fashion, 'image_url': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=400', 'stock': 35, 'rating': 4.6, 'review_count': 134},
            {'name': 'Running Shoes Pro', 'description': 'Lightweight mesh upper, cushioned midsole, anti-slip outsole. For serious runners.', 'price': 3299, 'original_price': 4499, 'category': sports, 'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400', 'stock': 22, 'rating': 4.7, 'review_count': 189, 'is_featured': True},
            {'name': 'Yoga Mat Premium', 'description': 'Non-slip, eco-friendly TPE foam, 6mm thickness, includes carry strap and bag.', 'price': 899, 'original_price': 1299, 'category': sports, 'image_url': 'https://images.unsplash.com/photo-1601925228010-6f05c8c30cef?w=400', 'stock': 50, 'rating': 4.5, 'review_count': 76},
            {'name': 'Scented Soy Candle Set', 'description': 'Set of 3 hand-poured soy candles with calming aromas: lavender, vanilla, and sandalwood.', 'price': 749, 'original_price': None, 'category': home, 'image_url': 'https://images.unsplash.com/photo-1602523961358-f9f03dd557db?w=400', 'stock': 40, 'rating': 4.8, 'review_count': 203},
            {'name': 'Ceramic Plant Pot Set', 'description': 'Modern minimalist ceramic pots, set of 3 sizes. Includes drainage holes and bamboo trays.', 'price': 599, 'original_price': 899, 'category': home, 'image_url': 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400', 'stock': 28, 'rating': 4.4, 'review_count': 91},
            {'name': 'Stainless Steel Water Bottle', 'description': 'Vacuum insulated 750ml bottle. Keeps drinks cold 24h, hot 12h. BPA-free, leakproof.', 'price': 699, 'original_price': 999, 'category': sports, 'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400', 'stock': 60, 'rating': 4.6, 'review_count': 312},
            {'name': 'Wireless Phone Charger', 'description': '15W fast wireless charging pad. Compatible with all Qi-enabled devices. Slim LED indicator.', 'price': 999, 'original_price': 1499, 'category': electronics, 'image_url': 'https://images.unsplash.com/photo-1586816879360-004f5b0c51e3?w=400', 'stock': 45, 'rating': 4.3, 'review_count': 167},
        ]

        for p in products:
            Product.objects.create(**p)

        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(products)} products across 4 categories!'))
