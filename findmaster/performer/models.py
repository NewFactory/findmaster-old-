import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Group(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField('Name', max_length=50, help_text="///")
    groups = models.ForeignKey(Group, related_name='group_specialization', on_delete=models.SET_NULL, null=True)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)

    def __str__(self):
        return self.name

class Performer(models.Model):
    name = models.CharField('Name', max_length=50)
    specializations = models.ManyToManyField(Specialization)
    web_site = models.URLField('Web site', max_length=100)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField('Phone', max_length=16)
    country = models.ManyToManyField('main.Country')
    provinces = models.ManyToManyField('main.Provinces')
    cities = models.ManyToManyField('main.City')
    option = models.CharField('Option', max_length=30)
    since = models.CharField('Since', max_length=4)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Performer'
        verbose_name_plural = 'Performers'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('performer:detail', args=[str(self.id)])

    def was_published_recently(self):
        return self.create_date >= (timezone.now() - datetime.timedelta(days=7))


class Review(models.Model):
    performers = models.ForeignKey(Performer, on_delete=models.SET_NULL, null=True)
    autor = models.CharField('Autor', max_length=50)
    email = models.EmailField('Email', max_length=50)
    reviews = models.TextField('Reviews', max_length=300)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
