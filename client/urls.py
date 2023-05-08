from django.urls import path
from .views import ClientListView, ClientCreateView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
]
