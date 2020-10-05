from django.db import models

class Message (models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    message = models.TextField('Message')

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
