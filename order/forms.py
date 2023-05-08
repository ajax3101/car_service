from django import forms
from .models import Order



class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client')
    car = forms.ModelChoiceField(queryset=Car.objects.all(), label='Car')
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(),
                                              label='Services')
    price = forms.DecimalField(label='Price', help_text='Enter the total price for the order.')
    status = forms.ChoiceField(choices=Order.STATUS_CHOICES, label='Status')

    class Meta:
        model = Order
        fields = ['client', 'car', 'services', 'price', 'status']
