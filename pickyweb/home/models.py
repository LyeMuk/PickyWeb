from django.db import models

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=100)
    detail = models.CharField(max_length=200)
    pic = models.CharField(max_length=1000)

    def __str__(self):
        return self.tag


class Links(models.Model):
    url = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}-                     ------            -{self.tag}"

