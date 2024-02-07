from django.db import models

class Apartment(models.Model):
    adress = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    # cost = models.IntegerField() #TODO

class ImageNames(models.Model):
    pass
    
class BookedDate(models.Model):
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        )
    date_from = models.DateTimeField()
    date_until = models.DateTimeField()

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    date = models.OneToOneField(
        BookedDate,
        on_delete=models.CASCADE,
        primary_key=True,
        )
