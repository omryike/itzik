from django.shortcuts import render
from .models import Customer,Book,Loan
from .serializers import CustomerSerializer,BookSerializer,LoanSerializer
from rest_framework import viewsets
# Create your views here.

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanView(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer