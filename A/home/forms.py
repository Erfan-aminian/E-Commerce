from django import forms
from .models import ContactUsModel

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md',
                'placeholder': 'نام کامل خود را وارد کنید'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md',
                'placeholder': 'ایمیل خود را وارد کنید'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md',
                'placeholder': 'موضوع پیام را وارد کنید'
            }),
            'message': forms.Textarea(attrs={
                'rows': 6,
                'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md resize-y',
                'placeholder': 'پیام خود را اینجا بنویسید...'
            }),
        }