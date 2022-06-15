from api import views
from django.urls import path

urlpatterns = [
    path('api/GetUser', views.get_user, name='get-user'),
    path('api/Register', views.add_user, name='register'),
    path('api/GetAllProducts', views.list_products, name='get-all-products'),
    path('api/CreateProduct', views.add_product, name='add-product'),
    path('api/DeleteProduct', views.delete_product, name='delete-product'),
    path('api/PurchaseProduct', views.purchase_product, name='purchase-product'),
    path('api/DeletePurchaseProduct', views.delete_purchase_product, name='delete-purchase-product'),
    path('api/PurchaseList', views.purchase_list, name='purchase-list'),
    path('api/Recommend', views.recommend, name='api'),
]