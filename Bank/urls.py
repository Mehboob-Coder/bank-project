
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.list_banks, name='list_banks'),
    path('banks/<int:bank_id>/details/', views.bank_details, name='bank_details'),
    path('banks/<int:bank_id>/add_branch/', views.add_branch, name='add_branch'),
    path('banks/branch/<int:branch_id>/details/', views.branch_details, name='branch_details'),
    path('banks/branch/<int:branch_id>/edit/', views.edit_branch, name='edit_branch'),
    path('banks/add/', views.add_bank, name='add_bank'),
     path('banks/<int:bank_id>/edit/', views.edit_bank, name='edit_bank'),
     path('banks/<int:bank_id>/delete/', views.delete_bank, name='delete_bank'),
    path('branches/<int:branch_id>/delete/', views.delete_branch, name='delete_branch'),
]