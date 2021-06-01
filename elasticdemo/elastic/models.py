from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])
class log(models.Model):
    host_id   = models.IntegerField()
    host_name = models.CharField(max_length=100)
    start_time= models.TimeField()
    date= models.DateField()
    type = models.TextField()