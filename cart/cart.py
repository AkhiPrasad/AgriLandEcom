from profile import Profile

from django.contrib.auth.models import User

import cart
from AgrilandApp.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        # get req
        self.request = request
        # to get current session key

        cart = self.session.get('session_key')
        # if new user no session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

            # cart available in all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        # to loginuser cart persistenace

        # if self.request.user.is_authenticated:
        #     # Get the current user profile
        #     current_user = Profile.objects.filter(user__id=self.request.user.id)
        #     # Convert {'3':1, '2':4} to {"3":1, "2":4}
        #     carty = str(self.cart)
        #     carty = carty.replace("\'", "\"")
        #     # Save carty to the Profile Model
        #     current_user.update(old_cart=str(carty))

    def total(self):
        # to get pro id
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            # converting  string to int
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # to get all ids from products
        product_ids = self.cart.keys()

        productss = Product.objects.filter(id__in=product_ids)

        return productss

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart

        ourcart[product_id] = product_qty

        self.session.modified = True

        up = self.cart
        return up

    def delete(self, product):
        product_id = str(product)
        # to del from dic
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
