# stocks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.company_list, name="company_list"),
     path('stocks/', views.stock_data_view, name='stock_data'),
]
