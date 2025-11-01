from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Transaction, Goal
from .forms import TransactionForm, GoalForm



def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)
    income = sum(t.amount for t in transactions if t.type == 'Income')
    expense = sum(t.amount for t in transactions if t.type == 'Expense')
    balance = income - expense
    return render(request, 'main/dashboard.html', {
        'transactions': transactions,
        'goals': goals,
        'balance': balance,
        'income': income,
        'expense': expense,
    })
@login_required
def add_transaction_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'main/add_transaction.html', {'form': form})

@login_required
def add_goal_view(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'main/add_goal.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



def transactions_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'main/view_transaction.html', {'transactions': transactions})

@login_required
def edit_transaction_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'main/edit_transaction.html', {'form': form})


@login_required
def delete_transaction_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        transaction.delete()
        return redirect('transaction')
    return render(request, 'main/delete_transaction.html', {'transaction': transaction})