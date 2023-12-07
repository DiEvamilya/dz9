from django.db import models
from django.urls import reverse

GENDER_CHOICES = [('man', 'man'), ('wuman', 'wuman')]

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

    def get_absolute_url(self):
        return reverse('user_detail', args=(self.pk, ))

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.gender}"