from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_extended (models.Model):

    id_usuario= models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True,related_name='id_usuario_user_extended')
    fecha_nacimiento= models.CharField(max_length=30)
    ciudad_residencia= models.CharField(max_length=30)
    estado_civil= models.CharField(max_length=30)
    sexo= models.CharField(max_length=10)
    estrato= models.IntegerField()
    tel_celular= models.IntegerField()
    identificacion= models.IntegerField()
    direccion= models.CharField(max_length=30)
    barrio= models.CharField(max_length=30)

    class Meta:
        db_table = "user_extended"
    def __str__(self):
        return str(self.id_usuario)
    
    #rol
# class user_extended (models.Model):

#     id_usuario= models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True,related_name='id_usuario_user_extended')
#     fecha_nacimiento= models.CharField(max_length=30)
#     ciudad_residencia= models.CharField(max_length=30)
#     estado_civil= models.CharField(max_length=30)
#     sexo= models.CharField(max_length=10)
#     estrato= models.IntegerField()
#     tel_celular= models.IntegerField()
#     identificacion= models.IntegerField()
#     direccion= models.CharField(max_length=30)
#     barrio= models.CharField(max_length=30)

#     class Meta:
#         db_table = "user_extended"
#     def __str__(self):
#         return str(self.id_usuario)

#     #usuario_rol