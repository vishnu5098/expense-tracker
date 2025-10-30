from django.contrib import admin
from .models import Transaction, Goal

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'amount', 'type', 'date')
    list_filter = ('type', 'date')
    search_fields = ('title', 'user__username')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_name', 'target_amount', 'current_amount')
    search_fields = ('goal_name', 'user__username')

