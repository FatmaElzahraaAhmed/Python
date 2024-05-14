from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10), MaxLengthValidator(50)])
    desc = models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    views = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class ISBN(models.Model):
    author = models.CharField(max_length=100)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.number
