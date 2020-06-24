from django.db import models

# Create your models here.
class Wish(models.Model):
    wish_list = models.CharField(max_length=200)
    
    def __str__(self):
        return self.wish_list
    
