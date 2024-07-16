from django.contrib import messages

from django.shortcuts import render, redirect

from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress


# Create your views here.

def payment_success(request):
    return render(request, "payment/payment_success.html")


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total = cart.total()
    if request.user.is_authenticated:
        # checkout as user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html",
                      {'cart_products': cart_products, 'quantities': quantities, 'total': total,
                       'shipping_form': shipping_form})
    # guest login if any
    else:
        shipping_form = ShippingForm(request.POST or None)

    return render(request, "payment/checkout.html",
                  {'cart_products': cart_products, 'quantities': quantities, 'total': total})


def billing_info(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total = cart.total()
    shipping_form = request.POST
    return render(request, "payment/billing_info.html",
                  {'cart_products': cart_products, 'quantities': quantities, 'total': total,
                   'shipping_form': shipping_form})


def process_order(request):
    if request.POST:
        # payment_form = PaymentForm(request.POST or None)
        # my_shipping = request.session.get
        pass
    else:
        messages.success(request, "Access if Denied")
        return redirect('h1')
