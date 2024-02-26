from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here

class Tipo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
       return self.name 
    
    class Meta:
        db_table = 'tipo'
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
       return self.name 


class employ(models.Model):
    GENDERS = [
        ('Male', 'M'),
        ('Female', 'F')
    ]
    cc = models.CharField(max_length=10, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    employ_type = models.ForeignKey(Tipo, on_delete=models.SET_NULL, related_name='tipo', null=True, blank=True)
    cat = models.ManyToManyField(Category, related_name='category')
    gender = models.CharField(max_length=10, choices=GENDERS, default='Male')
    date_of_hire = models.DateField(default=timezone.now().date())
    created_date = models.DateField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='employs', null=True, blank=True)

    class Meta:
        db_table = 'employ'
        verbose_name_plural = 'employes'

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    