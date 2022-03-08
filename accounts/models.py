from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=250)
    acno=models.CharField(max_length=20)
    ifsc=models.CharField(max_length=20)
    mob=models.CharField(max_length=10)
    pic=models.ImageField(upload_to='images/',default='images/user.png',null=True,blank=True)

    def __str__(self):
        return self.name
