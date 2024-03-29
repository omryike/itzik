from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name
class Loan(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)