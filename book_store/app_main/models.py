from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
# Important! You must read shell_executaded_commands.txt file.

class Country(models.Model): #Many to Many relation
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=80)

    def __str__(self):
        return self.name + " - " + self.code

    #To correct label on django admin site (not Countrys)
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return  self.street + " - " + self.city

    #To correct label on django admin site (not Addresss)
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) #One-to-one relation
    #For one-to-one relation isn't necessary related_name="<string>" param.

    def full_name(self):
        return self.first_name + " " + self.last_name

    #Reescreve o método que retorna a string do campo Author da classe Book
    #e também da coluna Author do Book Admin site.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    #The id autoincrement field is automated inseted by Django.
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    #Book and Author are 1xN relation, because 1 Author can write many books.
    #Author param is a pointer for the author table
    #on_delete specify what happen is a author will detele
    #CASCADE means that if the author was delete all related books also will delete

    #author = models.CharField(null=True, max_length=60)
    #null=True indicated that for blank insertion field the null will write to default value.
    #It's possible declare a default value using default=<> argument
    #You can add the blank=True argument to allow empty fields in the database - by default is's NOT allowed

    #slug = models.SlugField(default="", editable=False, blank=True, null=False, db_index=True)
    #blank means this field will be set blank
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    #Many to Many relation
    #For this relation isn't necessary set-up on_delete
    #It's possible to indicate related_name=<name> for many-to-many relation
    published_countries = models.ManyToManyField(Country)

    #Important: When the class property is modified so it necessary runs makemigrations and migrations

    is_bestselling = models.BooleanField(default=False)

    def __str__(self):      #rewriting all() method
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)    #Transform a string to slug
        super().save(*args, **kwargs)  #Call original superclass method
