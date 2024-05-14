from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN

@receiver(post_save, sender=Book)
def create_isbn(sender, instance, created, **kwargs):
    if created:
        isbn = ISBN.objects.create(book=instance, author=instance.user.username, number='auto-generated ISBN')
