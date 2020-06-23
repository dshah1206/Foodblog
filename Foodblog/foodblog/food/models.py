from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=70,blank=False,null=False)
    email = models.EmailField(max_length=70,blank=True,null=True)
    dishname = models.CharField(max_length=50,blank=False,null=False)
    review= models.TextField(blank=False,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.name + " - " + self.dishname

    