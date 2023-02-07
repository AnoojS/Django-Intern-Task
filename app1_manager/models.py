from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Title=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='images')
    User=models.ForeignKey(User,on_delete=models.CASCADE)