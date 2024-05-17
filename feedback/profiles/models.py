from django.db import models

# Create your models here.

class UserProfile(models.Model):
    #image_profile = models.FileField(upload_to="images") #For general files
    image_profile = models.ImageField(upload_to="images") #For images only

    # upload_to="<folder>" ,so the apload folder is: /media/<folder>
