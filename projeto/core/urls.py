from django.urls import path
from core.views import IndexView, CreateProduct, UpdateProductView, DetailProductView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateProduct.as_view(), name='create_product'),
    path('detail/<int:pk>/', DetailProductView.as_view(), name='detail_product'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update_product'),

]