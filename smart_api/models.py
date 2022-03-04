from django.db import models
from django.db.models.deletion import SET_NULL
# Create your models here.
class Inventory(models.Model):
    id_device = models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    subarea=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

class Iot_device(models.Model):
    token = models.CharField(max_length=250)
    variable=models.CharField(max_length=250)
    measure=models.CharField(max_length=250,default="None")
    machine=models.ForeignKey(Inventory, on_delete=SET_NULL, null=True)
    description=models.CharField(max_length=250)

class Iot_dots_ampers(models.Model):
   
    measure_date=models.DateTimeField(auto_now_add=True)
    value_amper=models.FloatField(default="None")
    value_volt=models.FloatField(default="None")
    measure_amper=models.CharField(max_length=250,default="None")
    measure_volt=models.CharField(max_length=250,default="None")
    device=models.ForeignKey(Iot_device, on_delete=SET_NULL, null=True)

class Iot_tag_dot(models.Model):
   
    measure_date=models.DateTimeField(auto_now_add=True)
    tag_number=models.IntegerField()
    device=models.ForeignKey(Iot_device, on_delete=SET_NULL, null=True)
    
