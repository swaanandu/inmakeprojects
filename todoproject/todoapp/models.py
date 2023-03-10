from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=250)
    priority = models.IntegerField()
    datefield=models.DateField()
def __str__(self):
    self.name