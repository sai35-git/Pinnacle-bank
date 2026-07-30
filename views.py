from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BankAccount

@csrf_exempt
def home(request):
    context = {}
    # Check if a user is currently logged in
    if request.user.is_authenticated:
        account = BankAccount.objects.filter(user=request.user).first()
        context['account'] = account

    return render(request, 'index.html', context)

@login_required
def dashboard(request):
    account = BankAccount.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {'account': account})