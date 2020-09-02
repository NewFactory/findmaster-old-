from django.db import models


class City(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Сities'


class Provinces(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provinces'
        verbose_name_plural = 'Provinces'

class Contry(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contry'
        verbose_name_plural = 'Contry'
