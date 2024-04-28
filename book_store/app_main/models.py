from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

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

    #slug = models.SlugField(default="", editable=False, blank=True, null=False, db_index=True)
    #blank means this field will be set blank
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    #Important: When the class property is modified so it necessary runs makemigrations and migrations

    is_bestselling = models.BooleanField(default=False)

    def __str__(self):      #rewriting all() method
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)    #Transform a string to slug
        super().save(*args, **kwargs)  #Call original superclass method
