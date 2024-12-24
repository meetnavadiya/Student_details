from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:pk>/',views.details, name='details'),
    path('update/<int:pk>/',views.update, name='update'),
    path('delete/<int:pk>/',views.delete, name='delete'),
]
