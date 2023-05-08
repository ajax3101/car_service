from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Service
from .forms import ServiceForm

class ServiceListView(ListView):
    model = Service
    template_name = 'service-list.html'
    context_object_name = 'services'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service-create.html'
    success_url = reverse_lazy('service-list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service-update.html'
    success_url = reverse_lazy('service-list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service-delete.html'
    success_url = reverse_lazy('service-list')
