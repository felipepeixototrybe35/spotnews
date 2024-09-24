from django.db import models
from django.forms import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=False)

    # Validação para garantir que o título tenha mais de uma palavra
    def clean(self):
        if len(self.title.split()) < 2:
            raise ValidationError('O título deve ter mais de uma palavra.')

    def __str__(self):
        return self.title
