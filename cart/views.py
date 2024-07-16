from django.shortcuts import render, get_object_or_404
from .cart import Cart
from AgrilandApp.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total = cart.total()

    return render(request, 'cart_summary.html',
                  {'cart_products': cart_products, 'quantities': quantities, 'total': total})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # to get
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)

        # to session
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Product added to cart")
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        # delete func
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        messages.success(request, "Item removed from cart")
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        messages.success(request, "Your cart has been updated!")
        return response
        # return redirect('cart_summary')


def payment_success():
    return None