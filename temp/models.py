from django.db import models
from django.urls import reverse


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    age = models.IntegerField(verbose_name='Age')
    birthday = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])