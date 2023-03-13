from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    emp_img=models.ImageField(upload_to='image',null=True)
    emp_name=models.CharField(max_length=250,null=True)
    emp_det=models.TextField(null=True)
