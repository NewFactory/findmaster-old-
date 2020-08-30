from django.db import models

# Create your models here.
class Performer(models.Model):
    name = models.CharField('Name', max_length=50)
    web_site = models.URLField('Web site', max_length=100)
    email = models.EmailField('Email', max_length=50)
    create_date = models.DateTimeField('Create', auto_now_add=True)
    change_date = models.DateTimeField('Change', auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Performer'
        verbose_name_plural = 'Performers'


class Review(models.Model):
    Performer = models.ForeignKey(Performer, on_delete = models.CASCADE)
    autor = models.CharField('Autor', max_length=50)
    rating = models.CharField('Rating', max_length=50)
    reviews = models.TextField('Comment', max_length=300)
    create_date = models.DateTimeField('Create', auto_now_add=True)
    change_date = models.DateTimeField('Change', auto_now=True)


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
