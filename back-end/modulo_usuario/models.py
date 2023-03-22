from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class usuario (models.Model):
    codigo= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='CODIGO')
    deleted= models.BooleanField()
    nombre= models.CharField(max_length=100)
    password= models.CharField(max_length=300)
    email= models.CharField(max_length=100)

    class Meta:
        db_table = "usuario"
    def __str__(self):
        return str(self.codigo)

