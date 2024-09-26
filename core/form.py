# forms.py
from django import forms
from .models import BaylingAddress
from core.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    review =  forms.CharField(widget=forms.Textarea(attrs={'placeholder':'add your comment','class':'w-full h-24 m-2'}))
    
    class Meta:
        model = ProductReview
        fields = ['review','rating']
        

class BaylingAddressForm(forms.ModelForm):
    class Meta:
        model = BaylingAddress
        fields = [
            'your_name',
            'phone_number',
            'email',
            'division',
            'district',
            'home_address'
        ]
        widgets = {
            'your_name': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-500',
                'placeholder': 'Enter your name',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-500',
                'placeholder': 'Enter your phone number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-500',
                'placeholder': 'Enter your email',
            }),
            'division': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-500',
            }),
            'district': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-500',
            }),
            'home_address': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-500',
                'placeholder': 'Enter your home address',
            }),
        }
