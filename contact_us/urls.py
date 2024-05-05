from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]