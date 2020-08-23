from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    message = models.TextField('Message')

    def __str__(self):
        return self.email