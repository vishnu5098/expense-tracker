from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_transaction/', views.add_transaction_view, name='add_transaction'),
    path('add_goal/', views.add_goal_view, name='add_goal'),
    path('logout/', views.logout_view, name='logout'),
    path('transaction/', views.transactions_view, name='transaction'),
    path('transaction/<int:pk>/edit/', views.edit_transaction_view, name='edit_transaction'),
    path('transaction/<int:pk>/delete/', views.delete_transaction_view, name='delete_transaction')
    
]
