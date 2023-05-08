from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Client

class ClientListView(ListView):
    model = Client
    template_name = 'client-list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client-create.html'
    fields = ['name', 'phone_number', 'email']
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client-update.html'
    fields = ['name', 'phone_number', 'email']
    success_url = reverse_lazy('client-list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client-delete.html'
    success_url = reverse_lazy('client-list')
