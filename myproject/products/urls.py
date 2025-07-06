from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductCreateView, ProductCreate, ProductDetail


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('allproducts/', ProductCreate.as_view(), name='todo-list-create'),
    path('allproducts/<int:pk>/', ProductDetail.as_view(), name='todo-detail'),
    path('products/', ProductCreateView.as_view(), name='todo-list-create'),
    path('', include(router.urls)),
]
