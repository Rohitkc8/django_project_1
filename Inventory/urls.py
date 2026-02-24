from django.urls import path
from .views import *

urlpatterns=[
    path('home/',HomePage),
    path('page/',navbarPage),
    path('about/',aboutPage),
    path('contact/',contactPage),
    path('service/',servicePage),
    path('project/',projectPage),
    path('products/add/',products_add),
    path('products/',All_products),
    path('products/delete/<int:id>/',Delete_Product,name='product_delete'),
    path('products/update/<int:id>/',Update_Product,name='product_update'),
]