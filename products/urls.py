from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.products, name='products-url'),
    path('add-destinations/', my_views.add_products, name='add-products-url'),
    path('delete/<id>', my_views.delete, name='delete-destination-url'),
]
