from django.urls import path
from .views import CarListView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('car/', CarListView.as_view(), name='car-list'),
    path('car/create/', CarCreateView.as_view(), name='car-create'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
]
