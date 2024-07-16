from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="",
                                         widget=forms.TextInput(
                                             attrs={'class': 'form-control', 'placeholder': 'Phone'}),
                                         required=True)
    shipping_phone = forms.CharField(label="",
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
                                     required=True)
    shipping_email = forms.CharField(label="",
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname'}),
                                     required=True)
    shipping_address1 = forms.CharField(label="",
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Address'}),
                                        required=True)
    shipping_address2 = forms.CharField(label="",
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Confirm Address'}),
                                        required=True)
    shipping_city = forms.CharField(label="",
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
                                    required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_phone', 'shipping_email', 'shipping_address1', 'shipping_address2',
                  'shipping_city']

        exclude = ['user',]


class PaymentForm(forms.Form):
    upi_id = forms.CharField(label="",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Enter your UPI ID'}),
                             required=True)
