from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm

class OrderListView(ListView):
    model = Order
    template_name = 'order-list.html'
    context_object_name = 'orders'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order-create.html'

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order-update.html'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')
    template_name = 'order-delete.html'
    
    def delete(self, request, *args, **kwargs):
        """
        Переопределяем метод delete для добавления дополнительной логики перед удалением заказа.
        """
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
