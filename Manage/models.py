from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=[('Income', 'Income'), ('Expense', 'Expense')])

    def __str__(self):
        return f"{self.title} - {self.amount}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    target_amount = models.FloatField()
    current_amount = models.FloatField(default=0)

    def __str__(self):
        return self.goal_name



