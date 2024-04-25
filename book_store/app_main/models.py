from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# Important! You must read shell_executaded_commands.txt file.

class Book(models.Model):
    #The id autoincrement field is automated inseted by Django.
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    author = models.CharField(null=True, max_length=60)
    #null=True indicated that for blank insertion field the null will write to default value.
    #It's possible declare a default value using default=<> argument
    #You can add the blank=True argument to allow empty fields in the database - by default is's NOT allowed

    #Important: When the class property is modified so it necessary runs makemigrations and migrations

    is_bestselling = models.BooleanField(default=False)

    def __str__(self):      #rewriting all() method
        return f"{self.title} ({self.rating})"
