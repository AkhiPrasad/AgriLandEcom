from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from AgrilandApp.models import Product, Category, Profile

from payment.forms import ShippingForm
from payment.models import ShippingAddress


# Create your views here.

def mainpgfn(request):
    return render(request, 'Homepg.html')


def market(request):
    products = Product.objects.all()
    return render(request, 'Shoppingpg.html', {'products': products})


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully Signed Up, Please Complete your Profile Details")
            return redirect('update_info')
        else:
            messages.success(request, "Whoops! There was a problem Registering, please try again...")
            return redirect('sg1')
    else:
        return render(request, 'Signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully Logged In, Happy Shopping!")
            return redirect('m1')
        else:
            messages.success(request, "Invalid Credentials")
            return redirect('lg1')
    else:
        return render(request, 'Loginpg.html')


def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('h1')


def category(request, cat):
    cat = cat.replace('-', ' ')
    # taking categry frm url
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, "Selected category doesn't exist")
        return redirect('h1')


def aboutpg(request):
    return render(request, 'aboutpg.html')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, 'Profile updated successfully!')
            return redirect('h1')
        return render(request, 'update_user.html', {'user_form': user_form})

    else:
        messages.success(request, 'Please LOGIN to continue.')
        return redirect('h1')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Updated Successfully')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})

    else:
        messages.success(request, 'Please LOGIN to continue.')
        return redirect('update_password')


def update_info(request):
    if request.user.is_authenticated:
        # Get Current User
        current_user = Profile.objects.get(user__id=request.user.id)
        # Get Current User's Shipping Info
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        # Get original User Form
        form = UserInfoForm(request.POST or None, instance=current_user)
        # Get User's Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            # Save original form
            form.save()
            # Save shipping form
            shipping_form.save()

            messages.success(request, "Your Info Has Been Updated!!")
            return redirect('h1')
        return render(request, "update_info.html", {'form': form, 'shipping_form': shipping_form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('h1')


def shipping_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if shipping_form.is_valid():

            # Save shipping form
            shipping_form.save()
            messages.success(request, 'User Details successfully updated!')
            return redirect('h1')
        return render(request, 'update_info.html', {'shipping_form': shipping_form})

    else:
        messages.success(request, 'Please LOGIN to continue.')
        return redirect('h1')
