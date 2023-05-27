from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.store, name="store"),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
=======
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name ='search'),
>>>>>>> 0afb77cd8c389fc020fa6622693f504778a742e7
]
