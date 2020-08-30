from django.db import models

# Create your models here.
class Order (models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    #city = models.CharField('City', max_length=50)
    message = models.TextField('Message')

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
