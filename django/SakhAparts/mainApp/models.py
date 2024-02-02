from django.db import models

# Create your models here.
class ListItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    

class User(models.Model):
    pass
    
    
class ApartItem(models.Model):
    pass
    

class BookedDate(models.Model):
    pass