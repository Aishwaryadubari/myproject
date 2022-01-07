from django.db import models


class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

    class Meta:
        db_table = "hello_world_driver"


class Car(models.Model):
    make = models.TextField()

    model = models.TextField()

    year = models.IntegerField()

    vin = models.TextField()

    owner = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)
