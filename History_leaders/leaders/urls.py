from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('countries/', views.country_list, name= 'country_list'),
    path('country/<int:pk>', views.country_detail, name='country_detail'),
    path('leaders/<int:pk>/', views.leader_detail, name='leader_detail'),
    path('search/', views.search_results, name='search_results'),
]