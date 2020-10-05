from django.db import models

class Country(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)

    def __str__(self):
        return self.name


class Provinces(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)


    def __str__(self):
        return self.name


class City(models.Model):
    provinces = models.ForeignKey(Provinces, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField('Create')
    change_date = models.DateTimeField('Change', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Сities'
