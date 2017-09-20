from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    thumbnail = models.ImageField()
    date = models.CharField(max_length=10)
    link = models.CharField(max_length=1000)
    def __str__(self):
        return self.name + ' - ' + self.date


