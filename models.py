from django.db import models

class sqldatabase(models.Model):
    Name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    address = models.TextField(max_length=200)

