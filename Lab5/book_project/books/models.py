from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)  # Rating out of 10.0
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
