from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
import json
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    sort = request.GET.get('sort', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_slug:
        products = products.filter(category__slug=category_slug)
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'rating':
        products = products.order_by('-rating')
    elif sort == 'newest':
        products = products.order_by('-created_at')

    featured = Product.objects.filter(is_featured=True)[:4]
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'featured': featured,
        'query': query,
        'category_slug': category_slug,
        'sort': sort,
        'cart_count': cart_count,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related': related,
        'cart_count': cart_count,
    })

@require_POST
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    key = str(pk)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    cart_count = sum(cart.values())
    return JsonResponse({'success': True, 'cart_count': cart_count, 'message': f'{product.name} added to cart!'})

@require_POST
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    key = str(pk)
    if key in cart:
        del cart[key]
    request.session['cart'] = cart
    cart_count = sum(cart.values())
    return JsonResponse({'success': True, 'cart_count': cart_count})

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for pk, qty in cart.items():
        try:
            product = Product.objects.get(pk=int(pk))
            subtotal = product.price * qty
            total += subtotal
            cart_items.append({'product': product, 'qty': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass
    cart_count = sum(cart.values())
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'cart_count': cart_count,
    })

@require_POST
def update_cart(request, pk):
    data = json.loads(request.body)
    qty = int(data.get('qty', 1))
    cart = request.session.get('cart', {})
    key = str(pk)
    if qty <= 0:
        cart.pop(key, None)
    else:
        cart[key] = qty
    request.session['cart'] = cart
    cart_count = sum(cart.values())
    total = 0
    for p, q in cart.items():
        try:
            product = Product.objects.get(pk=int(p))
            total += float(product.price) * q
        except:
            pass
    return JsonResponse({'success': True, 'cart_count': cart_count, 'total': total})

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('home')
    
    cart_items = []
    total = 0
    for pk, qty in cart.items():
        try:
            product = Product.objects.get(pk=int(pk))
            subtotal = product.price * qty
            total += subtotal
            cart_items.append({'product': product, 'qty': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass

    if request.method == 'POST':
        # Clear cart after order
        request.session['cart'] = {}
        return redirect('order_success')

    cart_count = sum(cart.values())
    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'cart_count': cart_count,
    })

def order_success(request):
    cart_count = 0
    return render(request, 'store/order_success.html', {
        'cart_count': cart_count,
    })