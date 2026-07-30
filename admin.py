from django.contrib import admin
from .models import BankAccount

# This makes your BankAccount table visible in the Admin Panel
admin.site.register(BankAccount)
