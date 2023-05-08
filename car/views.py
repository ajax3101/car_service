from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm

class CarListView(ListView):
    model = Car
    template_name = 'car-list.html'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car-create.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car-update.html'

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car-list')
    template_name = 'car-delete.html'
